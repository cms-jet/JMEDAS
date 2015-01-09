import FWCore.ParameterSet.Config as cms

convertedPackedPFCandidates = cms.EDProducer('convertPackedCandToRecoCand',
       								     	  src = cms.InputTag('packedPFCandidates')
            							  	)