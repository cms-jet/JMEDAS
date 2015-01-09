////////////////////////////////////////////////////////////////////////////////
//
// pileupTreeMaker
// ---------------
//
//                        01/07/2014 Alexx Perloff   <aperloff@physics.tamu.edu>
////////////////////////////////////////////////////////////////////////////////

#include "Analysis/JMEDAS/interface/jmedas_pileupNtuple.h"

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

class pileupTreeMaker : public edm::EDAnalyzer
{
public:
  // construction/destruction
  explicit pileupTreeMaker(const edm::ParameterSet& iConfig);
  virtual ~pileupTreeMaker();

private:
  // member functions
  void beginJob();
  void analyze(const edm::Event& iEvent,const edm::EventSetup& iSetup);
  void endJob(){;}

private:
  // member data
  std::string   moduleLabel_;
  std::string   JetCorLabel_;
  std::vector<std::string> JetCorLevels_;

  edm::InputTag srcJet_;
  edm::InputTag srcRho_;
  edm::InputTag srcVtx_;
  edm::InputTag srcMuons_;
  edm::InputTag srcVMCHSTAND_;
  edm::InputTag srcVMNHSTAND_;
  edm::InputTag srcVMPhSTAND_;
  edm::InputTag srcVMPUSTAND_;
  edm::InputTag srcVMNHPFWGT_;
  edm::InputTag srcVMPhPFWGT_;
  edm::InputTag srcVMCHPUPPI_;
  edm::InputTag srcVMNHPUPPI_;
  edm::InputTag srcVMPhPUPPI_;

  bool          doComposition_;
  bool          doFlavor_;
  unsigned int  nJetMax_;
  double        deltaRMax_;
  double        deltaPhiMin_;
  double        deltaRPartonMax_;
  int           nref_;
  FactorizedJetCorrector* jetCorrector_;
  
  // tree
  TTree*        tree_;
  pileupNtuple* PUNtuple_;
};


////////////////////////////////////////////////////////////////////////////////
// construction/destruction
////////////////////////////////////////////////////////////////////////////////

//______________________________________________________________________________
pileupTreeMaker::pileupTreeMaker(const edm::ParameterSet& iConfig)
  : moduleLabel_   (iConfig.getParameter<std::string>            ("@module_label"))
  , JetCorLabel_   (iConfig.getParameter<std::string>              ("JetCorLabel"))
  , JetCorLevels_  (iConfig.getParameter<vector<string> >         ("JetCorLevels"))
  , srcJet_        (iConfig.getParameter<edm::InputTag>                 ("srcJet"))
  , srcRho_        (iConfig.getParameter<edm::InputTag>                 ("srcRho"))
  , srcVtx_        (iConfig.getParameter<edm::InputTag>                 ("srcVtx"))
  , srcMuons_      (iConfig.getParameter<edm::InputTag>               ("srcMuons"))
  , srcVMCHSTAND_  (iConfig.getParameter<edm::InputTag>           ("srcVMCHSTAND"))
  , srcVMNHSTAND_  (iConfig.getParameter<edm::InputTag>           ("srcVMNHSTAND"))
  , srcVMPhSTAND_  (iConfig.getParameter<edm::InputTag>           ("srcVMPhSTAND"))
  , srcVMPUSTAND_  (iConfig.getParameter<edm::InputTag>           ("srcVMPUSTAND"))
  , srcVMNHPFWGT_  (iConfig.getParameter<edm::InputTag>           ("srcVMNHPFWGT"))
  , srcVMPhPFWGT_  (iConfig.getParameter<edm::InputTag>           ("srcVMPhPFWGT"))
  , srcVMCHPUPPI_  (iConfig.getParameter<edm::InputTag>           ("srcVMCHPUPPI"))
  , srcVMNHPUPPI_  (iConfig.getParameter<edm::InputTag>           ("srcVMNHPUPPI"))
  , srcVMPhPUPPI_  (iConfig.getParameter<edm::InputTag>           ("srcVMPhPUPPI"))
  , doComposition_ (iConfig.getParameter<bool>                   ("doComposition"))
  , doFlavor_      (iConfig.getParameter<bool>                        ("doFlavor"))
  , nJetMax_       (iConfig.getParameter<unsigned int>                 ("nJetMax"))
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

  // Jet CORRECTOR
  if(!JetCorLevels_.empty()) {
    vector<JetCorrectorParameters> vPar;
    string jetCorPar = "PHYS14_V2_MC_L1FastJet_"+JetCorLabel_.substr(0,JetCorLabel_.size()-2)+".txt";
    cout << "Getting JEC from file " << jetCorPar  << " ... ";
    vPar.push_back(JetCorrectorParameters(jetCorPar));
    jetCorrector_ = new FactorizedJetCorrector(vPar);
    cout << "DONE" << endl;
  }
  
}


