import FWCore.ParameterSet.Config as cms

from JetMETCorrections.Configuration.JetCorrectionServicesAllAlgos_cff import *
from JetMETCorrections.Configuration.CorrectedJetProducersAllAlgos_cff import *
from JetMETCorrections.Configuration.CorrectedJetProducersDefault_cff import *
from JetMETCorrections.Configuration.CorrectedJetProducers_cff import *
from JetMETCorrections.Configuration.JetCorrectors_cff import *
from JetMETCorrections.Configuration.JetCorrectorsAllAlgos_cff import *

#
# PF JEC PRODUCERS NOT DEFINED in DEFAULTJEC_CFF
#
ak8PFL1FastL2L3Corrector = ak8PFL2L3Corrector.clone()
ak8PFL1FastL2L3Corrector.correctors.insert(0,'ak8PFL1FastjetCorrector')
ak8PFL1FastL2L3CorrectorChain = cms.Sequence(
    ak8PFL1FastjetCorrector * ak8PFL2RelativeCorrector * ak8PFL3AbsoluteCorrector * ak8PFL1FastL2L3Corrector
)
ak8PFL1FastL2L3 = ak8PFL2L3.clone()
ak8PFL1FastL2L3.correctors.insert(0,'ak8PFL1Fastjet')


#
# PFCHS JEC PRODUCERS NOT DEFINED IN DEFAULTJEC_CFF
#
ak8PFCHSL1FastL2L3Corrector = ak8PFL2L3Corrector.clone()
ak8PFCHSL1FastL2L3Corrector.correctors.insert(0,'ak8PFCHSL1FastjetCorrector')
ak8PFCHSL1FastL2L3CorrectorChain = cms.Sequence(
    ak8PFCHSL1FastjetCorrector * ak8PFCHSL2RelativeCorrector * ak8PFCHSL3AbsoluteCorrector * ak8PFCHSL1FastL2L3Corrector
)
ak8PFCHSL1FastL2L3 = ak8PFL2L3.clone()
ak8PFCHSL1FastL2L3.correctors.insert(0,'ak8PFCHSL1Fastjet')

ak1PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak1PFJetsCHS', correctors = ['ak1PFCHSL1FastL2L3Corrector'])
ak2PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak2PFJetsCHS', correctors = ['ak2PFCHSL1FastL2L3Corrector'])
ak3PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak3PFJetsCHS', correctors = ['ak3PFCHSL1FastL2L3Corrector'])
ak4PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak4PFJetsCHS', correctors = ['ak4PFCHSL1FastL2L3Corrector'])
ak5PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak5PFJetsCHS', correctors = ['ak5PFCHSL1FastL2L3Corrector'])
ak6PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak6PFJetsCHS', correctors = ['ak6PFCHSL1FastL2L3Corrector'])
ak7PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak7PFJetsCHS', correctors = ['ak7PFCHSL1FastL2L3Corrector'])
ak8PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak8PFJetsCHS', correctors = ['ak8PFCHSL1FastL2L3Corrector'])
ak9PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak9PFJetsCHS', correctors = ['ak9PFCHSL1FastL2L3Corrector'])
ak10PFJetsCHSL1FastL2L3 = ak4PFCHSJetsL2L3.clone(src = 'ak10PFJetsCHS', correctors = ['ak10PFCHSL1FastL2L3Corrector'])

#
# PUPPI JEC PRODUCERS NOT DEFINED IN DEFAULTJEC_CFF
#
ak1PUPPIL1Fastjet = cms.ESProducer(
    'L1FastjetCorrectionESProducer',
    #era         = cms.string('Summer11'),
    level       = cms.string('L1FastJet'),
    algorithm   = cms.string('AK1PFPuppi'),
    #section     = cms.string(''),
    srcRho      = cms.InputTag('fixedGridRhoFastjetAll'),
    #useCondDB = cms.untracked.bool(True)
    )
ak2PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK2PFPuppi' )
ak3PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK3PFPuppi' )
ak4PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK4PFPuppi' )
ak5PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK5PFPuppi' )
ak6PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK6PFPuppi' )
ak7PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK7PFPuppi' )
ak8PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK8PFPuppi' )
ak9PUPPIL1Fastjet  = ak1PUPPIL1Fastjet.clone( algorithm = 'AK9PFPuppi' )
ak10PUPPIL1Fastjet = ak1PUPPIL1Fastjet.clone( algorithm = 'AK10PFPuppi' )

