// -*- C++ -*-
//
// Package:    Analysis/JetTester
// Class:      JetTester
// 
/**\class JetTester JetTester.cc Analysis/JetTester/plugins/JetTester.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  James Dolen
//         Created:  Thu, 11 Jun 2015 22:52:52 GMT
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

#include "RecoJets/JetAlgorithms/interface/CATopJetHelper.h"
#include "DataFormats/BTauReco/interface/CATopJetTagInfo.h"

//#include "DataFormats/JetReco/interface/CaloJet.h"
//#include "DataFormats/JetReco/interface/CaloJetCollection.h"
//#include "DataFormats/Candidate/interface/Candidate.h"
//#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
//#include "DataFormats/Candidate/interface/Candidate.h"
//#include "DataFormats/Candidate/interface/CompositeCandidate.h"
//#include "DataFormats/Candidate/interface/Particle.h"
//#include "DataFormats/Candidate/interface/Candidate.h"
//#include "DataFormats/Candidate/interface/CandidateFwd.h"
//#include "DataFormats/Candidate/interface/CandMatchMap.h" 
//#include "DataFormats/RecoCandidate/interface/RecoCandidate.h"
//#include "DataFormats/Math/interface/LorentzVector.h"
//#include "SimDataFormats/PileupSummaryInfo/interface/PileupSummaryInfo.h" 
// JEC
//#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
//#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
//#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"

// utilities
//#include "DataFormats/Math/interface/deltaR.h"
//#include "DataFormats/Math/interface/deltaPhi.h"

// TFile
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"

// fastjet
//#include <fastjet/JetDefinition.hh>
//#include <fastjet/PseudoJet.hh>
//#include "fastjet/tools/Filter.hh"
//#include <fastjet/ClusterSequence.hh>
//#include <fastjet/ClusterSequenceArea.hh>


// root
#include "TH1.h"
#include "TH2.h"
#include "TTree.h"


//
// class declaration
//

class JetTester : public edm::EDAnalyzer {
   public:
      explicit JetTester(const edm::ParameterSet&);
      ~JetTester();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() override;
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
      virtual void endJob() override;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

      // ----------member data ---------------------------
      TH1D * h_ak12chs_pt            ;
      TH1D * h_ak12chs_mass          ;
      TH1D * h_ak12chs_rapidity      ;
      TH1D * h_ak12chs_prunedMass    ;
      TH1D * h_ak12chs_trimmedMass   ;
      TH1D * h_ak12chs_filteredMass  ;
      TH1D * h_ak12chs_softDropMass  ;
      TH1D * h_ak12chs_tau1          ;
      TH1D * h_ak12chs_tau2          ;
      TH1D * h_ak12chs_tau3          ;
      TH1D * h_ak12chs_tau4          ;
      TH1D * h_ak12chs_tau32         ;
      TH1D * h_ak12chs_tau21         ;
      TH1D * h_ak12chs_ndau          ;
 
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

      TH1D * h_ak8puppi_pt           ;
      TH1D * h_ak8puppi_mass         ;
      TH1D * h_ak8puppi_rapidity     ;
      TH1D * h_ak8puppi_prunedMass   ;
      TH1D * h_ak8puppi_trimmedMass  ;
      TH1D * h_ak8puppi_filteredMass ;
      TH1D * h_ak8puppi_softDropMass ;
      TH1D * h_ak8puppi_ndau         ;

      TH1D * h_ak8pf_pt              ;
      TH1D * h_ak8pf_mass            ;
      TH1D * h_ak8pf_rapidity        ;
      TH1D * h_ak8pf_prunedMass      ;
      TH1D * h_ak8pf_trimmedMass     ;
      TH1D * h_ak8pf_filteredMass    ;
      TH1D * h_ak8pf_softDropMass    ;
      TH1D * h_ak8pf_ndau            ;

      TH1D * h_ak8chsmod_pt              ;
      TH1D * h_ak8chsmod_mass            ;
      TH1D * h_ak8chsmod_rapidity        ;
      TH1D * h_ak8chsmod_prunedMass      ;
      TH1D * h_ak8chsmod_trimmedMass     ;
      TH1D * h_ak8chsmod_filteredMass    ;
      TH1D * h_ak8chsmod_softDropMass    ;
      TH1D * h_ak8chsmod_ndau            ;

      

};

//
// constructors and destructor
//
JetTester::JetTester(const edm::ParameterSet& iConfig)
{
  edm::Service<TFileService> fs;

  h_ak12chs_pt            =  fs->make<TH1D>("h_ak12chs_pt"               ,"",100,0,3000); 
  h_ak12chs_mass          =  fs->make<TH1D>("h_ak12chs_mass"             ,"",100,0,300); 
  h_ak12chs_rapidity      =  fs->make<TH1D>("h_ak12chs_rapidity"         ,"",100,-5, 5); 
  h_ak12chs_prunedMass    =  fs->make<TH1D>("h_ak12chs_prunedMass"       ,"",100,0,300); 
  h_ak12chs_trimmedMass   =  fs->make<TH1D>("h_ak12chs_trimmedMass"      ,"",100,0,300); 
  h_ak12chs_filteredMass  =  fs->make<TH1D>("h_ak12chs_filteredMass"     ,"",100,0,300); 
  h_ak12chs_softDropMass  =  fs->make<TH1D>("h_ak12chs_softDropMass"     ,"",100,0,300); 
  h_ak12chs_tau1          =  fs->make<TH1D>("h_ak12chs_tau1"             ,"",100,0,  1); 
  h_ak12chs_tau2          =  fs->make<TH1D>("h_ak12chs_tau2"             ,"",100,0,  1); 
  h_ak12chs_tau3          =  fs->make<TH1D>("h_ak12chs_tau3"             ,"",100,0,  1); 
  h_ak12chs_tau4          =  fs->make<TH1D>("h_ak12chs_tau4"             ,"",100,0,  1); 
  h_ak12chs_tau32         =  fs->make<TH1D>("h_ak12chs_tau32"            ,"",100,0,  1); 
  h_ak12chs_tau21         =  fs->make<TH1D>("h_ak12chs_tau21"            ,"",100,0,  1); 
  h_ak12chs_ndau          =  fs->make<TH1D>("h_ak12chs_ndau"             ,"",100,0,300); 
 
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

  h_ak8puppi_pt           =  fs->make<TH1D>("h_ak8puppi_pt"              ,"",100,0,3000);
  h_ak8puppi_mass         =  fs->make<TH1D>("h_ak8puppi_mass"            ,"",100,0,300);
  h_ak8puppi_rapidity     =  fs->make<TH1D>("h_ak8puppi_rapidity"        ,"",100,-5, 5);
  h_ak8puppi_prunedMass   =  fs->make<TH1D>("h_ak8puppi_prunedMass"      ,"",100,0,300);
  h_ak8puppi_trimmedMass  =  fs->make<TH1D>("h_ak8puppi_trimmedMass"     ,"",100,0,300);
  h_ak8puppi_filteredMass =  fs->make<TH1D>("h_ak8puppi_filteredMass"    ,"",100,0,300);
  h_ak8puppi_softDropMass =  fs->make<TH1D>("h_ak8puppi_softDropMass"    ,"",100,0,300);
  h_ak8puppi_ndau         =  fs->make<TH1D>("h_ak8puppi_ndau"            ,"",100,0,300);

  h_ak8pf_pt              =  fs->make<TH1D>("h_ak8pf_pt"                 ,"",100,0,3000);
  h_ak8pf_mass            =  fs->make<TH1D>("h_ak8pf_mass"               ,"",100,0,300);
  h_ak8pf_rapidity        =  fs->make<TH1D>("h_ak8pf_rapidity"           ,"",100,-5,5);
  h_ak8pf_prunedMass      =  fs->make<TH1D>("h_ak8pf_prunedMass"         ,"",100,0,300);
  h_ak8pf_trimmedMass     =  fs->make<TH1D>("h_ak8pf_trimmedMass"        ,"",100,0,300);
  h_ak8pf_filteredMass    =  fs->make<TH1D>("h_ak8pf_filteredMass"       ,"",100,0,300);
  h_ak8pf_softDropMass    =  fs->make<TH1D>("h_ak8pf_softDropMass"       ,"",100,0,300);
  h_ak8pf_ndau            =  fs->make<TH1D>("h_ak8pf_ndau"               ,"",100,0,300);

  h_ak8chsmod_pt              =  fs->make<TH1D>("h_ak8chsmod_pt"                 ,"",100,0,3000);
  h_ak8chsmod_mass            =  fs->make<TH1D>("h_ak8chsmod_mass"               ,"",100,0,300);
  h_ak8chsmod_rapidity        =  fs->make<TH1D>("h_ak8chsmod_rapidity"           ,"",100,-5,5);
  h_ak8chsmod_prunedMass      =  fs->make<TH1D>("h_ak8chsmod_prunedMass"         ,"",100,0,300);
  h_ak8chsmod_trimmedMass     =  fs->make<TH1D>("h_ak8chsmod_trimmedMass"        ,"",100,0,300);
  h_ak8chsmod_filteredMass    =  fs->make<TH1D>("h_ak8chsmod_filteredMass"       ,"",100,0,300);
  h_ak8chsmod_softDropMass    =  fs->make<TH1D>("h_ak8chsmod_softDropMass"       ,"",100,0,300);
  h_ak8chsmod_ndau            =  fs->make<TH1D>("h_ak8chsmod_ndau"               ,"",100,0,300);

  // JetTree = new TTree("JetTree","JetTree");  
  // JetTree->Branch("EventNumber"                         ,  & EventNumber               , "EventNumber/I"                      );
  // JetTree->Branch("Weight" 
}


JetTester::~JetTester()
{
}


//
// member functions
//

// ------------ method called for each event  ------------
void
JetTester::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;
  using namespace std;
  using namespace reco;
  using namespace pat;

  //--------------------------------------------------------------------------------------------
  // AK R=1.2 jets - from toolbox
  edm::Handle<std::vector<pat::Jet> > AK12CHS;
  iEvent.getByLabel( "selectedPatJetsAK12PFCHS", AK12CHS );
  for ( std::vector<pat::Jet>::const_iterator jetBegin = AK12CHS->begin(), jetEnd = AK12CHS->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  {
    double pt           = ijet->pt();
    if (pt<150) continue;
    double mass         = ijet->mass();
    double rapidity     = ijet->rapidity();
    double prunedMass   = ijet->userFloat("ak12PFJetsCHSPrunedMass");
    double trimmedMass  = ijet->userFloat("ak12PFJetsCHSTrimmedMass");
    double filteredMass = ijet->userFloat("ak12PFJetsCHSFilteredMass");
    double softDropMass = ijet->userFloat("ak12PFJetsCHSSoftDropMass");
    double tau1         = ijet->userFloat("NjettinessAK12CHS:tau1");
    double tau2         = ijet->userFloat("NjettinessAK12CHS:tau2");
    double tau3         = ijet->userFloat("NjettinessAK12CHS:tau3");
    double tau4         = ijet->userFloat("NjettinessAK12CHS:tau4");
    double ndau         = ijet->numberOfDaughters();

    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=2) tau21 = tau2/tau1;
    if (tau2!=2) tau32 = tau3/tau2;
    h_ak12chs_pt           ->Fill( pt           );
    h_ak12chs_mass         ->Fill( mass         );
    h_ak12chs_rapidity     ->Fill( rapidity     );
    h_ak12chs_prunedMass   ->Fill( prunedMass   );
    h_ak12chs_trimmedMass  ->Fill( trimmedMass  );
    h_ak12chs_filteredMass ->Fill( filteredMass );
    h_ak12chs_softDropMass ->Fill( softDropMass );
    h_ak12chs_tau1         ->Fill( tau1         );
    h_ak12chs_tau2         ->Fill( tau2         );
    h_ak12chs_tau3         ->Fill( tau3         );
    h_ak12chs_tau4         ->Fill( tau4         );
    h_ak12chs_tau32        ->Fill( tau32        );
    h_ak12chs_tau21        ->Fill( tau21        );
    h_ak12chs_ndau         ->Fill( ndau         );
    // cout<<"pt "<<pt<<" softDropMass "<<softDropMass<<" t1 "<<t1<<" ndau "<<ndau<<endl;
  }

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 jets - default miniAOD
  edm::Handle<std::vector<pat::Jet> > AK8MINI;
  iEvent.getByLabel( "slimmedJetsAK8", AK8MINI );
  for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8MINI->begin(), jetEnd = AK8MINI->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  {
    double pt           = ijet->pt();
    if (pt<150) continue;
    double mass         = ijet->mass();
    double rapidity     = ijet->rapidity();
    double prunedMass   = ijet->userFloat("ak8PFJetsCHSPrunedMass");
    double trimmedMass  = ijet->userFloat("ak8PFJetsCHSTrimmedMass");
    double filteredMass = ijet->userFloat("ak8PFJetsCHSFilteredMass");
    double softDropMass = ijet->userFloat("ak8PFJetsCHSSoftDropMass");
    double tau1         = ijet->userFloat("NjettinessAK8:tau1");
    double tau2         = ijet->userFloat("NjettinessAK8:tau2");
    double tau3         = ijet->userFloat("NjettinessAK8:tau3");
    double ndau         = ijet->numberOfDaughters();

    double tau21 = 99;
    double tau32 = 99;
    if (tau1!=2) tau21 = tau2/tau1;
    if (tau2!=2) tau32 = tau3/tau2;

    // Soft Drop + Nsubjettiness tagger
    bool SoftDropTau32Tagged = false;
    if (softDropMass<230 && softDropMass>140 && tau32 <0.65) SoftDropTau32Tagged = true;

    //CMS Top Tagger
    reco::CATopJetTagInfo const * tagInfo =  dynamic_cast<reco::CATopJetTagInfo const *>( ijet->tagInfo("caTop"));
    bool Run1CMStopTagged = false;
    if ( tagInfo != 0 ) {
        double minMass = tagInfo->properties().minMass;
        double topMass = tagInfo->properties().topMass;
        int nSubJets = tagInfo->properties().nSubJets;
        if ( nSubJets > 2 && minMass > 50.0 && topMass > 140.0 &&  topMass < 250.0 ) Run1CMStopTagged = true;
	}	

	//Print some jet info
    cout<<"Jet with pT "<<pt<<" sdMass "<<softDropMass<<endl;
    if (SoftDropTau32Tagged) cout<<"->SoftDropTau32Tagged"<<endl;
    if (Run1CMStopTagged)    cout<<"->Run1CMStopTagged"<<endl;

	// Fill histograms
    h_ak8chs_pt           ->Fill( pt           );
    h_ak8chs_mass         ->Fill( mass         );
    h_ak8chs_rapidity     ->Fill( rapidity     );
    h_ak8chs_prunedMass   ->Fill( prunedMass   );
    h_ak8chs_trimmedMass  ->Fill( trimmedMass  );
    h_ak8chs_filteredMass ->Fill( filteredMass );
    h_ak8chs_softDropMass ->Fill( softDropMass );
    h_ak8chs_tau1         ->Fill( tau1         );
    h_ak8chs_tau2         ->Fill( tau2         );
    h_ak8chs_tau3         ->Fill( tau3         );
    h_ak8chs_tau32        ->Fill( tau32        );
    h_ak8chs_tau21        ->Fill( tau21        );
    h_ak8chs_ndau         ->Fill( ndau         );
  }

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 PUPPI jets - from toolbox

  edm::Handle<std::vector<pat::Jet> > AK8Puppi;
  iEvent.getByLabel( "selectedPatJetsAK8PFPuppi", AK8Puppi );
  for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8Puppi->begin(), jetEnd = AK8Puppi->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  {
    double pt           = ijet->pt();
    if (pt<150) continue;
    double mass         = ijet->mass();
    double rapidity     = ijet->rapidity();
    double prunedMass   = ijet->userFloat("ak8PFJetsPuppiPrunedMass");
    double trimmedMass  = ijet->userFloat("ak8PFJetsPuppiTrimmedMass");
    double filteredMass = ijet->userFloat("ak8PFJetsPuppiFilteredMass");
    double softDropMass = ijet->userFloat("ak8PFJetsPuppiSoftDropMass");
    double ndau         = ijet->numberOfDaughters();

    h_ak8puppi_pt           ->Fill( pt           );
    h_ak8puppi_mass         ->Fill( mass         );
    h_ak8puppi_rapidity     ->Fill( rapidity     );
    h_ak8puppi_prunedMass   ->Fill( prunedMass   );
    h_ak8puppi_trimmedMass  ->Fill( trimmedMass  );
    h_ak8puppi_filteredMass ->Fill( filteredMass );
    h_ak8puppi_softDropMass ->Fill( softDropMass );
    h_ak8puppi_ndau         ->Fill( ndau         );
  }

  //--------------------------------------------------------------------------------------------
  // AK R=0.8 PF jets - from toolbox

  edm::Handle<std::vector<pat::Jet> > AK8PF;
  iEvent.getByLabel( "selectedPatJetsAK8PF", AK8PF );
  for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8PF->begin(), jetEnd = AK8PF->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  {
    double pt           = ijet->pt();
    if (pt<150) continue;
    double mass         = ijet->mass();
    double rapidity     = ijet->rapidity();
    double prunedMass   = ijet->userFloat("ak8PFJetsPrunedMass");
    double trimmedMass  = ijet->userFloat("ak8PFJetsTrimmedMass");
    double filteredMass = ijet->userFloat("ak8PFJetsFilteredMass");
    double softDropMass = ijet->userFloat("ak8PFJetsSoftDropMass");
    double ndau         = ijet->numberOfDaughters();

    h_ak8pf_pt           ->Fill( pt           );
    h_ak8pf_mass         ->Fill( mass         );
    h_ak8pf_rapidity     ->Fill( rapidity     );
    h_ak8pf_prunedMass   ->Fill( prunedMass   );
    h_ak8pf_trimmedMass  ->Fill( trimmedMass  );
    h_ak8pf_filteredMass ->Fill( filteredMass );
    h_ak8pf_softDropMass ->Fill( softDropMass );
    h_ak8pf_ndau         ->Fill( ndau         );
  }


  //--------------------------------------------------------------------------------------------
  // AK R=0.8 CHS jets with modified grooming parameters - from toolbox

  edm::Handle<std::vector<pat::Jet> > AK8CHS;
  iEvent.getByLabel( "selectedPatJetsAK8PFCHS", AK8CHS );
  for ( std::vector<pat::Jet>::const_iterator jetBegin = AK8CHS->begin(), jetEnd = AK8CHS->end(), ijet = jetBegin; ijet != jetEnd; ++ijet ) 
  {
    double pt           = ijet->pt();
    if (pt<150) continue;
    double mass         = ijet->mass();
    double rapidity     = ijet->rapidity();
    double prunedMass   = ijet->userFloat("ak8CHSJetsCHSPrunedMass");
    double trimmedMass  = ijet->userFloat("ak8CHSJetsCHSTrimmedMass");
    double filteredMass = ijet->userFloat("ak8CHSJetsCHSFilteredMass");
    double softDropMass = ijet->userFloat("ak8CHSJetsCHSSoftDropMass");
    double ndau         = ijet->numberOfDaughters();

    h_ak8chsmod_pt           ->Fill( pt           );
    h_ak8chsmod_mass         ->Fill( mass         );
    h_ak8chsmod_rapidity     ->Fill( rapidity     );
    h_ak8chsmod_prunedMass   ->Fill( prunedMass   );
    h_ak8chsmod_trimmedMass  ->Fill( trimmedMass  );
    h_ak8chsmod_filteredMass ->Fill( filteredMass );
    h_ak8chsmod_softDropMass ->Fill( softDropMass );
    h_ak8chsmod_ndau         ->Fill( ndau         );
  }

//   [jdolen@cmslpc24 python]$ edmdump jettoolbox.root 
// Type                           Module                      Label            Process   
// --------------------------------------------------------------------------------------
// edm::ValueMap<float>           "ak12PFJetsCHSFilteredMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak12PFJetsCHSPrunedMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak12PFJetsCHSSoftDropMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak12PFJetsCHSTrimmedMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsCHSFilteredMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsCHSSoftDropMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsCHSTrimmedMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsFilteredMass"     ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsPuppiFilteredMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsPuppiSoftDropMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsPuppiTrimmedMass"   ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsSoftDropMass"     ""               "Ana"     
// edm::ValueMap<float>           "ak8PFJetsTrimmedMass"      ""               "Ana"     
// edm::ValueMap<float>           "NjettinessAK12CHS"         "tau1"           "Ana"     
// edm::ValueMap<float>           "NjettinessAK12CHS"         "tau2"           "Ana"     
// edm::ValueMap<float>           "NjettinessAK12CHS"         "tau3"           "Ana"     
// edm::ValueMap<float>           "NjettinessAK12CHS"         "tau4"           "Ana"     
// vector<pat::Jet>               "selectedPatJetsAK12PFCHS"   ""               "Ana"     
// vector<pat::Jet>               "selectedPatJetsAK8PF"      ""               "Ana"     
// vector<pat::Jet>               "selectedPatJetsAK8PFCHS"   ""               "Ana"     
// vector<pat::Jet>               "selectedPatJetsAK8PFPuppi"   ""               "Ana"     
// vector<reco::GenJet>           "selectedPatJetsAK12PFCHS"   "genJets"        "Ana"     
// vector<reco::GenJet>           "selectedPatJetsAK8PF"      "genJets"        "Ana"     
// vector<reco::GenJet>           "selectedPatJetsAK8PFCHS"   "genJets"        "Ana"     
// vector<reco::GenJet>           "selectedPatJetsAK8PFPuppi"   "genJets"        "Ana"     
// vector<reco::PFCandidate>      "selectedPatJetsAK12PFCHS"   "pfCandidates"   "Ana"     
// vector<reco::PFCandidate>      "selectedPatJetsAK8PF"      "pfCandidates"   "Ana"     
// vector<reco::PFCandidate>      "selectedPatJetsAK8PFCHS"   "pfCandidates"   "Ana"     
// vector<reco::PFCandidate>      "selectedPatJetsAK8PFPuppi"   "pfCandidates"   "Ana"  
}


// ------------ method called once each job just before starting event loop  ------------
void 
JetTester::beginJob()
{
}

// ------------ method called once each job just after ending the event loop  ------------
void 
JetTester::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
JetTester::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
JetTester::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
JetTester::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
JetTester::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
JetTester::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(JetTester);