//______________________________________________________________________________
pileupTreeMaker::~pileupTreeMaker()
{

}


////////////////////////////////////////////////////////////////////////////////
// implementation of member functions
////////////////////////////////////////////////////////////////////////////////

//______________________________________________________________________________
void pileupTreeMaker::beginJob()
{
  edm::Service<TFileService> fs;
  if (!fs) throw edm::Exception(edm::errors::Configuration,
				"TFileService missing from configuration!");
  
  tree_=fs->make<TTree>("t","t");
  PUNtuple_ = new pileupNtuple(tree_,true);

}


//______________________________________________________________________________
void pileupTreeMaker::analyze(const edm::Event& iEvent,
                                  const edm::EventSetup& iSetup)
{
  // EVENT DATA HANDLES
  nref_=0;
  edm::Handle<GenEventInfoProduct>               genInfo;
  edm::Handle<vector<PileupSummaryInfo> >        puInfos;  
  edm::Handle<reco::CandidateView>               refs;
  edm::Handle<std::vector<pat::Jet> >            jets;
  edm::Handle<double>                            rho;
  edm::Handle<std::vector<reco::Vertex> >        vtx;
  edm::Handle<edm::View<pat::Muon> >             muons;
  edm::Handle<edm::ValueMap<double> >            VMCHSTAND;
  edm::Handle<edm::ValueMap<double> >            VMNHSTAND;
  edm::Handle<edm::ValueMap<double> >            VMPhSTAND;
  edm::Handle<edm::ValueMap<double> >            VMPUSTAND;
  edm::Handle<edm::ValueMap<double> >            VMNHPFWGT;
  edm::Handle<edm::ValueMap<double> >            VMPhPFWGT;
  edm::Handle<edm::ValueMap<double> >            VMCHPUPPI;
  edm::Handle<edm::ValueMap<double> >            VMNHPUPPI;
  edm::Handle<edm::ValueMap<double> >            VMPhPUPPI;

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

     if(ref) {
       PUNtuple_->refdrjt[nref_]  =reco::deltaR(jet.eta(),jet.phi(),ref->eta(),ref->phi());
       if (PUNtuple_->refdrjt[nref_]>deltaRMax_) continue;
     }
     else {
       PUNtuple_->refdrjt[nref_] = 0;
     }
     
     // Beta/Beta Star Calculation
     PUNtuple_->beta = 0.0;
     PUNtuple_->betaStar = 0.0;
     //---- vertex association -----------
     //---- get the vector of tracks -----
     reco::TrackRefVector vTrks(jet.associatedTracks());
     float sumTrkPt(0.0),sumTrkPtBeta(0.0),sumTrkPtBetaStar(0.0);
     //---- loop over the tracks of the jet ----
     for(reco::TrackRefVector::const_iterator i_trk = vTrks.begin(); i_trk != vTrks.end(); i_trk++) {
        //if (npv_ == 0) break;
        if ((*vtx).size() == 0) break;
        sumTrkPt += (*i_trk)->pt();
        //---- loop over all vertices ----------------------------
        for(unsigned ivtx = 0;ivtx < (*vtx).size();ivtx++) {
           //---- loop over the tracks associated with the vertex ---
           if (!((*vtx)[ivtx].isFake()) && (*vtx)[ivtx].ndof() >= 4 && fabs((*vtx)[ivtx].z()) <= 24) {
              for(reco::Vertex::trackRef_iterator i_vtxTrk = (*vtx)[ivtx].tracks_begin(); i_vtxTrk != (*vtx)[ivtx].tracks_end(); ++i_vtxTrk) {
                 //---- match the jet track to the track from the vertex ----
                 reco::TrackRef trkRef(i_vtxTrk->castTo<reco::TrackRef>());
                 //---- check if the tracks match -------------------------
                 if (trkRef == (*i_trk)) {
                    if (ivtx == 0) {
                       sumTrkPtBeta += (*i_trk)->pt();
                    }
                    else {
                       sumTrkPtBetaStar += (*i_trk)->pt();
                    }   
                    break;
                 }
              }
           } 
        }
     }
     if (sumTrkPt > 0) {
        PUNtuple_->beta     = sumTrkPtBeta/sumTrkPt;
        PUNtuple_->betaStar = sumTrkPtBetaStar/sumTrkPt;
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

     if (0!=jetCorrector_) {
        jetCorrector_->setJetEta(jet.eta());
        jetCorrector_->setJetPt(jet.pt());
        jetCorrector_->setJetE(jet.energy());
        jetCorrector_->setJetA(jet.jetArea());
        jetCorrector_->setRho(PUNtuple_->rho);
        jetCorrector_->setNPV(PUNtuple_->npv);
        PUNtuple_->jtjec[nref_]=jetCorrector_->getCorrection();
     }
     else {
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
  

  // MUON SECTION
  iEvent.getByLabel(srcMuons_, muons);
  iEvent.getByLabel(srcVMCHSTAND_, VMCHSTAND);
  iEvent.getByLabel(srcVMNHSTAND_, VMNHSTAND);
  iEvent.getByLabel(srcVMPhSTAND_, VMPhSTAND);
  iEvent.getByLabel(srcVMPUSTAND_, VMPUSTAND);
  iEvent.getByLabel(srcVMNHPFWGT_, VMNHPFWGT);
  iEvent.getByLabel(srcVMPhPFWGT_, VMPhPFWGT);
  iEvent.getByLabel(srcVMCHPUPPI_, VMCHPUPPI);
  iEvent.getByLabel(srcVMNHPUPPI_, VMNHPUPPI);
  iEvent.getByLabel(srcVMPhPUPPI_, VMPhPUPPI);

  PUNtuple_->nmu = muons->size();
  //for(auto iMuon = muons->begin(); iMuon!=muons->end(); ++iMuon) {
  for(size_t i = 0, n = muons->size(); i < n; ++i) {
    edm::Ptr<pat::Muon> muPtr = muons->ptrAt(i);
    PUNtuple_->mupt[i]  = muPtr->pt();
    PUNtuple_->mueta[i] = muPtr->eta();
    PUNtuple_->muphi[i] = muPtr->phi();
    PUNtuple_->mue[i]   = muPtr->energy();

    //Delta Beta (see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Muon_Isolation for more details)
    //I = [sumChargedHadronPt+ max(0.,sumNeutralHadronPt+sumPhotonPt-0.5sumPUPt]/pt
    PUNtuple_->muIsoSTAND[i] = ((*VMCHSTAND)[muPtr] + max(0.0,(*VMNHSTAND)[muPtr]+(*VMPhSTAND)[muPtr]-(0.5*(*VMPUSTAND)[muPtr])))/muPtr->pt();
    
    // PF Weighted (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonIsolationForRun2 for more details)
    PUNtuple_->muIsoPFWGT[i] = ((*VMCHSTAND)[muPtr]+(*VMNHPFWGT)[muPtr]+(*VMPhPFWGT)[muPtr])/muPtr->pt();
    
    // PUPPI Weighted (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonIsolationForRun2 for more details)
    PUNtuple_->muIsoPUPPI[i] = ((*VMCHPUPPI)[muPtr]+(*VMNHPUPPI)[muPtr]+(*VMPhPUPPI)[muPtr])/muPtr->pt();;
  }

  tree_->Fill();
  
  return;
}


////////////////////////////////////////////////////////////////////////////////
// define pileupTreeMaker as a plugin
////////////////////////////////////////////////////////////////////////////////

DEFINE_FWK_MODULE(pileupTreeMaker);