ak1PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK1PFPuppi' )
ak2PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK2PFPuppi' )
ak3PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK3PFPuppi' )
ak4PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK4PFPuppi' )
ak5PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK5PFPuppi' )
ak6PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK6PFPuppi' )
ak7PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK7PFPuppi' )
ak8PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK8PFPuppi' )
ak9PUPPIL2Relative  = ak4PFL2Relative.clone( algorithm = 'AK9PFPuppi' )
ak10PUPPIL2Relative = ak4PFL2Relative.clone( algorithm = 'AK10PFPuppi' )

ak1PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK1PFPuppi' )
ak2PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK2PFPuppi' )
ak3PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK3PFPuppi' )
ak4PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK4PFPuppi' )
ak5PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK5PFPuppi' )
ak6PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK6PFPuppi' )
ak7PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK7PFPuppi' )
ak8PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK8PFPuppi' )
ak9PUPPIL3Absolute  = ak4PFL3Absolute.clone( algorithm = 'AK9PFPuppi' )
ak10PUPPIL3Absolute = ak4PFL3Absolute.clone( algorithm = 'AK10PFPuppi' )

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

ak4PUPPIL1FastjetCorrector = cms.EDProducer(
    'L1FastjetCorrectorProducer',
    level       = cms.string('L1FastJet'),
    algorithm   = cms.string('AK4PFPuppi'),
    srcRho      = cms.InputTag( 'fixedGridRhoFastjetAll' )
    )
ak1PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK1PFPuppi' )
ak2PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK2PFPuppi' )
ak3PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK3PFPuppi' )
ak5PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK5PFPuppi' )
ak6PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK6PFPuppi' )
ak7PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK7PFPuppi' )
ak8PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK8PFPuppi' )
ak9PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK9PFPuppi' )
ak10PUPPIL1FastjetCorrector = ak4PUPPIL1FastjetCorrector.clone( algorithm = 'AK10PFPuppi' )

ak1PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK1PFPuppi' )
ak2PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK2PFPuppi' )
ak3PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK3PFPuppi' )
ak4PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK4PFPuppi' )
ak5PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK5PFPuppi' )
ak6PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK6PFPuppi' )
ak7PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK7PFPuppi' )
ak8PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK8PFPuppi' )
ak9PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK9PFPuppi' )
ak10PUPPIL2RelativeCorrector = ak4CaloL2RelativeCorrector.clone( algorithm = 'AK10PFPuppi' )

ak1PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK1PFPuppi' )
ak2PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK2PFPuppi' )
ak3PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK3PFPuppi' )
ak4PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK4PFPuppi' )
ak5PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK5PFPuppi' )
ak6PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK6PFPuppi' )
ak7PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK7PFPuppi' )
ak8PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK8PFPuppi' )
ak9PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK9PFPuppi' )
ak10PUPPIL3AbsoluteCorrector = ak4CaloL3AbsoluteCorrector.clone( algorithm = 'AK10PFPuppi' )

ak4PUPPIL2L3Corrector = cms.EDProducer(
    'ChainedJetCorrectorProducer',
    correctors = cms.VInputTag('ak4PUPPIL2RelativeCorrector','ak4PUPPIL3AbsoluteCorrector')
    )
ak1PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak1PUPPIL2RelativeCorrector','ak1PUPPIL3AbsoluteCorrector'])
ak2PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak2PUPPIL2RelativeCorrector','ak2PUPPIL3AbsoluteCorrector'])
ak3PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak3PUPPIL2RelativeCorrector','ak3PUPPIL3AbsoluteCorrector'])
ak5PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak5PUPPIL2RelativeCorrector','ak5PUPPIL3AbsoluteCorrector'])
ak6PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak6PUPPIL2RelativeCorrector','ak6PUPPIL3AbsoluteCorrector'])
ak7PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak7PUPPIL2RelativeCorrector','ak7PUPPIL3AbsoluteCorrector'])
ak8PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak8PUPPIL2RelativeCorrector','ak8PUPPIL3AbsoluteCorrector'])
ak9PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak9PUPPIL2RelativeCorrector','ak9PUPPIL3AbsoluteCorrector'])
ak10PUPPIL2L3Corrector = ak4PUPPIL2L3Corrector.clone( correctors = ['ak10PUPPIL2RelativeCorrector','ak10PUPPIL3AbsoluteCorrector'])

