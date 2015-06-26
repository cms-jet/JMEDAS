import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Configuration.JetCorrectionProducersAllAlgos_cff import *
from JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff import *
from JetMETCorrections.Configuration.DefaultJEC_cff import *

#
# FIX RHO INPUT COLLECTION FOR CALO L1FAST CORRECTORS (CALO NOT PF)
#
ak4CaloL1Fastjet.srcRho = 'kt6CaloJets:rho'
ak7CaloL1Fastjet.srcRho = 'kt6CaloJets:rho'
kt4CaloL1Fastjet.srcRho = 'kt6CaloJets:rho'
kt6CaloL1Fastjet.srcRho = 'kt6CaloJets:rho'

#
# L1OFFSET JEC PRODUCERS NOT DEFINED IN DEFAULTJEC_CFF
#
ak4CaloJetsL1Off = cms.EDProducer(
	    'CaloJetCorrectionProducer',
		    src         = cms.InputTag('ak4CaloJets'),
		    correctors  = cms.vstring('ak4CaloL1Offset')
		    )
ak7CaloJetsL1Off = ak4CaloJetsL1Off.clone(src='ak7CaloJets', correctors=['ak7CaloL1Offset'])
ak5CaloJetsL2L3   = cms.EDProducer('PFJetCorrectionProducer',
    src         = cms.InputTag('ak5CaloJets'),
    correctors  = cms.vstring('ak5CaloL2L3')
    )
ak5CaloJetsL1L2L3 = ak5CaloJetsL2L3.clone(src = 'ak5CaloJets', correctors = ['ak5CaloL1L2L3'])
ak7CaloJetsL1L2L3 = ak5CaloJetsL2L3.clone(src = 'ak7CaloJets', correctors = ['ak7CaloL1L2L3'])

ak5PFJetsL1Off = cms.EDProducer(
	    'PFJetCorrectionProducer',
		    src         = cms.InputTag('ak5PFJets'),
		    correctors  = cms.vstring('ak5PFL1Offset')
		    )
ak7PFJetsL1Off = ak5PFJetsL1Off.clone(src='ak7PFJets', correctors=['ak7PFL1Offset'])
ak5PFJetsL2L3   = cms.EDProducer('PFJetCorrectionProducer',
    src         = cms.InputTag('ak5PFJets'),
    correctors  = cms.vstring('ak5PFL2L3')
    )
ak5PFJetsL1L2L3 = ak5PFJetsL2L3.clone(src = 'ak5PFJets', correctors = ['ak5PFL1L2L3'])
ak7PFJetsL1L2L3 = ak5PFJetsL2L3.clone(src = 'ak7PFJets', correctors = ['ak7PFL1L2L3'])

ak5JPTJetsL1Off  = cms.EDProducer(
    'JPTJetCorrectionProducer',
    src         = cms.InputTag('ak5JPTJets'),
    correctors  = cms.vstring('ak5L1JPTOffset')
    )
ak7JPTJetsL1Off = ak5JPTJetsL1Off.clone(src='ak7JPTJets', correctors=['ak7L1JPTOffset'])


#
# L1FAST JEC PRODUCERS NOT DEFINED IN DEFAULTJEC_CFF
#

#ak5PFL1FastL2L3 = ak4PFL2L3.clone()
#ak5PFL1FastL2L3.correctors.insert(0,'ak5PFL1Fastjet')
#ak5PFJetsL1FastL2L3 = ak4PFJetsL1L2L3.clone(src = 'ak5PFJets', correctors=['ak5PFL1FastL2L3'])

ak5JPTJetsL1Fast = cms.EDProducer(
	'JPTJetCorrectionProducer',
	src         = cms.InputTag('ak5JPTJets'),
	correctors  = cms.vstring('ak5JPTL1Fastjet')
	)
ak7JPTJetsL1Fast = ak5JPTJetsL1Fast.clone(src='ak5JPTJets', correctors=['ak5JPTL1Fastjet'])


