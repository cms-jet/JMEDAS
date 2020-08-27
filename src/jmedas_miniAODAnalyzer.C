// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/PackedCandidate.h"
//
// class declaration
//

class MiniAnalyzer : public edm::EDAnalyzer {
   public:
      explicit MiniAnalyzer (const edm::ParameterSet&);
      ~MiniAnalyzer();

   private:
      virtual void analyze(const edm::Event&, const edm::EventSetup&) override;

      // ----------member data ---------------------------
      edm::EDGetTokenT vtxToken_;
      edm::EDGetTokenT jetToken_;
      edm::EDGetTokenT fatjetToken_;

};

MiniAnalyzer::MiniAnalyzer(const edm::ParameterSet& iConfig):
    vtxToken_(consumes(iConfig.getParameter("vertices"))),
    jetToken_(consumes(iConfig.getParameter("jets"))),
    fatjetToken_(consumes(iConfig.getParameter("fatjets"))),
{
}

MiniAnalyzer::~MiniAnalyzer()
{
}

void
MiniAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{

    edm::Handle vertices;
    iEvent.getByToken(vtxToken_, vertices);
    if (vertices->empty()) return; // skip the event if no PV found
    const reco::Vertex &PV = vertices->front();

    edm::Handle jets;
    iEvent.getByToken(jetToken_, jets);
    int ijet = 0;
    for (const pat::Jet &j : *jets) {
        if (j.pt() < 20) continue;
        printf("jet  with pt %5.1f (raw pt %5.1f), eta %+4.2f, btag CSV %.3f, CISV %.3f, pileup mva disc %+.2f\n",
            j.pt(), j.pt()*j.jecFactor("Uncorrected"), j.eta(), std::max(0.f,j.bDiscriminator("combinedSecondaryVertexBJetTags")), std::max(0.f,j.bDiscriminator("combinedInclusiveSecondaryVertexBJetTags")), j.userFloat("pileupJetId:fullDiscriminant"));
        if ((++ijet) == 1) { // for the first jet, lets print the leading constituents
            std::vector daus(j.daughterPtrVector());
            std::sort(daus.begin(), daus.end(), [](const reco::CandidatePtr &p1, const reco::CandidatePtr &p2) { return p1->pt() > p2->pt(); }); // the joys of C++11
            for (unsigned int i2 = 0, n = daus.size(); i2 < n && i2 <= 3; ++i2) {
                const pat::PackedCandidate &cand = dynamic_cast<const pat::PackedCandidate &>(*daus[i2]);
                printf("         constituent %3d: pt %6.2f, dz(pv) %+.3f, pdgId %+3d\n", i2,cand.pt(),cand.dz(PV.position()),cand.pdgId());
            }
        }
    }

    edm::Handle fatjets;
    iEvent.getByToken(fatjetToken_, fatjets);
    for (const pat::Jet &j : *fatjets) {
        printf("AK8j with pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f ungroomed, %5.1f softdrop, %5.1f pruned CHS\n",
            j.pt(), j.pt()*j.jecFactor("Uncorrected"), j.eta(), j.mass(), j.userFloat("ak8PFJetsPuppiSoftDropMass"), j.userFloat("ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass") );

        // To get the constituents of the AK8 jets, you have to loop over all of the
        // daughters recursively. To save space, the first two constituents are actually
        // the Soft Drop SUBJETS, which will then point to their daughters.
        // The remaining constituents are those constituents removed by soft drop but
        // still in the AK8 jet.
   std::vector constituents;
        for ( unsigned ida = 0; ida < j.numberOfDaughters(); ++ida ) {
     reco::Candidate const * cand = j.daughter(ida);
     if ( cand->numberOfDaughters() == 0 )
       constituents.push_back( cand ) ;
     else {
       for ( unsigned jda = 0; jda < cand->numberOfDaughters(); ++jda ) {
         reco::Candidate const * cand2 = cand->daughter(jda);
         constituents.push_back( cand2 );
       }
     }
   }
   std::sort( constituents.begin(), constituents.end(), [] (reco::Candidate const * ida, reco::Candidate const * jda){return ida->pt() > jda->pt();} );

   for ( unsigned int ida = 0; ida < constituents.size(); ++ida ) {
     const pat::PackedCandidate &cand = dynamic_cast<const pat::PackedCandidate &>(*constituents[ida]);
     printf("         constituent %3d: pt %6.2f, dz(pv) %+.3f, pdgId %+3d\n", ida,cand.pt(),cand.dz(PV.position()),cand.pdgId());
   }

   auto sdSubjets = j.subjets("SoftDropPuppi");
   for ( auto const & isd : sdSubjets ) {
     printf("  sd subjet with pt %5.1f (raw pt %5.1f), eta %+4.2f, mass %5.1f ungroomed\n",
       isd->pt(), isd->pt()*isd->jecFactor("Uncorrected"), isd->eta(), isd->mass() );

   }
    }
}


//define this as a plug-in
DEFINE_FWK_MODULE(MiniAnalyzer);
