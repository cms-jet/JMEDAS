////////////////////////////////////////////////////////////////////////////////
//
// convertPackedCandToRecoCand
// ---------------------------
//
//                          01/08/2015 Alexx Perloff <aperloff@physics.tamu.edu>
////////////////////////////////////////////////////////////////////////////////


#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/MakerMacros.h"
 
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
 
#include "DataFormats/Common/interface/Handle.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"

#include <iostream>
#include <memory>

using namespace std;
using namespace edm;
using namespace reco;


////////////////////////////////////////////////////////////////////////////////
// class definition
////////////////////////////////////////////////////////////////////////////////

//______________________________________________________________________________
class convertPackedCandToRecoCand : public edm::EDProducer
{
public:
  // construction/destruction
  convertPackedCandToRecoCand(const edm::ParameterSet& iConfig);
  ~convertPackedCandToRecoCand() {;}
  
  // member functions
  void produce(edm::Event& iEvent,const edm::EventSetup& iSetup);
  void endJob();

private:
  // member data
  edm::InputTag src_;

  std::string  moduleName_;

};




////////////////////////////////////////////////////////////////////////////////
// construction/destruction
////////////////////////////////////////////////////////////////////////////////

//______________________________________________________________________________
convertPackedCandToRecoCand::convertPackedCandToRecoCand(const edm::ParameterSet& iConfig)
  : src_(iConfig.getParameter<InputTag>("src"))
  , moduleName_(iConfig.getParameter<string>("@module_label"))
{
  //produces<reco::PFCandidateCollection>("convertedPackedPFCandidates");
  produces<reco::PFCandidateCollection>();
}


////////////////////////////////////////////////////////////////////////////////
// implementation of member functions
////////////////////////////////////////////////////////////////////////////////

//______________________________________________________________________________
void convertPackedCandToRecoCand::produce(edm::Event& iEvent,const edm::EventSetup& iSetup)
{

  edm::Handle<vector<pat::PackedCandidate> > packedCands_;
  //edm::Handle<View<Candidate> > packedCands_;
  
  iEvent.getByLabel(src_,packedCands_);
  
  size_t nCands = (size_t)packedCands_->size();
  
  auto_ptr<reco::PFCandidateCollection> recoCands(new vector<reco::PFCandidate>);

  reco::PFCandidate dummy;
    
  for(unsigned int iCand = 0; iCand<nCands; iCand++) {
    //reco::CandidateBaseRef intCandBaseRef = packedCands_->at(iCand).masterClone();
    //reco::PFCandidateRef intPFCandRef = intCandBaseRef.castTo<reco::PFCandidateRef>();
    //recoCands->push_back(*intPFCandRef);
    
    //reco::PFCandidate intPFCand = static_cast<reco::PFCandidate>(packedCands_->at(iCand));

    reco::PFCandidate intPFCand(packedCands_->at(iCand).charge(),packedCands_->at(iCand).p4(),dummy.translatePdgIdToType(packedCands_->at(iCand).pdgId()));
    recoCands->push_back(intPFCand);
  }
  
  //iEvent.put(recoCands,"convertedPackedPFCandidates");
  iEvent.put(recoCands);
}


//______________________________________________________________________________
void convertPackedCandToRecoCand::endJob()
{
}


////////////////////////////////////////////////////////////////////////////////
// plugin definition
////////////////////////////////////////////////////////////////////////////////

DEFINE_FWK_MODULE(convertPackedCandToRecoCand);