#
# L2 AND L3 ESPRODUCERS FOR JPT
#
ak7JPTL2Relative = ak7CaloL2Relative.clone( algorithm = 'AK7JPT' )
ak7JPTL3Absolute = ak7CaloL3Absolute.clone( algorithm = 'AK7JPT' )


#
# PFchs JEC PRODUCERS NOT DEFINED IN DEFAULTJEC_CFF
#

#ak5PFchsJetsL1Off = cms.EDProducer(
#    'PFJetCorrectionProducer',
#    src         = cms.InputTag('ak5PFchsJets'),
#    correctors  = cms.vstring('ak5PFchsL1Offset')
#    )
#ak7PFchsJetsL1Off = ak5PFchsJetsL1Off.clone(src='ak7PFchsJets', correctors=['ak7PFchsL1Offset'])
#
#ak5PFchsJetsL1L2L3 = ak5PFchsJetsL2L3.clone(src = 'ak5PFchsJets', correctors = ['ak5PFchsL1L2L3'])
#ak7PFchsJetsL1L2L3 = ak5PFchsJetsL2L3.clone(src = 'ak7PFchsJets', correctors = ['ak7PFchsL1L2L3'])
#
#ak5PFchsL1Offset = ak5PFL1Offset.clone(algorithm = 'AK5PFchs')
#ak7PFchsL1Offset = ak5PFchsL1Offset.clone()
#


#
# HLT JEC PRODUCERS NOT DEFINED IN DEFAULTJEC_CFF
#
ak5CaloHLTL1Offset = ak4CaloL1Offset.clone(algorithm = 'AK5CaloHLT')
ak5CaloHLTL1Fastjet = cms.ESProducer(
    'L1FastjetCorrectionESProducer',
    era         = cms.string('Summer11'),
    level       = cms.string('L1FastJet'),
    algorithm   = cms.string('AK5CaloHLT'),
    section     = cms.string(''),
    srcRho      = cms.InputTag('hltKT6CaloJets','rho'),
    useCondDB = cms.untracked.bool(True)
    )
ak5CaloHLTL2Relative = ak4CaloL2Relative.clone( algorithm = 'AK5CaloHLT' )
ak5CaloHLTL3Absolute     = ak4CaloL3Absolute.clone( algorithm = 'AK5CaloHLT' )
ak5CaloHLTL2L3 = cms.ESProducer(
    'JetCorrectionESChain',
    correctors = cms.vstring('ak5CaloHLTL2Relative','ak5CaloHLTL3Absolute')
    )
ak5CaloHLTL1L2L3 = cms.ESProducer(
    'JetCorrectionESChain',
    correctors = cms.vstring('ak5CaloHLTL1Offset','ak5CaloHLTL2Relative','ak5CaloHLTL3Absolute')
    )
ak5CaloHLTL1FastL2L3 = ak5CaloHLTL2L3.clone()
ak5CaloHLTL1FastL2L3.correctors.insert(0,'ak5CaloHLTL1Fastjet')
ak5CaloHLTJetsL1Fast = cms.EDProducer(
    'CaloJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5CaloJets'),#'ak5CaloHLTJets'),
    correctors  = cms.vstring('ak5CaloHLTL1Fastjet')
    )
ak5CaloHLTJetsL1Off = cms.EDProducer(
    'PFJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5CaloJets'),#'ak5CaloHLTJets'),
    correctors  = cms.vstring('ak5CaloHLTL1Offset')
    )
ak5CaloHLTJetsL2L3   = cms.EDProducer('PFJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5CaloJets'),#'ak5CaloHLTJets'),
    correctors  = cms.vstring('ak5CaloHLTL2L3')
    )
