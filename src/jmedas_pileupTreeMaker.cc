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
#include "FWCore/Framework/interface/EventSetup.h"
 
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
#include "JetMETCorrections/Objects/interface/JetCorrectionsRecord.h"
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
#include <utility>

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

  edm::InputTag srcJet_;
  edm::InputTag srcRho_;
  edm::InputTag srcVtx_;
  edm::InputTag srcMuons_;
  edm::InputTag srcMET_;
  edm::InputTag srcMETNoHF_;
  edm::InputTag srcPuppiMET_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_Combined_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_Combined_CH_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_Combined_NH_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_Combined_PH_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_WithLep_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_WithLep_CH_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_WithLep_NH_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_WithLep_PH_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_WithoutLep_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_WithoutLep_CH_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_WithoutLep_NH_;
  edm::EDGetTokenT< edm::ValueMap<double> > srcPuppuMuIso_WithoutLep_PH_;

  bool          doComposition_;
  bool          doFlavor_;
  unsigned int  nJetMax_;
  double        deltaRMax_;
  double        deltaPhiMin_;
  double        deltaRPartonMax_;
  int           nref_;
  
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
  , srcJet_        (iConfig.getParameter<edm::InputTag>                 ("srcJet"))
  , srcRho_        (iConfig.getParameter<edm::InputTag>                 ("srcRho"))
  , srcVtx_        (iConfig.getParameter<edm::InputTag>                 ("srcVtx"))
  , doComposition_ (iConfig.getParameter<bool>                   ("doComposition"))
  , doFlavor_      (iConfig.getParameter<bool>                        ("doFlavor"))
  , nJetMax_       (iConfig.getParameter<unsigned int>                 ("nJetMax"))
  , deltaRMax_(0.0)
  , deltaPhiMin_(3.141)
  , deltaRPartonMax_(0.0)
{

   if(iConfig.exists("srcMuons")) {
      srcMuons_     = iConfig.getParameter<edm::InputTag>    ("srcMuons");
      srcPuppuMuIso_Combined_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_Combined"));
      srcPuppuMuIso_Combined_CH_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_Combined_CH"));
      srcPuppuMuIso_Combined_NH_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_Combined_NH"));
      srcPuppuMuIso_Combined_PH_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_Combined_PH"));
      srcPuppuMuIso_WithLep_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_WithLep"));
      srcPuppuMuIso_WithLep_CH_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_WithLep_CH"));
      srcPuppuMuIso_WithLep_NH_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_WithLep_NH"));
      srcPuppuMuIso_WithLep_PH_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_WithLep_PH"));
      srcPuppuMuIso_WithoutLep_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_WithoutLep"));
      srcPuppuMuIso_WithoutLep_CH_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_WithoutLep_CH"));
      srcPuppuMuIso_WithoutLep_NH_ = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_WithoutLep_NH"));
      srcPuppuMuIso_WithoutLep_PH_  = consumes< edm::ValueMap<double> >(iConfig.getParameter<edm::InputTag>("srcPuppuMuIso_WithoutLep_PH"));
   }
   if(iConfig.exists("srcMET")) {
      srcMET_ = iConfig.getParameter<edm::InputTag>("srcMET");
   }
   if(iConfig.exists("srcMETNoHF")) {
      srcMETNoHF_ = iConfig.getParameter<edm::InputTag>("srcMETNoHF");
   }
   if(iConfig.exists("srcMET")) {
      srcPuppiMET_ = iConfig.getParameter<edm::InputTag>("srcPuppiMET");
   }

  if (iConfig.exists("deltaRMax")) {
    deltaRMax_ = iConfig.getParameter<double>("deltaRMax");
  }
  else
    throw cms::Exception("MissingParameter")<<"Set *either* deltaRMax (matching)"
					    <<" *or* deltaPhiMin (balancing)";
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
  edm::Handle<edm::ValueMap<double> >            iso_PuppiCombined;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiCombined_CH;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiCombined_NH;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiCombined_PH;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiWithLep;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiWithLep_CH;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiWithLep_NH;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiWithLep_PH;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiWithoutLep;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiWithoutLep_CH;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiWithoutLep_NH;
  edm::Handle<edm::ValueMap<double> >            iso_PuppiWithoutLep_PH;
  edm::Handle<edm::View<pat::MET> >              met;
  edm::Handle<edm::View<pat::MET> >              met_nohf;
  edm::Handle<edm::View<pat::MET> >              puppi_met;

  // CLEAR THE NTUPLE
  PUNtuple_->clear();

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
  if (iEvent.getByLabel("slimmedAddPileupInfo",puInfos)) {
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
  for (size_t iJet=0;iJet<nJet;iJet++) {
     //cout << "Doing jet " << iJet << endl;

     pat::Jet jet = jets->at(iJet);
     const reco::GenJet* ref = jet.genJet();

     if(ref) {
       PUNtuple_->refdrjt->push_back(reco::deltaR(jet.eta(),jet.phi(),ref->eta(),ref->phi()));
       if (PUNtuple_->refdrjt->back()>deltaRMax_) continue;
     }
     else {
       PUNtuple_->refdrjt->push_back(0);
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

     //PUNtuple_->refrank[nref_]=nref_;
     PUNtuple_->refpdgid_algorithmicDef->push_back(0);
     PUNtuple_->refpdgid_physicsDef->push_back(0);
     if(ref) { 
        PUNtuple_->refpdgid->push_back(ref->pdgId());
        PUNtuple_->refe->push_back(ref->energy());
        PUNtuple_->refpt->push_back(ref->pt());
        PUNtuple_->refeta->push_back(ref->eta());
        PUNtuple_->refphi->push_back(ref->phi());
        PUNtuple_->refy->push_back(ref->rapidity());
        PUNtuple_->refarea->push_back(ref->jetArea());
     }
     else {
        PUNtuple_->refpdgid->push_back(0);
        PUNtuple_->refe->push_back(0);
        PUNtuple_->refpt->push_back(0);
        PUNtuple_->refeta->push_back(0);
        PUNtuple_->refphi->push_back(0);
        PUNtuple_->refy->push_back(0);
        PUNtuple_->refarea->push_back(0);      
     }

     //for(unsigned int ijec = 0; ijec<jet.availableJECLevels().size(); ijec++) {
     //   cout << jet.availableJECLevels()[ijec] << endl;
     //}
     //cout << jet.currentJECLevel() << endl;
     //cout << jet.currentJECSet() << endl;
     try {
        vector<pair<string,float> > jec;
        //cout << "New jet" << endl;
        for(unsigned int ijec = 0; ijec<jet.availableJECLevels().size(); ijec++) {
          jec.push_back(make_pair(jet.availableJECLevels()[ijec],jet.jecFactor(jet.availableJECLevels()[ijec])));
          //cout << "JEC level: " << jet.availableJECLevels()[ijec] << "\tJEC Factor: " << jet.jecFactor(jet.availableJECLevels()[ijec]) << endl;
        }
        PUNtuple_->jtjec->push_back(jec);
     } catch(cms::Exception& e) {
        cout << e.what() << endl;
        //PUNtuple_->jtjec->push_back(vector<pair<string,float> >(jet.availableJECLevels().size(),make_pair("Unknown",1.0)));
        PUNtuple_->jtjec->push_back(JECInfo(jet.availableJECLevels().size(),make_pair("Unknown",1.0)));
     }

     PUNtuple_->jte->push_back(jet.energy());
     PUNtuple_->jtpt->push_back(jet.pt());
     PUNtuple_->jteta->push_back(jet.eta());
     PUNtuple_->jtphi->push_back(jet.phi());
     PUNtuple_->jty->push_back(jet.rapidity());
     PUNtuple_->jtarea->push_back(jet.jetArea());
     
     if (doComposition_) {
        PUNtuple_->jtchf->push_back(jet.chargedHadronEnergyFraction());
        PUNtuple_->jtnhf->push_back(jet.neutralHadronEnergyFraction());
        PUNtuple_->jtnef->push_back(jet.photonEnergyFraction());
        PUNtuple_->jtcef->push_back(jet.electronEnergyFraction());
        PUNtuple_->jtmuf->push_back(jet.muonEnergyFraction());
        PUNtuple_->jthfhf->push_back(jet.HFHadronEnergyFraction());
        PUNtuple_->jthfef->push_back(jet.HFEMEnergyFraction());
    }

     nref_++;
  }
  

  // MUON SECTION
  if(srcMuons_.label()!="") {
     iEvent.getByLabel(srcMuons_, muons);
     iEvent.getByToken(srcPuppuMuIso_Combined_, iso_PuppiCombined);
     iEvent.getByToken(srcPuppuMuIso_Combined_CH_, iso_PuppiCombined_CH);
     iEvent.getByToken(srcPuppuMuIso_Combined_NH_, iso_PuppiCombined_NH);
     iEvent.getByToken(srcPuppuMuIso_Combined_PH_, iso_PuppiCombined_PH);
     iEvent.getByToken(srcPuppuMuIso_WithLep_, iso_PuppiWithLep);
     iEvent.getByToken(srcPuppuMuIso_WithLep_CH_, iso_PuppiWithLep_CH);
     iEvent.getByToken(srcPuppuMuIso_WithLep_NH_, iso_PuppiWithLep_NH);
     iEvent.getByToken(srcPuppuMuIso_WithLep_PH_, iso_PuppiWithLep_PH);
     iEvent.getByToken(srcPuppuMuIso_WithoutLep_, iso_PuppiWithoutLep);
     iEvent.getByToken(srcPuppuMuIso_WithoutLep_CH_, iso_PuppiWithoutLep_CH);
     iEvent.getByToken(srcPuppuMuIso_WithoutLep_NH_, iso_PuppiWithoutLep_NH);
     iEvent.getByToken(srcPuppuMuIso_WithoutLep_PH_, iso_PuppiWithoutLep_PH);
     
     for(size_t i = 0, n = muons->size(); i < n; ++i) {
        edm::Ptr<pat::Muon> muPtr = muons->ptrAt(i);
        PUNtuple_->mupt->push_back(muPtr->pt());
        PUNtuple_->mueta->push_back(muPtr->eta());
        PUNtuple_->muphi->push_back(muPtr->phi());
        PUNtuple_->mue->push_back(muPtr->energy());
        PUNtuple_->muIso_PuppiCombined->push_back((* iso_PuppiCombined ) [ muPtr ]);
        PUNtuple_->muIso_PuppiCombined_CH->push_back((* iso_PuppiCombined_CH ) [ muPtr ]);
        PUNtuple_->muIso_PuppiCombined_NH->push_back((* iso_PuppiCombined_NH ) [ muPtr ]);
        PUNtuple_->muIso_PuppiCombined_PH->push_back((* iso_PuppiCombined_PH ) [ muPtr ]);
        PUNtuple_->muIso_PuppiWithLep->push_back((* iso_PuppiWithLep ) [ muPtr ]);
        PUNtuple_->muIso_PuppiWithLep_CH->push_back((* iso_PuppiWithLep_CH ) [ muPtr ]);
        PUNtuple_->muIso_PuppiWithLep_NH->push_back((* iso_PuppiWithLep_NH ) [ muPtr ]);
        PUNtuple_->muIso_PuppiWithLep_PH->push_back((* iso_PuppiWithLep_PH ) [ muPtr ]);
        PUNtuple_->muIso_PuppiWithoutLep->push_back((* iso_PuppiWithoutLep ) [ muPtr ]);
        PUNtuple_->muIso_PuppiWithoutLep_CH->push_back((* iso_PuppiWithoutLep_CH ) [ muPtr ]);
        PUNtuple_->muIso_PuppiWithoutLep_NH->push_back((* iso_PuppiWithoutLep_NH ) [ muPtr ]);
        PUNtuple_->muIso_PuppiWithoutLep_PH->push_back((* iso_PuppiWithoutLep_PH ) [ muPtr ]);

        //Raw Isolation
        //I = [sumChargedHadronPt+ max(0.,sumNeutralHadronPt+sumPhotonPt]/pt
        //Delta Beta (see https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideMuonId#Muon_Isolation for more details)
        //I = [sumChargedHadronPt+ max(0.,sumNeutralHadronPt+sumPhotonPt-0.5sumPUPt]/pt
        //PF Weighted (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonIsolationForRun2 for more details)
        //PUPPI Weighted (see https://twiki.cern.ch/twiki/bin/viewauth/CMS/MuonIsolationForRun2 for more details)
     }
  }

  // MET SECTION
  if(srcMET_.label()!="") {
     iEvent.getByLabel(srcMET_, met);
     for(size_t i = 0, n = met->size(); i < n; ++i) {
        edm::Ptr<pat::MET> metPtr = met->ptrAt(i);
        PUNtuple_->metpt->push_back(metPtr->pt());
        PUNtuple_->meteta->push_back(metPtr->eta());
        PUNtuple_->metphi->push_back(metPtr->phi());
        PUNtuple_->mete->push_back(metPtr->energy());
     }
  }
  if(srcMETNoHF_.label()!="") {
     iEvent.getByLabel(srcMETNoHF_, met_nohf);
     for(size_t i = 0, n = met_nohf->size(); i < n; ++i) {
        edm::Ptr<pat::MET> metPtr = met_nohf->ptrAt(i);
        PUNtuple_->metNoHFpt->push_back(metPtr->pt());
        PUNtuple_->metNoHFeta->push_back(metPtr->eta());
        PUNtuple_->metNoHFphi->push_back(metPtr->phi());
        PUNtuple_->metNoHFe->push_back(metPtr->energy());
     }
  }
  if(srcMET_.label()!="") {
     iEvent.getByLabel(srcPuppiMET_, puppi_met);
     for(size_t i = 0, n = puppi_met->size(); i < n; ++i) {
        edm::Ptr<pat::MET> metPtr = puppi_met->ptrAt(i);
        PUNtuple_->metPUPPIpt->push_back(metPtr->pt());
        PUNtuple_->metPUPPIeta->push_back(metPtr->eta());
        PUNtuple_->metPUPPIphi->push_back(metPtr->phi());
        PUNtuple_->metPUPPIe->push_back(metPtr->energy());
     }
  }

  tree_->Fill();
  
  return;
}


////////////////////////////////////////////////////////////////////////////////
// define pileupTreeMaker as a plugin
////////////////////////////////////////////////////////////////////////////////

DEFINE_FWK_MODULE(pileupTreeMaker);
