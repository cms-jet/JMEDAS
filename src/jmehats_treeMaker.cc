////////////////////////////////////////////////////////////////////////////////
//
// treeMaker
// ---------
//
//                        06/15/2015 Alexx Perloff   <aperloff@physics.tamu.edu>
////////////////////////////////////////////////////////////////////////////////

#include "Analysis/JMEDAS/interface/jmehats_ntuple.h"

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"
 
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Common/interface/Ref.h"
#include "DataFormats/Common/interface/RefToBase.h"
#include "DataFormats/Common/interface/RefVector.h"
#include "DataFormats/Common/interface/ValueMap.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/Candidate/interface/CandMatchMap.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/JetCollection.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/MuonReco/interface/MuonFwd.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/deltaPhi.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"

#include "JetMETCorrections/Objects/interface/JetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"

#include "SimDataFormats/JetMatching/interface/JetMatchedPartons.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"

#include <TH1F.h>
#include <TH2F.h>
#include <TTree.h>

#include <memory>
#include <vector>
#include <iostream>
#include <string>
#include <iomanip>
#include <sstream>
#include <cmath>

using namespace std;

////////////////////////////////////////////////////////////////////////////////
// class definition
////////////////////////////////////////////////////////////////////////////////

class treeMaker : public edm::EDAnalyzer
{
public:
  // construction/destruction
  explicit treeMaker(const edm::ParameterSet& iConfig);
  virtual ~treeMaker();

private:
  // member functions
  void beginJob();
  void analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup);
  void endJob(){;}
  double getJERfactor(double pt, double eta, double ptgen);

private:
  // member data
  std::string   moduleLabel_;
  std::string   JetCorLabel_;
  std::vector<std::string> JetCorLevels_;

  edm::InputTag srcJet_;
  edm::InputTag srcRho_;
  edm::InputTag srcVtx_;

  bool          doComposition_;
  bool          doFlavor_;
  bool          doJER_;
  string        JERUncertainty_;
  bool          doJESUncertainty_;
  string        JESUncertainty_;
  string        JESUncertaintyType_;
  string        JESUncertaintyFile_;
  unsigned int  nJetMax_;
  double        deltaRMax_;
  double        deltaPhiMin_;
  double        deltaRPartonMax_;
  double        JERCor;
  double        jesUncScale;
  double        uncert;

  int           nref_;
  FactorizedJetCorrector* jetCorrector_;
  JetCorrectionUncertainty* jecUnc;
  
  // tree
  TTree*        tree_;
  ntuple* PUNtuple_;
};


////////////////////////////////////////////////////////////////////////////////
// construction/destruction
////////////////////////////////////////////////////////////////////////////////

//______________________________________________________________________________
treeMaker::treeMaker(const edm::ParameterSet& iConfig)
  : moduleLabel_       (iConfig.getParameter<std::string>            ("@module_label"))
  , JetCorLabel_       (iConfig.getParameter<std::string>              ("JetCorLabel"))
  , JetCorLevels_      (iConfig.getParameter<vector<string> >         ("JetCorLevels"))
  , srcJet_            (iConfig.getParameter<edm::InputTag>                 ("srcJet"))
  , srcRho_            (iConfig.getParameter<edm::InputTag>                 ("srcRho"))
  , srcVtx_            (iConfig.getParameter<edm::InputTag>                 ("srcVtx"))
  , doComposition_     (iConfig.getParameter<bool>                   ("doComposition"))
  , doFlavor_          (iConfig.getParameter<bool>                        ("doFlavor"))
  , doJER_             (iConfig.getParameter<bool>                           ("doJER"))
  , JERUncertainty_    (iConfig.getParameter<string>                ("JERUncertainty"))
  , doJESUncertainty_  (iConfig.getParameter<bool>                ("doJESUncertainty"))
  , JESUncertainty_    (iConfig.getParameter<string>                ("JESUncertainty"))
  , JESUncertaintyType_(iConfig.getParameter<string>            ("JESUncertaintyType"))
  , JESUncertaintyFile_(iConfig.getParameter<string>            ("JESUncertaintyFile"))
  , nJetMax_           (iConfig.getParameter<unsigned int>                 ("nJetMax"))
  , deltaRMax_(0.0)
  , deltaPhiMin_(3.141)
  , deltaRPartonMax_(0.0)
  , jetCorrector_(0)
{

  if (iConfig.exists("deltaRMax")) {
    deltaRMax_=iConfig.getParameter<double>("deltaRMax");
  }
  else
    throw cms::Exception("MissingParameter")<<"Set *either* deltaRMax (matching)"
					    <<" *or* deltaPhiMin (balancing)";

  if ( iConfig.exists("JESUncertainty") ){
    if (JESUncertainty_ == "up" || JESUncertainty_ == "down") {
      jecUnc =  new JetCorrectionUncertainty(*(new JetCorrectorParameters(JESUncertaintyFile_, JESUncertaintyType_)));
    }
  }
}