ak5CaloHLTJetsL1FastL2L3 = ak5CaloHLTJetsL2L3.clone(src = 'hltAntiKT5CaloJets', correctors = ['ak5CaloHLTL1FastL2L3'])
ak5CaloHLTJetsL1L2L3 = ak5CaloHLTJetsL2L3.clone(src = 'hltAntiKT5CaloJets', correctors = ['ak5CaloHLTL1L2L3'])


ak5PFHLTL1Offset = ak4CaloL1Offset.clone(algorithm = 'AK5PFHLT')
ak5PFHLTL1Fastjet = cms.ESProducer(
    'L1FastjetCorrectionESProducer',
    era         = cms.string('Summer11'),
    level       = cms.string('L1FastJet'),
    algorithm   = cms.string('AK5PFHLT'),
    section     = cms.string(''),
    srcRho      = cms.InputTag('hltKT6PFJets','rho'),
    useCondDB = cms.untracked.bool(True)
     )
ak5PFHLTL2Relative = ak4CaloL2Relative.clone( algorithm = 'AK5PFHLT' )
ak5PFHLTL3Absolute     = ak4CaloL3Absolute.clone( algorithm = 'AK5PFHLT' )
ak5PFHLTL2L3 = cms.ESProducer(
    'JetCorrectionESChain',
    correctors = cms.vstring('ak5PFHLTL2Relative','ak5PFHLTL3Absolute')
    )
ak5PFHLTL1L2L3 = cms.ESProducer(
    'JetCorrectionESChain',
    correctors = cms.vstring('ak5PFHLTL1Offset','ak5PFHLTL2Relative','ak5PFHLTL3Absolute')
    )
ak5PFHLTL1FastL2L3 = ak5PFHLTL2L3.clone()
ak5PFHLTL1FastL2L3.correctors.insert(0,'ak5PFHLTL1Fastjet')
ak5PFHLTJetsL1Fast = cms.EDProducer(
    'PFJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5PFJets'),#'ak5PFHLTJets'),
    correctors  = cms.vstring('ak5PFHLTL1Fastjet')
    )
ak5PFHLTJetsL1Off = cms.EDProducer(
    'PFJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5PFJets'),#'ak5PFHLTJets'),
    correctors  = cms.vstring('ak5PFHLTL1Offset')
    )
ak5PFHLTJetsL2L3   = cms.EDProducer('PFJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5PFJets'),#'ak5PFHLTJets'),
    correctors  = cms.vstring('ak5PFHLTL2L3')
    )
ak5PFHLTJetsL1FastL2L3 = ak5PFHLTJetsL2L3.clone(src = 'hltAntiKT5PFJets', correctors = ['ak5PFHLTL1FastL2L3'])
ak5PFHLTJetsL1L2L3 = ak5PFHLTJetsL2L3.clone(src = 'hltAntiKT5PFJets', correctors = ['ak5PFHLTL1L2L3'])


ak5PFchsHLTL1Offset = ak4CaloL1Offset.clone(algorithm = 'AK5PFchsHLT')
ak5PFchsHLTL1Fastjet = cms.ESProducer(
    'L1FastjetCorrectionESProducer',
    era         = cms.string('Summer11'),
    level       = cms.string('L1FastJet'),
    algorithm   = cms.string('AK5PFchsHLT'),
    section     = cms.string(''),
    srcRho      = cms.InputTag('hltKT6PFJets','rho'),
    useCondDB = cms.untracked.bool(True)
     )
ak5PFchsHLTL2Relative = ak4CaloL2Relative.clone( algorithm = 'AK5PFchsHLT' )
ak5PFchsHLTL3Absolute     = ak4CaloL3Absolute.clone( algorithm = 'AK5PFchsHLT' )
ak5PFchsHLTL2L3 = cms.ESProducer(
    'JetCorrectionESChain',
    correctors = cms.vstring('ak5PFchsHLTL2Relative','ak5PFchsHLTL3Absolute')
    )