ak1PUPPIL1FastL2L3Corrector = ak1PUPPIL2L3Corrector.clone()
ak1PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak1PUPPIL1FastjetCorrector')
ak2PUPPIL1FastL2L3Corrector = ak2PUPPIL2L3Corrector.clone()
ak2PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak2PUPPIL1FastjetCorrector')
ak3PUPPIL1FastL2L3Corrector = ak3PUPPIL2L3Corrector.clone()
ak3PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak3PUPPIL1FastjetCorrector')
ak4PUPPIL1FastL2L3Corrector = ak4PUPPIL2L3Corrector.clone()
ak4PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak4PUPPIL1FastjetCorrector')
ak5PUPPIL1FastL2L3Corrector = ak5PUPPIL2L3Corrector.clone()
ak5PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak5PUPPIL1FastjetCorrector')
ak6PUPPIL1FastL2L3Corrector = ak6PUPPIL2L3Corrector.clone()
ak6PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak6PUPPIL1FastjetCorrector')
ak7PUPPIL1FastL2L3Corrector = ak7PUPPIL2L3Corrector.clone()
ak7PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak7PUPPIL1FastjetCorrector')
ak8PUPPIL1FastL2L3Corrector = ak8PUPPIL2L3Corrector.clone()
ak8PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak8PUPPIL1FastjetCorrector')
ak9PUPPIL1FastL2L3Corrector = ak9PUPPIL2L3Corrector.clone()
ak9PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak9PUPPIL1FastjetCorrector')
ak10PUPPIL1FastL2L3Corrector = ak10PUPPIL2L3Corrector.clone()
ak10PUPPIL1FastL2L3Corrector.correctors.insert(0,'ak10PUPPIL1FastjetCorrector')

ak1PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak1PUPPIL1FastjetCorrector * ak1PUPPIL2RelativeCorrector * ak1PUPPIL3AbsoluteCorrector * ak1PUPPIL1FastL2L3Corrector
)
ak2PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak2PUPPIL1FastjetCorrector * ak2PUPPIL2RelativeCorrector * ak2PUPPIL3AbsoluteCorrector * ak2PUPPIL1FastL2L3Corrector
)
ak3PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak3PUPPIL1FastjetCorrector * ak3PUPPIL2RelativeCorrector * ak3PUPPIL3AbsoluteCorrector * ak3PUPPIL1FastL2L3Corrector
)
ak4PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak4PUPPIL1FastjetCorrector * ak4PUPPIL2RelativeCorrector * ak4PUPPIL3AbsoluteCorrector * ak4PUPPIL1FastL2L3Corrector
)
ak5PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak5PUPPIL1FastjetCorrector * ak5PUPPIL2RelativeCorrector * ak5PUPPIL3AbsoluteCorrector * ak5PUPPIL1FastL2L3Corrector
)
ak6PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak6PUPPIL1FastjetCorrector * ak6PUPPIL2RelativeCorrector * ak6PUPPIL3AbsoluteCorrector * ak6PUPPIL1FastL2L3Corrector
)
ak7PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak7PUPPIL1FastjetCorrector * ak7PUPPIL2RelativeCorrector * ak7PUPPIL3AbsoluteCorrector * ak7PUPPIL1FastL2L3Corrector
)
ak8PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak8PUPPIL1FastjetCorrector * ak8PUPPIL2RelativeCorrector * ak8PUPPIL3AbsoluteCorrector * ak8PUPPIL1FastL2L3Corrector
)
ak9PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak9PUPPIL1FastjetCorrector * ak9PUPPIL2RelativeCorrector * ak9PUPPIL3AbsoluteCorrector * ak9PUPPIL1FastL2L3Corrector
)
ak10PUPPIL1FastL2L3CorrectorChain = cms.Sequence(
    ak10PUPPIL1FastjetCorrector * ak10PUPPIL2RelativeCorrector * ak10PUPPIL3AbsoluteCorrector * ak10PUPPIL1FastL2L3Corrector
)

ak1PFJetsPuppiL1 = cms.EDProducer(
    'CorrectedPFJetProducer',
    src         = cms.InputTag('ak1PFJetsPuppi'),
    correctors  = cms.VInputTag('ak1PUPPIL1FastjetCorrector')
    )
