// Implementation of template class: JetPlotsExample
// Description:  Example of simple EDAnalyzer for jets from MiniAOD
// Author: S. Rappoccio
// Date:  3 December 2014
#include "Analysis/JMEDAS/plugins/JetPlotsExample.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include <TFile.h>
#include <TLorentzVector.h> 
#include <cmath>
#include "DataFormats/JetReco/interface/CATopJetTagInfo.h"
#include "DataFormats/Math/interface/LorentzVector.h"
#include "DataFormats/Math/interface/Vector.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

////////////////////////////////////////////////////////////////////////////////////////
JetPlotsExample::JetPlotsExample(edm::ParameterSet const& cfg) :
  jetSrc_   (cfg.getParameter<edm::InputTag>("jetSrc") ),     // jet collection to get
  leadJetPtMin_ (cfg.getParameter<double>("leadJetPtMin") ),  // minimum jet pt of leading jet
  jetPtMin_ (cfg.getParameter<double>("jetPtMin") ),          // minimum jet pt of all jets
  plotSubstructure_(cfg.getParameter<bool>("plotSubstructure"))     // plot substructure? 
{

  // Get the TFileService to handle plots
  edm::Service<TFileService> fileService;


  // Make histograms in that directory
  hPt           = fileService->make<TH1F>("hPt", "Jet pt", 60, 0., 3000.);
  hRapidity     = fileService->make<TH1F>("hRapidity", "Jet Rapidity", 50, -5.0, 5.0);
  hPhi          = fileService->make<TH1F>("hPhi", "Jet Azimuthal Angle", 50, -TMath::Pi(), TMath::Pi());
  hMass         = fileService->make<TH1F>("hMass", "Jet Mass", 80, 0., 400.);
  hArea         = fileService->make<TH1F>("hArea", "Jet Area", 50, 0., 5.0);
  hMassPruned   = fileService->make<TH1F>("hMassPruned", "Pruned Jet Mass", 80, 0., 400.);
  hMassTrimmed  = fileService->make<TH1F>("hMassTrimmed", "Trimmed Jet Mass", 80, 0., 400.);
  hMassFiltered = fileService->make<TH1F>("hMassFiltered", "Filtered Jet Mass", 80, 0., 400.);
  hTau21        = fileService->make<TH1F>("hTau21", "Jet #tau_{2} / #tau_{1}", 50, 0., 1.);
  hTau32        = fileService->make<TH1F>("hTau32", "Jet #tau_{3} / #tau_{2}", 50, 0., 1.);
  hCATopMinMass = fileService->make<TH1F>("hCATopMinMass", "CATop Jet minmass", 50, 0., 150.);
  hCATopNsubjets= fileService->make<TH1F>("hCATopNsubjets", "CATop Jet Nsubjets", 5, 0., 5.);
  
  

}
////////////////////////////////////////////////////////////////////////////////////////
void JetPlotsExample::beginJob() 
{
}
////////////////////////////////////////////////////////////////////////////////////////
void JetPlotsExample::analyze(edm::Event const& evt, edm::EventSetup const& iSetup) 
{


  // Get the jet collection
  edm::Handle<edm::View<pat::Jet> > jets;
  evt.getByLabel(jetSrc_,jets);

  // Ensure that we have at least one jet
  if ( jets->size() < 1 ) return;

  // Ensure that the leading jet is above trigger threshold
  edm::View<pat::Jet>::const_iterator ibegin = jets->begin();
  edm::View<pat::Jet>::const_iterator iend = jets->end();
  edm::View<pat::Jet>::const_iterator ijet = ibegin;
  if ( ibegin->pt() < leadJetPtMin_ )
    return;



  // Loop over the "hard" jets
  for ( ; ijet != iend; ++ijet ) {
    if ( ijet->pt() < jetPtMin_ ) continue;
    // Plot the "hard jet" quantities
    hPt->Fill( ijet->pt() );
    hRapidity->Fill( ijet->rapidity() );
    hPhi->Fill( ijet->phi() );
    hMass->Fill( ijet->mass() );
    hArea->Fill( ijet->jetArea() );

    if ( plotSubstructure_ ) {
      hMassPruned->Fill( ijet->userFloat("ak8PFJetsCHSPrunedLinks") );
      hMassTrimmed->Fill( ijet->userFloat("ak8PFJetsCHSTrimmedLinks") );
      hMassFiltered->Fill( ijet->userFloat("ak8PFJetsCHSFilteredLinks") );
      // Get n-subjettiness "tau" variables
      float tau1 = ijet->userFloat("NjettinessAK8:tau1");
      float tau2 = ijet->userFloat("NjettinessAK8:tau2");
      float tau3 = ijet->userFloat("NjettinessAK8:tau3");
      if ( tau1 > 0.0001 ) hTau21->Fill( tau2/tau1);
      else                 hTau21->Fill( -1.0 );
      if ( tau2 > 0.0001 ) hTau32->Fill( tau3/tau2);
      else                 hTau32->Fill( -1.0 );
      reco::CATopJetTagInfo const * caTopTagInfo = dynamic_cast<reco::CATopJetTagInfo const * > (ijet->tagInfo("caTop"));
      if ( caTopTagInfo != 0 ) {
	hCATopMinMass->Fill( caTopTagInfo->properties().minMass );
	hCATopNsubjets->Fill( caTopTagInfo->properties().nSubJets );
      }
    }
  }
}




////////////////////////////////////////////////////////////////////////////////////////
void JetPlotsExample::endJob() 
{
}
/////////// Register Modules ////////
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(JetPlotsExample);