ak5PFchsHLTL1L2L3 = cms.ESProducer(
    'JetCorrectionESChain',
    correctors = cms.vstring('ak5PFchsHLTL1Offset','ak5PFchsHLTL2Relative','ak5PFchsHLTL3Absolute')
    )
ak5PFchsHLTL1FastL2L3 = ak5PFchsHLTL2L3.clone()
ak5PFchsHLTL1FastL2L3.correctors.insert(0,'ak5PFchsHLTL1Fastjet')
ak5PFchsHLTJetsL1Fast = cms.EDProducer(
    'PFJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5PFJetsNoPUPixelVert'),
    correctors  = cms.vstring('ak5PFchsHLTL1Fastjet')
    )
ak5PFchsHLTJetsL1Off = cms.EDProducer(
    'PFJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5PFJetsNoPUPixelVert'),
    correctors  = cms.vstring('ak5PFchsHLTL1Offset')
    )
ak5PFchsHLTJetsL2L3   = cms.EDProducer('PFJetCorrectionProducer',
    src         = cms.InputTag('hltAntiKT5PFJetsNoPUPixelVert'),
    correctors  = cms.vstring('ak5PFchsHLTL2L3')
    )
ak5PFchsHLTJetsL1FastL2L3 = ak5PFchsHLTJetsL2L3.clone(src = 'hltAntiKT5PFJetsNoPUPixelVert', correctors = ['ak5PFchsHLTL1FastL2L3'])
ak5PFchsHLTJetsL1L2L3 = ak5PFchsHLTJetsL2L3.clone(src = 'hltAntiKT5PFJetsNoPUPixelVert', correctors = ['ak5PFchsHLTL1L2L3'])


#
# PUPPI JEC PRODUCERS NOT DEFINED IN DEFAULTJEC_CFF
#
ak1PUPPIL1Fastjet = cms.ESProducer(
    'L1FastjetCorrectionESProducer',
    era         = cms.string('Summer11'),
    level       = cms.string('L1FastJet'),
    algorithm   = cms.string('AK1PUPPI'),
    section     = cms.string(''),
    srcRho      = cms.InputTag('kt6PFJets','rho'),
    useCondDB = cms.untracked.bool(True)
    )
ak2PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK2PUPPI' )
ak3PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK3PUPPI' )
ak4PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK4PUPPI' )
ak5PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK5PUPPI' )
ak6PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK6PUPPI' )
ak7PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK7PUPPI' )
ak8PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK8PUPPI' )
ak9PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK9PUPPI' )
ak10PUPPIL1Fastjet = ak1PUPPIL1Fastjet.clone( algorithm = 'AK10PUPPI' )

ak1PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK1PUPPI' )
ak2PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK2PUPPI' )
ak3PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK3PUPPI' )
ak4PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK4PUPPI' )
ak5PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK5PUPPI' )
ak6PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK6PUPPI' )
ak7PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK7PUPPI' )
ak8PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK8PUPPI' )
ak9PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK9PUPPI' )
ak10PUPPIL2Relative = ak4PFL2Relative.clone( algorithm = 'AK10PUPPI' )

ak1PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK1PUPPI' )
ak2PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK2PUPPI' )
ak3PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK3PUPPI' )
ak4PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK4PUPPI' )
ak5PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK5PUPPI' )
ak6PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK6PUPPI' )
ak7PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK7PUPPI' )
ak8PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK8PUPPI' )
ak9PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK9PUPPI' )
ak10PUPPIL3Absolute = ak4PFL3Absolute.clone( algorithm = 'AK10PUPPI' )

ak1PUPPIL2L3 = cms.ESProducer(
    'JetCorrectionESChain',
    correctors = cms.vstring('ak1PUPPIL2Relative','ak1PUPPIL3Absolute')
    )