ak2PFJetsPuppiL1  = ak1PFJetsPuppiL1.clone(src='ak2PFJetsPuppi', correctors=['ak2PUPPIL1FastjetCorrector'])
ak3PFJetsPuppiL1  = ak1PFJetsPuppiL1.clone(src='ak3PFJetsPuppi', correctors=['ak3PUPPIL1FastjetCorrector'])
ak4PFJetsPuppiL1  = ak1PFJetsPuppiL1.clone(src='ak4PFJetsPuppi', correctors=['ak4PUPPIL1FastjetCorrector'])
ak5PFJetsPuppiL1  = ak1PFJetsPuppiL1.clone(src='ak4PFJetsPuppi', correctors=['ak4PUPPIL1FastjetCorrector'])
ak6PFJetsPuppiL1  = ak1PFJetsPuppiL1.clone(src='ak6PFJetsPuppi', correctors=['ak6PUPPIL1FastjetCorrector'])
ak7PFJetsPuppiL1  = ak1PFJetsPuppiL1.clone(src='ak8PFJetsPuppi', correctors=['ak8PUPPIL1FastjetCorrector'])
ak8PFJetsPuppiL1  = ak1PFJetsPuppiL1.clone(src='ak8PFJetsPuppi', correctors=['ak8PUPPIL1FastjetCorrector'])
ak9PFJetsPuppiL1  = ak1PFJetsPuppiL1.clone(src='ak9PFJetsPuppi', correctors=['ak9PUPPIL1FastjetCorrector'])
ak10PFJetsPuppiL1 = ak1PFJetsPuppiL1.clone(src='ak10PFJetsPuppi', correctors=['ak10PUPPIL1FastjetCorrector'])

ak1PFJetsPuppiL2L3 = cms.EDProducer('CorrectedPFJetProducer',
    src         = cms.InputTag('ak1PFJetsPuppi'),
    correctors  = cms.VInputTag('ak1PUPPIL2L3Corrector')
    )
ak2PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak2PFJetsPuppi', correctors = ['ak2PUPPIL2L3Corrector'])
ak3PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak3PFJetsPuppi', correctors = ['ak3PUPPIL2L3Corrector'])
ak4PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak4PFJetsPuppi', correctors = ['ak4PUPPIL2L3Corrector'])
ak5PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak5PFJetsPuppi', correctors = ['ak5PUPPIL2L3Corrector'])
ak6PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak6PFJetsPuppi', correctors = ['ak6PUPPIL2L3Corrector'])
ak7PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak7PFJetsPuppi', correctors = ['ak7PUPPIL2L3Corrector'])
ak8PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak8PFJetsPuppi', correctors = ['ak8PUPPIL2L3Corrector'])
ak9PFJetsPuppiL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak9PFJetsPuppi', correctors = ['ak9PUPPIL2L3Corrector'])
ak10PFJetsPuppiL2L3 = ak1PFJetsPuppiL2L3.clone(src = 'ak10PFJetsPuppi', correctors = ['ak10PUPPIL2L3Corrector'])

ak1PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak1PFJetsPuppi', correctors = ['ak1PUPPIL1FastL2L3Corrector'])
ak2PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak2PFJetsPuppi', correctors = ['ak2PUPPIL1FastL2L3Corrector'])
ak3PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak3PFJetsPuppi', correctors = ['ak3PUPPIL1FastL2L3Corrector'])
ak4PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak4PFJetsPuppi', correctors = ['ak4PUPPIL1FastL2L3Corrector'])
ak5PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak5PFJetsPuppi', correctors = ['ak5PUPPIL1FastL2L3Corrector'])
ak6PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak6PFJetsPuppi', correctors = ['ak6PUPPIL1FastL2L3Corrector'])
ak7PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak7PFJetsPuppi', correctors = ['ak7PUPPIL1FastL2L3Corrector'])
ak8PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak8PFJetsPuppi', correctors = ['ak8PUPPIL1FastL2L3Corrector'])
ak9PFJetsPuppiL1FastL2L3  = ak1PFJetsPuppiL2L3.clone(src = 'ak9PFJetsPuppi', correctors = ['ak9PUPPIL1FastL2L3Corrector'])
ak10PFJetsPuppiL1FastL2L3 = ak1PFJetsPuppiL2L3.clone(src = 'ak10PFJetsPuppi', correctors = ['ak10PUPPIL1FastL2L3Corrector'])
