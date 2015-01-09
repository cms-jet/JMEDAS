import FWCore.ParameterSet.Config as cms

from RecoJets.JetProducers.ak4PFJets_cfi import ak4PFJets
from RecoJets.JetProducers.ak4GenJets_cfi import ak4GenJets

from PhysicsTools.PatAlgos.tools.jetTools import addJetCollection
from PhysicsTools.PatAlgos.tools.jetTools import switchJetCollection

def load_PUPPIJet_sequence(proc, seq_name, rParam):

	puppi_seq = cms.Sequence()
	for r in rParam:
		if r==0.4:
			ak4GenJets.src = 'packedGenParticles'
			setattr(proc,"ak4GenJets",ak4GenJets)
			# Select candidates that would pass CHS requirements
			#AK4PFchs = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
			#setattr(proc,"ak4PFchsJets",AK4PFchs)
			#AK4PUPPI = ak4PFJets.clone(src = 'packedPFCandidates')
			ak4PUPPI = ak4PFJets.clone(src = 'particleFlowPUPPI')
			setattr(proc,"ak4PUPPI",ak4PUPPI)
			puppi_seq = cms.Sequence(puppi_seq*ak4GenJets*ak4PUPPI)
			addJetCollection(
				proc,
				labelName = 'AK4PUPPIJets',
				jetSource = cms.InputTag('ak4PUPPI'),
				algo = 'ak4',
				rParam = 0.4,
				jetCorrections = None,
				trackSource = cms.InputTag('unpackedTracksAndVertices'),
				pvSource = cms.InputTag('unpackedTracksAndVertices'),
				#btagDiscriminators = ['combinedSecondaryVertexBJetTags'],
			)
			for module in [proc.patJetsAK4PUPPIJets]:
				module.addJetCharge = False
				module.addBTagInfo = False
				module.getJetMCFlavour = False
				module.addAssociatedTracks = False
			for module in [proc.patJetPartonMatchAK4PUPPIJets]:
				module.matched='prunedGenParticles'

		elif r==0.8:
			ak8GenJets = ak4GenJets.clone(rParam=0.8)
			ak8GenJets.src = 'packedGenParticles'
			setattr(proc,"ak8GenJets",ak8GenJets)
			# Select candidates that would pass CHS requirements
			#AK8PFchs = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))
			#setattr(proc,"ak8PFchsJets",AK8PFchs)
			#AK8PUPPI = ak4PFJets.clone(src = 'packedPFCandidates', rParam = 0.8)
			ak8PUPPI = ak4PFJets.clone(src = 'particleFlowPUPPI', rParam = 0.8)
			setattr(proc,"ak8PUPPI",ak8PUPPI)
			puppi_seq = cms.Sequence(puppi_seq*ak8GenJets*ak8PUPPI)
			addJetCollection(
				proc,
				labelName = 'AK8PUPPIJets',
				jetSource = cms.InputTag('ak8PUPPI'),
				algo = 'ak8',
				rParam = 0.8,
				jetCorrections = None,
				trackSource = cms.InputTag('unpackedTracksAndVertices'),
				pvSource = cms.InputTag('unpackedTracksAndVertices'),
				#btagDiscriminators = ['combinedSecondaryVertexBJetTags'],
			)
			for module in [proc.patJetsAK8PUPPIJets]:
				module.addJetCharge = False
				module.addBTagInfo = False
				module.getJetMCFlavour = False
				module.addAssociatedTracks = False
			for module in [proc.patJetPartonMatchAK8PUPPIJets]:
				module.matched='prunedGenParticles'

	setattr(proc, seq_name, puppi_seq)