ak2PUPPIL2L3  = ak1PUPPIL2L3.clone( correctors=['ak2PUPPIL2Relative','ak2PUPPIL3Absolute'] )
ak3PUPPIL2L3  = ak1PUPPIL2L3.clone( correctors=['ak3PUPPIL2Relative','ak3PUPPIL3Absolute'] )
ak4PUPPIL2L3  = ak1PUPPIL2L3.clone( correctors=['ak4PUPPIL2Relative','ak4PUPPIL3Absolute'] )
ak5PUPPIL2L3  = ak1PUPPIL2L3.clone( correctors=['ak5PUPPIL2Relative','ak5PUPPIL3Absolute'] )
ak6PUPPIL2L3  = ak1PUPPIL2L3.clone( correctors=['ak6PUPPIL2Relative','ak6PUPPIL3Absolute'] )
ak7PUPPIL2L3  = ak1PUPPIL2L3.clone( correctors=['ak7PUPPIL2Relative','ak7PUPPIL3Absolute'] )
ak8PUPPIL2L3  = ak1PUPPIL2L3.clone( correctors=['ak8PUPPIL2Relative','ak8PUPPIL3Absolute'] )
ak9PUPPIL2L3  = ak1PUPPIL2L3.clone( correctors=['ak9PUPPIL2Relative','ak9PUPPIL3Absolute'] )
ak10PUPPIL2L3 = ak1PUPPIL2L3.clone( correctors=['ak10PUPPIL2Relative','ak10PUPPIL3Absolute'] )

ak1PUPPIL1FastL2L3 = ak1PUPPIL2L3.clone()
ak1PUPPIL1FastL2L3.correctors.insert(0,'ak1PUPPIL1Fastjet')
ak2PUPPIL1FastL2L3 = ak2PUPPIL2L3.clone()
ak2PUPPIL1FastL2L3.correctors.insert(0,'ak2PUPPIL1Fastjet')
ak3PUPPIL1FastL2L3 = ak3PUPPIL2L3.clone()
ak3PUPPIL1FastL2L3.correctors.insert(0,'ak3PUPPIL1Fastjet')
ak4PUPPIL1FastL2L3 = ak4PUPPIL2L3.clone()
ak4PUPPIL1FastL2L3.correctors.insert(0,'ak4PUPPIL1Fastjet')
ak5PUPPIL1FastL2L3 = ak5PUPPIL2L3.clone()
ak5PUPPIL1FastL2L3.correctors.insert(0,'ak5PUPPIL1Fastjet')
ak6PUPPIL1FastL2L3 = ak6PUPPIL2L3.clone()
ak6PUPPIL1FastL2L3.correctors.insert(0,'ak6PUPPIL1Fastjet')
ak7PUPPIL1FastL2L3 = ak7PUPPIL2L3.clone()
ak7PUPPIL1FastL2L3.correctors.insert(0,'ak7PUPPIL1Fastjet')
ak8PUPPIL1FastL2L3 = ak8PUPPIL2L3.clone()
ak8PUPPIL1FastL2L3.correctors.insert(0,'ak8PUPPIL1Fastjet')
ak9PUPPIL1FastL2L3 = ak9PUPPIL2L3.clone()
ak9PUPPIL1FastL2L3.correctors.insert(0,'ak9PUPPIL1Fastjet')
ak10PUPPIL1FastL2L3 = ak10PUPPIL2L3.clone()
ak10PUPPIL1FastL2L3.correctors.insert(0,'ak10PUPPIL1Fastjet')

ak1PFJetsPuppiL1Fast = cms.EDProducer(
    'PFJetCorrectionProducer',
    src         = cms.InputTag('ak1PFJetsPuppi'),
    correctors  = cms.vstring('ak1PUPPIL1Fastjet')
    )
