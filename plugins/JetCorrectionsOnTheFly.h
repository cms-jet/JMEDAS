// Template class: JetCorrectionsOnTheFly
// Description:  Example of simple EDAnalyzer correcting jets "on the fly".
// Author: S. Rappoccio
// Date: 07 Dec 2011
#ifndef JetCorrectionsOnTheFly_h
#define JetCorrectionsOnTheFly_h
#include <vector>
#include <string>
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Utilities/interface/InputTag.h"
#include "PhysicsTools/FWLite/interface/TFileService.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectionUncertainty.h"
#include "CondFormats/JetMETObjects/interface/FactorizedJetCorrector.h"
#include "CondFormats/JetMETObjects/interface/JetCorrectorParameters.h"
#include <boost/shared_ptr.hpp>

class JetCorrectionsOnTheFly : public edm::EDAnalyzer 
   {
     public:
       JetCorrectionsOnTheFly(edm::ParameterSet const& cfg);
     private:
       void beginJob();
       void analyze(edm::Event const& e, edm::EventSetup const& iSetup);
       void endJob();

       edm::InputTag            jetSrc_;
       edm::InputTag            rhoSrc_;
       edm::InputTag            pvSrc_;

       std::vector<std::string> jecPayloadNames_;
       std::string              jecUncName_;
       
	TH1F *corrPt;
	TH1F *corrPtUp;
	TH1F *corrPtDown;
       

       boost::shared_ptr<JetCorrectionUncertainty> jecUnc_;
       boost::shared_ptr<FactorizedJetCorrector> jec_;
   };
#endif