//______________________________________________________________________________
treeMaker::~treeMaker()
{

}


////////////////////////////////////////////////////////////////////////////////
// implementation of member functions
////////////////////////////////////////////////////////////////////////////////

//______________________________________________________________________________
void treeMaker::beginJob()
{
  edm::Service<TFileService> fs;
  if (!fs) throw edm::Exception(edm::errors::Configuration,
				"TFileService missing from configuration!");
  
  tree_=fs->make<TTree>("t","t");
  PUNtuple_ = new ntuple(tree_,true);

}


//______________________________________________________________________________
void treeMaker::analyze(const edm::Event& iEvent,
                                  const edm::EventSetup& iSetup)
{
  // EVENT DATA HANDLES
  nref_=0;
  edm::Handle<GenEventInfoProduct>               genInfo;
  edm::Handle<vector<PileupSummaryInfo> >        puInfos;  
  edm::Handle<std::vector<pat::Jet> >            jets;
  edm::Handle<double>                            rho;
  edm::Handle<std::vector<reco::Vertex> >        vtx;

  //RHO INFORMATION
  PUNtuple_->rho = 0.0;
  if (iEvent.getByLabel(srcRho_,rho)) {
    PUNtuple_->rho = *rho;
  }
 
  //NPV INFORMATION
  PUNtuple_->npv = 0;
  if (iEvent.getByLabel(srcVtx_,vtx)) {
     const reco::VertexCollection::const_iterator vtxEnd = vtx->end();
     for (reco::VertexCollection::const_iterator vtxIter = vtx->begin(); vtxEnd != vtxIter; ++vtxIter) {
        if (!vtxIter->isFake() && vtxIter->ndof()>=4 && fabs(vtxIter->z())<=24)
           PUNtuple_->npv++;
     }
  }
 
  //EVENT INFORMATION
  PUNtuple_->run = iEvent.id().run();
  PUNtuple_->lumi = iEvent.id().luminosityBlock();
  PUNtuple_->evt = iEvent.id().event();

  // MC PILEUP INFORMATION
  PUNtuple_->npus->clear();
  PUNtuple_->tnpus->clear();
  PUNtuple_->bxns->clear();
  if (iEvent.getByLabel("addPileupInfo",puInfos)) {
     for(unsigned int i=0; i<puInfos->size(); i++) {
        PUNtuple_->npus->push_back((*puInfos)[i].getPU_NumInteractions());
        PUNtuple_->tnpus->push_back((*puInfos)[i].getTrueNumInteractions());
        PUNtuple_->bxns->push_back((*puInfos)[i].getBunchCrossing());
     }
  }

  // REFERENCES & RECOJETS
  iEvent.getByLabel(srcJet_, jets);
  
  //loop over the jets and fill the ntuple
  size_t nJet=(nJetMax_==0) ? jets->size() : std::min(nJetMax_,(unsigned int)jets->size());
  PUNtuple_->nref=nJet;
  for (size_t iJet=0;iJet<nJet;iJet++) {

     //cout << "Doing jet " << iJet << endl;

     pat::Jet jet = jets->at(iJet);
     const reco::GenJet* ref = jet.genJet();

     //Remove jets which are unmatched with a generator level jet
     if(!ref) {
      PUNtuple_->nref--;
      continue;
     }

     jesUncScale = 1.0;
      if (doJESUncertainty_) {
         if (JESUncertainty_ == "none") {
            jesUncScale *= 1.0;
         }
         else {
            jecUnc->setJetEta(jet.eta());
            jecUnc->setJetPt(jet.pt());

            uncert = jecUnc->getUncertainty(true);

            if (JESUncertainty_ == "up") {
               jesUncScale *= (1 + uncert);
            }
            else if (JESUncertainty_ == "down") {
               jesUncScale *= (1 - uncert);
            }
         }
      }

     JERCor = 1.0;
     if (doJER_) {
        // get the JER correction factor for this jet
        (ref && jet.pt()>10)? JERCor = getJERfactor(jet.pt(), jet.eta(), ref->pt()) : JERCor = 1.0;
        //Remember to propogate the corrections to the MET if you care about MET
      }

      jet.scaleEnergy(jesUncScale);
      jet.scaleEnergy(JERCor);

     if(ref) {
       PUNtuple_->refdrjt[nref_]  =reco::deltaR(jet.eta(),jet.phi(),ref->eta(),ref->phi());
       if (PUNtuple_->refdrjt[nref_]>deltaRMax_) continue;
     }
     else {
       PUNtuple_->refdrjt[nref_] = 0;
     }
     
     PUNtuple_->refrank[nref_]=nref_;
     PUNtuple_->refpdgid_algorithmicDef[nref_] = 0;
     PUNtuple_->refpdgid_physicsDef[nref_] = 0;
     if(ref) { 
        PUNtuple_->refpdgid[nref_] = ref->pdgId();
        PUNtuple_->refe[nref_]     = ref->energy();
        PUNtuple_->refpt[nref_]    = ref->pt();
        PUNtuple_->refeta[nref_]   = ref->eta();
        PUNtuple_->refphi[nref_]   = ref->phi();
        PUNtuple_->refy[nref_]     = ref->rapidity();
        PUNtuple_->refarea[nref_]  = ref->jetArea();
     }
     else {
        PUNtuple_->refpdgid[nref_] = 0;
        PUNtuple_->refe[nref_]     = 0;
        PUNtuple_->refpt[nref_]    = 0;
        PUNtuple_->refeta[nref_]   = 0;
        PUNtuple_->refphi[nref_]   = 0;
        PUNtuple_->refy[nref_]     = 0;
        PUNtuple_->refarea[nref_]  = 0;      
     }

     //Options are:
     //Uncorrected = 0
     //L1FastJet = 1
     //L2Relative = 2
     //L3Absolute = 3
     try {
       PUNtuple_->jtjec[nref_]=1.0/jet.jecFactor(0);
     }
     catch(int e) {
      PUNtuple_->jtjec[nref_]=1.0;
     }

     PUNtuple_->jte[nref_]    =jet.energy()*PUNtuple_->jtjec[nref_];
     PUNtuple_->jtpt[nref_]   =jet.pt()*PUNtuple_->jtjec[nref_];
     PUNtuple_->jteta[nref_]  =jet.eta()*PUNtuple_->jtjec[nref_];
     PUNtuple_->jtphi[nref_]  =jet.phi()*PUNtuple_->jtjec[nref_];
     PUNtuple_->jty[nref_]    =jet.rapidity();
     PUNtuple_->jtarea[nref_] =jet.jetArea();
     
     if (doComposition_) {        
        PUNtuple_->jtchf[nref_] =jet.chargedHadronEnergyFraction()*PUNtuple_->jtjec[nref_];
        PUNtuple_->jtnhf[nref_] =jet.neutralHadronEnergyFraction()*PUNtuple_->jtjec[nref_];
        PUNtuple_->jtnef[nref_] =jet.photonEnergyFraction()*PUNtuple_->jtjec[nref_];
        PUNtuple_->jtcef[nref_] =jet.electronEnergyFraction()*PUNtuple_->jtjec[nref_];
        PUNtuple_->jtmuf[nref_] =jet.muonEnergyFraction()*PUNtuple_->jtjec[nref_];
        PUNtuple_->jthfhf[nref_]=jet.HFHadronEnergyFraction()*PUNtuple_->jtjec[nref_];
        PUNtuple_->jthfef[nref_]=jet.HFEMEnergyFraction()*PUNtuple_->jtjec[nref_];
    }

     nref_++;
  }
  
  tree_->Fill();
  
  return;
}