ak2PFJetsPuppiL1Fast  = ak1PFJetsPuppiL1Fast.clone(src='ak2PFJetsPuppi', correctors=['ak2PUPPIL1Fastjet'])
ak3PFJetsPuppiL1Fast  = ak1PFJetsPuppiL1Fast.clone(src='ak3PFJetsPuppi', correctors=['ak3PUPPIL1Fastjet'])
ak4PFJetsPuppiL1Fast  = ak1PFJetsPuppiL1Fast.clone(src='ak4PFJetsPuppi', correctors=['ak4PUPPIL1Fastjet'])
ak5PFJetsPuppiL1Fast  = ak1PFJetsPuppiL1Fast.clone(src='ak4PFJetsPuppi', correctors=['ak4PUPPIL1Fastjet'])
ak6PFJetsPuppiL1Fast  = ak1PFJetsPuppiL1Fast.clone(src='ak6PFJetsPuppi', correctors=['ak6PUPPIL1Fastjet'])
ak7PFJetsPuppiL1Fast  = ak1PFJetsPuppiL1Fast.clone(src='ak8PFJetsPuppi', correctors=['ak8PUPPIL1Fastjet'])
ak8PFJetsPuppiL1Fast  = ak1PFJetsPuppiL1Fast.clone(src='ak8PFJetsPuppi', correctors=['ak8PUPPIL1Fastjet'])
ak9PFJetsPuppiL1Fast  = ak1PFJetsPuppiL1Fast.clone(src='ak9PFJetsPuppi', correctors=['ak9PUPPIL1Fastjet'])
ak10PFJetsPuppiL1Fast = ak1PFJetsPuppiL1Fast.clone(src='ak10PFJetsPuppi', correctors=['ak10PUPPIL1Fastjet'])

ak1PFJetsPuppiL2L3 = cms.EDProducer('PFJetCorrectionProducer',
    src         = cms.InputTag('ak1PFJetsPuppi'),
    correctors  = cms.vstring('ak1PUPPIL2L3')
    )
ak2PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak2PFJetsPuppi', correctors = ['ak2PUPPIL2L3'])
ak3PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak3PFJetsPuppi', correctors = ['ak3PUPPIL2L3'])
ak4PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak4PFJetsPuppi', correctors = ['ak4PUPPIL2L3'])
ak5PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak5PFJetsPuppi', correctors = ['ak5PUPPIL2L3'])
ak6PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak6PFJetsPuppi', correctors = ['ak6PUPPIL2L3'])
ak7PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak7PFJetsPuppi', correctors = ['ak7PUPPIL2L3'])
ak8PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak8PFJetsPuppi', correctors = ['ak8PUPPIL2L3'])
ak9PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak9PFJetsPuppi', correctors = ['ak9PUPPIL2L3'])
ak10PFJetsPuppiL2L3 = ak1PFJetsPuppiL2L3.clone(src = 'ak10PFJetsPuppi', correctors = ['ak10PUPPIL2L3'])

ak1PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak1PFJetsPuppi', correctors = ['ak1PUPPIL1FastL2L3'])
ak2PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak2PFJetsPuppi', correctors = ['ak2PUPPIL1FastL2L3'])
ak3PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak3PFJetsPuppi', correctors = ['ak3PUPPIL1FastL2L3'])
ak4PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak4PFJetsPuppi', correctors = ['ak4PUPPIL1FastL2L3'])
ak5PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak5PFJetsPuppi', correctors = ['ak5PUPPIL1FastL2L3'])
ak6PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak6PFJetsPuppi', correctors = ['ak6PUPPIL1FastL2L3'])
ak7PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak7PFJetsPuppi', correctors = ['ak7PUPPIL1FastL2L3'])
ak8PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak8PFJetsPuppi', correctors = ['ak8PUPPIL1FastL2L3'])
ak9PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak9PFJetsPuppi', correctors = ['ak9PUPPIL1FastL2L3'])
ak10PFJetsPuppiL1FastL2L3 = ak1PFJetsPuppiL2L3.clone(src = 'ak10PFJetsPuppi', correctors = ['ak10PUPPIL1FastL2L3'])
