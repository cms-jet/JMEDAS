#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/SingleObjectSelector.h"
#include "CommonTools/UtilAlgos/interface/PtMinSelector.h"
#include "CommonTools/UtilAlgos/interface/EtaRangeSelector.h"
#include "CommonTools/UtilAlgos/interface/AndSelector.h"
#include "DataFormats/Candidate/interface/Candidate.h"

typedef SingleObjectSelector<
   edm::View<reco::Candidate>,
   AndSelector<PtMinSelector,EtaRangeSelector>
   >
EtaPtMinCandViewRefSelector;

DEFINE_FWK_MODULE(EtaPtMinCandViewRefSelector);
