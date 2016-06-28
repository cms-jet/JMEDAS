// -*- C++ -*-
//
// Package:    Analysis/JetMiniValidation
// Class:      JetMiniValidation
// 
/**\class JetMiniValidation JetMiniValidation.cc Analysis/JetMiniValidation/plugins/JetMiniValidation.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  James Dolen
//         Created:  Sat, 30 Apr 2016 17:40:42 GMT
//
//

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

// DataFormats
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "DataFormats/JetReco/interface/PFJetCollection.h"

// TFile
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

// Gen particle
#include "DataFormats/PatCandidates/interface/PackedGenParticle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

// JEC
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

// root
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"
#include "TLorentzVector.h"
//
// class declaration
//

class JetMiniValidation : public edm::one::EDAnalyzer<edm::one::SharedResources>  {
   public:
      explicit JetMiniValidation(const edm::ParameterSet&);
      ~JetMiniValidation();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      // ----------member data ---------------------------
      edm::EDGetTokenT<pat::JetCollection> ak4jetToken_;
      edm::EDGetTokenT<pat::JetCollection> ak8jetToken_;
      edm::EDGetTokenT<pat::JetCollection> puppijetToken_;
      edm::EDGetTokenT<reco::GenJetCollection> ak4genjetToken_;
      edm::EDGetTokenT<reco::GenJetCollection> ak8genjetToken_;
      edm::EDGetTokenT<edm::View<reco::GenParticle> > prunedGenToken_;
      edm::EDGetTokenT<double> rhoToken_;
      edm::EDGetTokenT<std::vector<reco::Vertex> > vtxToken_;

      std::vector<std::string>  jecPayloads_; /// files for JEC payloads
      boost::shared_ptr<FactorizedJetCorrector> jec_;


      TH1D * h_ak4chs_pt             ;  
      TH1D * h_ak4chs_eta            ;  
      TH1D * h_ak4chs_phi            ;  
      TH1D * h_ak4chs_ndau           ;  
      TH1D * h_ak4chs_puid           ;  
      TH1D * h_ak4chs_flavParton     ;
      TH1D * h_ak4chs_flavHadron     ;
      TH1D * h_ak4chs_dRminGen       ;
      TH1D * h_ak4chs_ptGen          ;
      TH1D * h_ak4chs_ptResponse     ;

      TH1D * h_ak8chs_pt             ;
      TH1D * h_ak8chs_mass           ;
      TH1D * h_ak8chs_rapidity       ;
      TH1D * h_ak8chs_prunedMass     ;
      TH1D * h_ak8chs_trimmedMass    ;
      TH1D * h_ak8chs_filteredMass   ;
      TH1D * h_ak8chs_softDropMass   ;
      TH1D * h_ak8chs_tau1           ;
      TH1D * h_ak8chs_tau2           ;
      TH1D * h_ak8chs_tau3           ;
      TH1D * h_ak8chs_tau32          ;
      TH1D * h_ak8chs_tau21          ;
      TH1D * h_ak8chs_ndau           ;
      TH1D * h_ak8chs_sdSubjetMass   ;

      TH1D * h_ak8puppi_pt           ; 
      TH1D * h_ak8puppi_mass         ; 
      TH1D * h_ak8puppi_softDropMass ; 
      TH1D * h_ak8puppi_tau1         ; 
      TH1D * h_ak8puppi_tau2         ; 
      TH1D * h_ak8puppi_tau3         ; 
      TH1D * h_ak8puppi_tau32        ; 
      TH1D * h_ak8puppi_tau21        ; 
      TH1D * h_ak8puppi_sdSubjetMass ;

      TH1D * h_deltaR_chs_puppi      ;

      TTree *  ak4JetTree;
      Float_t  ak4_pt_uncorr;
      Float_t  ak4_pt;
      Float_t  ak4_eta;
      Float_t  ak4_puid;
      Float_t  ak4_flavHadron;
      Float_t  ak4_flavParton;
      Float_t  ak4_ptGen;
      Float_t  ak4_ptResponse;
      Float_t  ak4_dRminGen;
      Float_t  ak4_area;
      Float_t  ak4_rho;
      Int_t    ak4_nvtx;


      TTree * ak8JetTree;
      Float_t ak8_pt                  ;
      Float_t ak8_mass                ;
      Float_t ak8_rapidity            ;
      Float_t ak8_prunedMass          ;
      Float_t ak8_sdMass              ;
      Float_t ak8_tau1                ;
      Float_t ak8_tau2                ;
      Float_t ak8_tau3                ;
      Float_t ak8_tau32               ;
      Float_t ak8_tau21               ;
      Float_t ak8_ndau                ;
      Float_t ak8_subjet_M            ;
      Float_t ak8_subjet_count        ;
      Float_t ak8_puppi_pt            ;
      Float_t ak8_puppi_mass          ;
      Float_t ak8_puppi_softDropMass  ;
      Float_t ak8_puppi_tau1          ;
      Float_t ak8_puppi_tau2          ;
      Float_t ak8_puppi_tau3          ;
      Float_t ak8_puppi_tau32         ;
      Float_t ak8_puppi_tau21         ;
      Float_t ak8_puppi_subjet_M      ;
      Float_t ak8_puppi_subjet_count  ;
      Float_t ak8_mGen                ;
      Float_t ak8_ptGen               ;
      Float_t ak8_ptResponse          ;
      Float_t ak8_dRminGen            ;
      Float_t ak8_area                ;
      Float_t ak8_rho                 ;
      Int_t   ak8_nvtx                ;

};

//
// constructors and destructor
//
JetMiniValidation::JetMiniValidation(const edm::ParameterSet& iConfig):
    ak4jetToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJets"))),
    ak8jetToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJetsAK8"))),
    puppijetToken_(consumes<pat::JetCollection>(edm::InputTag("slimmedJetsPuppi"))),
    ak4genjetToken_(consumes<reco::GenJetCollection>(edm::InputTag("slimmedGenJets"))),
    ak8genjetToken_(consumes<reco::GenJetCollection>(edm::InputTag("slimmedGenJetsAK8"))),
    prunedGenToken_(consumes<edm::View<reco::GenParticle> >(edm::InputTag("prunedGenParticles"))),
    rhoToken_(consumes<double>(edm::InputTag("fixedGridRhoFastjetAll"))),
    vtxToken_(consumes<std::vector<reco::Vertex> >(edm::InputTag("offlineSlimmedPrimaryVertices"))),
    jecPayloads_        (iConfig.getParameter<std::vector<std::string> >  ("jecPayloads"))
{
  usesResource("TFileService");
  edm::Service<TFileService> fs;

  h_ak4chs_pt             =  fs->make<TH1D>("h_ak4chs_pt"                ,"",100, 0,2000);
  h_ak4chs_eta            =  fs->make<TH1D>("h_ak4chs_eta"               ,"",100,-5,   5);
  h_ak4chs_phi            =  fs->make<TH1D>("h_ak4chs_phi"               ,"",100,-6,   6);
  h_ak4chs_ndau           =  fs->make<TH1D>("h_ak4chs_ndau"              ,"",100, 0, 100);
  h_ak4chs_puid           =  fs->make<TH1D>("h_ak4chs_puid"              ,"",100,-1,   1);
  h_ak4chs_flavParton     =  fs->make<TH1D>("h_ak4chs_flavParton"        ,"",60,-30,30);
  h_ak4chs_flavHadron     =  fs->make<TH1D>("h_ak4chs_flavHadron"        ,"",60,-30,30);
  h_ak4chs_dRminGen       =  fs->make<TH1D>("h_ak4chs_dRminGen"          ,"",100, 0,  0.6);
  h_ak4chs_ptGen          =  fs->make<TH1D>("h_ak4chs_ptGen"             ,"",100, 0,2000);
  h_ak4chs_ptResponse     =  fs->make<TH1D>("h_ak4chs_ptResponse"        ,"",100,-2,   2);

  h_ak8chs_pt             =  fs->make<TH1D>("h_ak8chs_pt"                ,"",100,0,3000);
  h_ak8chs_mass           =  fs->make<TH1D>("h_ak8chs_mass"              ,"",100,0,300);
  h_ak8chs_rapidity       =  fs->make<TH1D>("h_ak8chs_rapidity"          ,"",100,-5, 5);
  h_ak8chs_prunedMass     =  fs->make<TH1D>("h_ak8chs_prunedMass"        ,"",100,0,300);
  h_ak8chs_trimmedMass    =  fs->make<TH1D>("h_ak8chs_trimmedMass"       ,"",100,0,300);
  h_ak8chs_filteredMass   =  fs->make<TH1D>("h_ak8chs_filteredMass"      ,"",100,0,300);
  h_ak8chs_softDropMass   =  fs->make<TH1D>("h_ak8chs_softDropMass"      ,"",100,0,300);
  h_ak8chs_tau1           =  fs->make<TH1D>("h_ak8chs_tau1"              ,"",100,0,  1);
  h_ak8chs_tau2           =  fs->make<TH1D>("h_ak8chs_tau2"              ,"",100,0,  1);
  h_ak8chs_tau3           =  fs->make<TH1D>("h_ak8chs_tau3"              ,"",100,0,  1);
  h_ak8chs_tau32          =  fs->make<TH1D>("h_ak8chs_tau32"             ,"",100,0,  1);
  h_ak8chs_tau21          =  fs->make<TH1D>("h_ak8chs_tau21"             ,"",100,0,  1);
  h_ak8chs_ndau           =  fs->make<TH1D>("h_ak8chs_ndau"              ,"",100,0,300);
  h_ak8chs_sdSubjetMass   =  fs->make<TH1D>("h_ak8chs_sdSubjetMass"      ,"",100,0,100);

  h_ak8puppi_pt           =  fs->make<TH1D>("h_ak8puppi_pt"                ,"",100,0,3000);
  h_ak8puppi_mass         =  fs->make<TH1D>("h_ak8puppi_mass"              ,"",100,0,300);
  h_ak8puppi_softDropMass =  fs->make<TH1D>("h_ak8puppi_softDropMass"      ,"",100,0,300);
  h_ak8puppi_tau1         =  fs->make<TH1D>("h_ak8puppi_tau1"              ,"",100,0,  1);
  h_ak8puppi_tau2         =  fs->make<TH1D>("h_ak8puppi_tau2"              ,"",100,0,  1);
  h_ak8puppi_tau3         =  fs->make<TH1D>("h_ak8puppi_tau3"              ,"",100,0,  1);
  h_ak8puppi_tau32        =  fs->make<TH1D>("h_ak8puppi_tau32"             ,"",100,0,  1);
  h_ak8puppi_tau21        =  fs->make<TH1D>("h_ak8puppi_tau21"             ,"",100,0,  1);
  h_ak8puppi_sdSubjetMass =  fs->make<TH1D>("h_ak8puppi_sdSubjetMass"      ,"",100,0,100);

  h_deltaR_chs_puppi      =  fs->make<TH1D>("h_deltaR_chs_puppi"           ,"",100,0,0.8);


  ak4JetTree = new TTree("ak4JetTree","ak4JetTree");  
  ak4JetTree->Branch("ak4_pt_uncorr"        , & ak4_pt_uncorr      , "ak4_pt_uncorr/F"        );          
  ak4JetTree->Branch("ak4_pt"               , & ak4_pt             , "ak4_pt/F"               );          
  ak4JetTree->Branch("ak4_eta"              , & ak4_eta            , "ak4_eta/F"              );          
  ak4JetTree->Branch("ak4_puid"             , & ak4_puid           , "ak4_puid/F"             );          
  ak4JetTree->Branch("ak4_flavHadron"       , & ak4_flavHadron     , "ak4_flavHadron/F"       );          
  ak4JetTree->Branch("ak4_flavParton"       , & ak4_flavParton     , "ak4_flavParton/F"       );          
  ak4JetTree->Branch("ak4_ptGen"            , & ak4_ptGen          , "ak4_ptGen/F"            );          
  ak4JetTree->Branch("ak4_ptResponse"       , & ak4_ptResponse     , "ak4_ptResponse/F"       );          
  ak4JetTree->Branch("ak4_dRminGen"         , & ak4_dRminGen       , "ak4_dRminGen/F"         );          
  ak4JetTree->Branch("ak4_area"             , & ak4_area           , "ak4_area/F"             );          
  ak4JetTree->Branch("ak4_rho"              , & ak4_rho            , "ak4_rho/F"              );          
  ak4JetTree->Branch("ak4_nvtx"             , & ak4_nvtx           , "ak4_nvtx/I"             );          


  ak8JetTree = new TTree("ak8JetTree","ak8JetTree");  
  ak8JetTree->Branch("ak8_pt"                   , & ak8_pt                   , "ak8_pt/F"                 );          
  ak8JetTree->Branch("ak8_mass"                 , & ak8_mass                 , "ak8_mass/F"               );          
  ak8JetTree->Branch("ak8_rapidity"             , & ak8_rapidity             , "ak8_rapidity/F"           );          
  ak8JetTree->Branch("ak8_prunedMass"           , & ak8_prunedMass           , "ak8_prunedMass/F"         );          
  ak8JetTree->Branch("ak8_sdMass"               , & ak8_sdMass               , "ak8_sdMass/F"             );          
  ak8JetTree->Branch("ak8_tau1"                 , & ak8_tau1                 , "ak8_tau1/F"               );          
  ak8JetTree->Branch("ak8_tau2"                 , & ak8_tau2                 , "ak8_tau2/F"               );          
  ak8JetTree->Branch("ak8_tau3"                 , & ak8_tau3                 , "ak8_tau3/F"               );          
  ak8JetTree->Branch("ak8_tau32"                , & ak8_tau32                , "ak8_tau32/F"              );          
  ak8JetTree->Branch("ak8_tau21"                , & ak8_tau21                , "ak8_tau21/F"              );          
  ak8JetTree->Branch("ak8_ndau"                 , & ak8_ndau                 , "ak8_ndau/F"               );          
  ak8JetTree->Branch("ak8_subjet_M"             , & ak8_subjet_M             , "ak8_subjet_M/F"           );          
  ak8JetTree->Branch("ak8_subjet_count"         , & ak8_subjet_count         , "ak8_subjet_count/F"       );          
  ak8JetTree->Branch("ak8_puppi_pt"             , & ak8_puppi_pt             , "ak8_puppi_pt/F"           );          
  ak8JetTree->Branch("ak8_puppi_mass"           , & ak8_puppi_mass           , "ak8_puppi_mass/F"         );          
  ak8JetTree->Branch("ak8_puppi_softDropMass"   , & ak8_puppi_softDropMass   , "ak8_puppi_softDropMass/F" );          
  ak8JetTree->Branch("ak8_puppi_tau1"           , & ak8_puppi_tau1           , "ak8_puppi_tau1/F"         );          
  ak8JetTree->Branch("ak8_puppi_tau2"           , & ak8_puppi_tau2           , "ak8_puppi_tau2/F"         );          
  ak8JetTree->Branch("ak8_puppi_tau3"           , & ak8_puppi_tau3           , "ak8_puppi_tau3/F"         );          
  ak8JetTree->Branch("ak8_puppi_tau32"          , & ak8_puppi_tau32          , "ak8_puppi_tau32/F"        );          
  ak8JetTree->Branch("ak8_puppi_tau21"          , & ak8_puppi_tau21          , "ak8_puppi_tau21/F"        );          
  ak8JetTree->Branch("ak8_puppi_subjet_M"       , & ak8_puppi_subjet_M       , "ak8_puppi_subjet_M/F"     );          
  ak8JetTree->Branch("ak8_puppi_subjet_count"   , & ak8_puppi_subjet_count   , "ak8_puppi_subjet_count/F" );          
  ak8JetTree->Branch("ak8_area"                 , & ak8_area                 , "ak8_area/F"               );          
  ak8JetTree->Branch("ak8_rho"                  , & ak8_rho                  , "ak8_rho/F"                );          
  ak8JetTree->Branch("ak8_nvtx"                 , & ak8_nvtx                 , "ak8_nvtx/F"               );          

  ak8JetTree->Branch("ak8_mGen"                 , & ak8_mGen                 , "ak8_mGen/F"               );    
  ak8JetTree->Branch("ak8_ptGen"                , & ak8_ptGen                , "ak8_ptGen/F"              );    
  ak8JetTree->Branch("ak8_ptResponse"           , & ak8_ptResponse           , "ak8_ptResponse/F"         );    
  ak8JetTree->Branch("ak8_dRminGen"             , & ak8_dRminGen             , "ak8_dRminGen/F"           );    

 
}


JetMiniValidation::~JetMiniValidation()
{
}


//
// member functions
//

// ------------ method called for each event  ------------
void
JetMiniValidation::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  using namespace reco;
  using namespace pat;

  bool verbose = false;

  // Vertices
  edm::Handle<std::vector<reco::Vertex> > vertices;
  iEvent.getByToken(vtxToken_, vertices);
  int nvtx = vertices->size();

  // Rho
  Handle<double> rhoH;
  iEvent.getByToken(rhoToken_, rhoH);
  double rho = *rhoH;

  // AK4 jet loop from miniAOD
  
  edm::Handle<pat::JetCollection> AK4CHS;
  iEvent.getByToken(ak4jetToken_, AK4CHS);

  edm::Handle<reco::GenJetCollection> AK4GENJET;  
  iEvent.getByToken(ak4genjetToken_, AK4GENJET);
  

  for (const pat::Jet &ijet : *AK4CHS) {  
    double pt           = ijet.pt();
    double pt_uncorr    = ijet.pt()*ijet.jecFactor("Uncorrected");
    double eta          = ijet.eta();
    double phi          = ijet.phi();
    double ndau         = ijet.numberOfDaughters();
    double puid         = ijet.userFloat("pileupJetId:fullDiscriminant");

    // jet ID
    double NHF       = ijet.neutralHadronEnergyFraction();
    double NEMF      = ijet.neutralEmEnergyFraction();
    double CHF       = ijet.chargedHadronEnergyFraction();
    // double MUF       = ijet.muonEnergyFraction();
    double CEMF      = ijet.chargedEmEnergyFraction();
    // double NumConst  = ijet.chargedMultiplicity()+ijet.neutralMultiplicity();
    double NM        = ijet.neutralMultiplicity();
    double CM        = ijet.chargedMultiplicity(); 

    bool goodJet_looseJetID =  
      (fabs(eta) < 2.4 && CHF > 0.0 && NHF < 0.99 && CM > 0 && CEMF < 0.99 && NEMF < 0.99) 
      || ( fabs(eta) >= 2.4 && fabs(eta) < 3.0 && NEMF < 0.9 && NM > 2 ) 
      || ( fabs(eta) >= 3.0 && NEMF < 0.9 && NM > 10 );
    if (verbose) cout<<"goodJet = "<<goodJet_looseJetID<<endl;

    h_ak4chs_pt         ->Fill( pt         );
    h_ak4chs_eta        ->Fill( eta        );
    h_ak4chs_phi        ->Fill( phi        );
    h_ak4chs_ndau       ->Fill( ndau       );
    h_ak4chs_puid       ->Fill( puid       );

    if (!iEvent.isRealData()) {
      float dRmin = 100.;
      float ptGen = -1.0;
      for (const reco::GenJet &igen : *AK4GENJET) {  
        float dR = deltaR(ijet.eta(),ijet.phi(),igen.eta(),igen.phi());
        if (dR < dRmin) {
          dRmin = dR;
          ptGen = igen.pt();
        }
      }
      h_ak4chs_dRminGen         ->Fill( dRmin       );
      h_ak4chs_ptGen            ->Fill( ptGen       );
      if (ptGen>0) h_ak4chs_ptResponse       ->Fill( pt/ptGen );
      h_ak4chs_flavParton       ->Fill( ijet.partonFlavour()       );
      h_ak4chs_flavHadron       ->Fill( ijet.hadronFlavour()       );
      
      ak4_flavParton  =  ijet.partonFlavour()  ;
      ak4_flavHadron  =  ijet.hadronFlavour()  ;
      ak4_ptGen       =  ptGen;
      ak4_ptResponse  =  pt/ptGen ;
      ak4_dRminGen    =  dRmin;
    }

    ak4_pt_uncorr   =  pt_uncorr;
    ak4_pt          =  pt;
    ak4_eta         =  eta;
    ak4_puid        =  puid;

    ak4_area     = ijet.jetArea();
    ak4_rho      = rho  ;
    ak4_nvtx     = nvtx ;

    ak4JetTree->Fill();

  }

  // ak8 jet Loop
 
  edm::Handle<pat::JetCollection> AK8MINI;
  iEvent.getByToken(ak8jetToken_, AK8MINI);

  edm::Handle<reco::GenJetCollection> AK8GENJET;  
  iEvent.getByToken(ak8genjetToken_, AK8GENJET);

  for (const pat::Jet &ijet : *AK8MINI) {  
    double pt           = ijet.pt();
    if (pt<200) continue;
    double mass         = ijet.mass();
    double rapidity     = ijet.rapidity();
    double ndau         = ijet.numberOfDaughters();
    double prunedMass   = ijet.userFloat("ak8PFJetsCHSPrunedMass");
    double softDropMass = ijet.userFloat("ak8PFJetsCHSSoftDropMass");
    double tau1         = ijet.userFloat("NjettinessAK8:tau1");
    double tau2         = ijet.userFloat("NjettinessAK8:tau2");
    double tau3         = ijet.userFloat("NjettinessAK8:tau3");
    double tau21        = 99;
    double tau32        = 99;

    double puppi_pt           = ijet.userFloat("ak8PFJetsPuppiValueMap:pt");
    double puppi_mass         = ijet.userFloat("ak8PFJetsPuppiValueMap:mass");
    double puppi_eta          = ijet.userFloat("ak8PFJetsPuppiValueMap:eta");
    double puppi_phi          = ijet.userFloat("ak8PFJetsPuppiValueMap:phi");
    double puppi_tau1         = ijet.userFloat("ak8PFJetsPuppiValueMap:NjettinessAK8PuppiTau1");
    double puppi_tau2         = ijet.userFloat("ak8PFJetsPuppiValueMap:NjettinessAK8PuppiTau2");
    double puppi_tau3         = ijet.userFloat("ak8PFJetsPuppiValueMap:NjettinessAK8PuppiTau3");
    double puppi_tau21        = 99;
    double puppi_tau32        = 99;

    double deltaRpup = deltaR(ijet.eta(), ijet.phi(), puppi_eta, puppi_phi );

    if (tau1!=0) tau21 = tau2/tau1;
    if (tau2!=0) tau32 = tau3/tau2;

    if (puppi_tau1!=0) puppi_tau21 = puppi_tau2/puppi_tau1;
    if (puppi_tau2!=0) puppi_tau32 = puppi_tau3/puppi_tau2;

    cout<<"\nJet with pT "<<pt<<" sdMass "<<softDropMass<<endl;


    // Soft Drop + Nsubjettiness tagger
    bool SoftDropTau32Tagged = false;
    if (softDropMass<230 && softDropMass>140 && tau32 <0.65) SoftDropTau32Tagged = true;

    // Get Soft drop subjets for subjet b-tagging
    double mostMassiveSDsubjetMass = 0;
    int count_SD =0;
    auto const & sdSubjets = ijet.subjets("SoftDrop");
    for ( auto const & it : sdSubjets ) {
      double subjetPt       = it->pt();
      double subjetPtUncorr = it->pt();
      double subjetEta      = it->eta();
      double subjetPhi      = it->phi();
      double subjetMass     = it->mass();
      double subjetBdisc    = it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (verbose) cout<<" SD Subjet pt "<<subjetPt<<" uncorr "<<subjetPtUncorr<<" Eta "<<subjetEta<<" deltaRsubjetJet "<<deltaRsubjetJet<<" Mass "<<subjetMass<<" Bdisc "<<subjetBdisc<<endl;
      h_ak8chs_sdSubjetMass ->Fill( subjetMass );
      if (subjetMass > mostMassiveSDsubjetMass) mostMassiveSDsubjetMass = subjetMass;
      count_SD++;
    }

    // Get Soft drop PUPPI subjets 
    TLorentzVector pup0;
    TLorentzVector pup1;
    double mostMassiveSDPUPPIsubjetMass = 0;
    auto const & sdSubjetsPuppi = ijet.subjets("SoftDropPuppi");
    int count_pup=0;
    for ( auto const & it : sdSubjetsPuppi ) {
      double subjetPt       = it->pt();
      double subjetPtUncorr = it->pt();
      double subjetEta      = it->eta();
      double subjetPhi      = it->phi();
      double subjetMass     = it->mass();
      double subjetBdisc    = it->bDiscriminator("pfCombinedInclusiveSecondaryVertexV2BJetTags"); 
      double deltaRsubjetJet = deltaR(ijet.eta(), ijet.phi(), subjetEta, subjetPhi);
      if (verbose) cout<<" SD Subjet pt "<<subjetPt<<" uncorr "<<subjetPtUncorr<<" Eta "<<subjetEta<<" deltaRsubjetJet "<<deltaRsubjetJet<<" Mass "<<subjetMass<<" Bdisc "<<subjetBdisc<<endl; 
      h_ak8puppi_sdSubjetMass ->Fill( subjetMass );
      if (count_pup==0) pup0.SetPtEtaPhiM( subjetPt, subjetEta, subjetPhi, subjetMass);
      if (count_pup==1) pup1.SetPtEtaPhiM( subjetPt, subjetEta, subjetPhi, subjetMass);
      if (subjetMass > mostMassiveSDPUPPIsubjetMass) mostMassiveSDPUPPIsubjetMass = subjetMass;
      count_pup++;
    }

    TLorentzVector puppiSD;
    if (count_pup>1)
    {
      puppiSD = pup0 + pup1;
      cout<<pup0.M()<<" "<<pup1.M()<<" "<<puppiSD.M()<<" "<<endl;
    }

    //Print some jet info
    if (SoftDropTau32Tagged) cout<<"->SoftDropTau32Tagged"<<endl;

    // Fill histograms
    h_ak8chs_pt           ->Fill( pt           );
    h_ak8chs_mass         ->Fill( mass         );
    h_ak8chs_rapidity     ->Fill( rapidity     );
    h_ak8chs_prunedMass   ->Fill( prunedMass   );
    h_ak8chs_softDropMass ->Fill( softDropMass );
    h_ak8chs_tau1         ->Fill( tau1         );
    h_ak8chs_tau2         ->Fill( tau2         );
    h_ak8chs_tau3         ->Fill( tau3         );
    h_ak8chs_tau32        ->Fill( tau32        );
    h_ak8chs_tau21        ->Fill( tau21        );
    h_ak8chs_ndau         ->Fill( ndau         );


    h_ak8puppi_pt           ->Fill( puppi_pt           );
    h_ak8puppi_mass         ->Fill( puppi_mass         );
    h_ak8puppi_softDropMass ->Fill( puppiSD.M()        );
    h_ak8puppi_tau1         ->Fill( puppi_tau1         );
    h_ak8puppi_tau2         ->Fill( puppi_tau2         );
    h_ak8puppi_tau3         ->Fill( puppi_tau3         );
    h_ak8puppi_tau32        ->Fill( puppi_tau32        );
    h_ak8puppi_tau21        ->Fill( puppi_tau21        );

    h_deltaR_chs_puppi      ->Fill( deltaRpup          );
    
    // Tree
    ak8_pt                 = pt           ;
    ak8_mass               = mass         ;
    ak8_rapidity           = rapidity     ;
    ak8_prunedMass         = prunedMass   ;
    ak8_sdMass             = softDropMass ;
    ak8_tau1               = tau1         ;
    ak8_tau2               = tau2         ;
    ak8_tau3               = tau3         ;
    ak8_tau32              = tau32        ;
    ak8_tau21              = tau21        ;
    ak8_ndau               = ndau         ;
    ak8_subjet_M           = mostMassiveSDsubjetMass ;
    ak8_subjet_count       = count_SD ;
    ak8_puppi_pt           = puppi_pt     ;
    ak8_puppi_mass         = puppi_mass   ;
    ak8_puppi_softDropMass = puppiSD.M()  ;
    ak8_puppi_tau1         = puppi_tau1   ;
    ak8_puppi_tau2         = puppi_tau2   ;
    ak8_puppi_tau3         = puppi_tau3   ;
    ak8_puppi_tau32        = puppi_tau32  ;
    ak8_puppi_tau21        = puppi_tau21  ;
    ak8_puppi_subjet_M     = mostMassiveSDPUPPIsubjetMass ;
    ak8_puppi_subjet_count     = count_pup ;

    ak8_area     = ijet.jetArea();
    ak8_rho      = rho  ;
    ak8_nvtx     = nvtx ;

    if (!iEvent.isRealData()) {
      float dRmin = 100.;
      float ptGen = -1.0;
      float mGen = -1.0;
      for (const reco::GenJet &igen : *AK8GENJET) {  
        float dR = deltaR(ijet.eta(),ijet.phi(),igen.eta(),igen.phi());
        if (dR < dRmin) {
          dRmin = dR;
          ptGen = igen.pt();
          mGen = igen.mass();
        }
      }
      ak8_mGen        =  mGen;
      ak8_ptGen       =  ptGen;
      ak8_ptResponse  =  pt/ptGen ;
      ak8_dRminGen    =  dRmin;
    }

    ak8JetTree -> Fill();

  }

}


// ------------ method called once each job just before starting event loop  ------------
void 
JetMiniValidation::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetMiniValidation::endJob() 
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetMiniValidation::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetMiniValidation);