////////////////////////////////////////////////////////////////////////////////
// implement additional functions
////////////////////////////////////////////////////////////////////////////////

//______________________________________________________________________________
double treeMaker::getJERfactor(double pt, double eta, double ptgen){

  double jer = 1;

  if(JERUncertainty_ == "none") {
    if (fabs(eta) < 0.5)
      jer = 1.079;
    else if (fabs(eta) < 1.1)
      jer = 1.099;
    else if (fabs(eta) < 1.7)
      jer = 1.121;
    else if (fabs(eta) < 2.3)
      jer = 1.208;
    else if (fabs(eta) < 2.8)
      jer = 1.253;
    else if (fabs(eta) < 3.2)
      jer = 1.395;
    else if (fabs(eta) < 5.0)
      jer = 1.056;
  }
  else if(JERUncertainty_ == "up") {
    if (fabs(eta) < 0.5)
      jer = 1.105;
    else if (fabs(eta) < 1.1)
      jer = 1.127;
    else if (fabs(eta) < 1.7)
      jer = 1.150;
    else if (fabs(eta) < 2.3)
      jer = 1.254;
    else if (fabs(eta) < 2.8)
      jer = 1.316;
    else if (fabs(eta) < 3.2)
      jer = 1.458;
    else if (fabs(eta) < 5.0)
      jer = 1.247;
  }
  else if(JERUncertainty_ == "down") {
    if (fabs(eta) < 0.5)
      jer = 1.053;
    else if (fabs(eta) < 1.1)
      jer = 1.071;
    else if (fabs(eta) < 1.7)
      jer = 1.092;
    else if (fabs(eta) < 2.3)
      jer = 1.162;
    else if (fabs(eta) < 2.8)
      jer = 1.192;
    else if (fabs(eta) < 3.2)
      jer = 1.332;
    else if (fabs(eta) < 5.0)
      jer = 0.865;
  }
  else {
    cout << "ERROR::treeMaker::getJERfactor Unrecognized JERUncertainty_ value." << endl;
    return 1.0;
  }
  double corr = ptgen / pt;

  return  max(0.0,corr + jer * (1 - corr));

}

////////////////////////////////////////////////////////////////////////////////
// define treeMaker as a plugin
////////////////////////////////////////////////////////////////////////////////

DEFINE_FWK_MODULE(treeMaker);
