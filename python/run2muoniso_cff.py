import FWCore.ParameterSet.Config as cms

from pfPUPPISequence_cff import *
from MuonPFIsolationSequence_cff import *
from makePUPPIJets_cff import *

def run2muoniso(process):

    ### Geometry and Detector Conditions (needed for a few patTuple production steps)
    process.load('Configuration.Geometry.GeometryIdeal_cff')
    process.load('Configuration.StandardSequences.MagneticField_cff')
    process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
    
    ### load default PAT sequence
    process.load("PhysicsTools.PatAlgos.producersLayer1.patCandidates_cff")
    process.load("PhysicsTools.PatAlgos.selectionLayer1.selectedPatCandidates_cff")
    process.load("Analysis.JMEDAS.convertPackedCandToRecoCand_cff")
    process.patseq = cms.Sequence(process.convertedPackedPFCandidates * process.patCandidates * process.selectedPatCandidates)
    process.p = cms.Path(process.patseq)
    
    # change the input collections
    process.particleFlowPtrs.src = 'convertedPackedPFCandidates'
    process.pfPileUpIso.Vertices = 'offlineSlimmedPrimaryVertices'
    process.pfPileUp.Vertices    = 'offlineSlimmedPrimaryVertices'

    # remove unnecessary PAT modules
    process.p.remove(process.makePatElectrons)
    process.p.remove(process.makePatPhotons)
    process.p.remove(process.makePatJets)
    process.p.remove(process.makePatTaus)
    process.p.remove(process.makePatMETs)
    process.p.remove(process.patCandidateSummary)
    process.p.remove(process.selectedPatElectrons)
    process.p.remove(process.selectedPatPhotons)
    process.p.remove(process.selectedPatJets)
    process.p.remove(process.selectedPatTaus)
    process.p.remove(process.selectedPatCandidateSummary)
    
    ### muon selection
    process.selectedPatMuons.src = 'slimmedMuons'
    process.selectedPatMuons.cut = 'pt>10 && abs(eta)<2.4'
    
    # load user-defined particle collections (e.g. PUPPI)
    
    # -- PF-Weighted
    process.load('CommonTools.ParticleFlow.deltaBetaWeights_cff')
    
    # -- PUPPI
    load_pfPUPPI_sequence(process, 'pfPUPPISequence', algo = 'PUPPI',
      src_puppi = 'pfAllHadronsAndPhotonsForPUPPI',
      cone_puppi_central = 0.5
    )

    # change the input collections
    process.pfAllHadronsAndPhotonsForPUPPI.src = 'convertedPackedPFCandidates'
    process.particleFlowPUPPI.candName = 'packedPFCandidates'
    process.particleFlowPUPPI.vertexName = 'offlineSlimmedPrimaryVertices'

    load_PUPPIJet_sequence(process,"PUPPIJetSequence",[0.4,0.8])

    process.p.replace(
      process.pfParticleSelectionSequence,
      process.pfParticleSelectionSequence  *
      process.pfDeltaBetaWeightingSequence *
      process.pfPUPPISequence *
      process.PUPPIJetSequence *
      process.patJetPartonMatchAK4PUPPIJets *
      process.patJetGenJetMatchAK4PUPPIJets *
      process.patJetsAK4PUPPIJets *
      process.patJetPartonMatchAK8PUPPIJets *
      process.patJetGenJetMatchAK8PUPPIJets *
      process.patJetsAK8PUPPIJets
    )
    
    # load user-defined muon PF-isolation values
    muon_src, cone_size = 'selectedPatMuons', 0.4
    
    load_muonPFiso_sequence(process, 'MuonPFIsoSequenceSTAND', algo = 'R04STAND',
      src = muon_src,
      src_charged_hadron = 'pfAllChargedHadrons',
      src_neutral_hadron = 'pfAllNeutralHadrons',
      src_photon         = 'pfAllPhotons',
      src_charged_pileup = 'pfPileUpAllChargedParticles',
      coneR = cone_size
    )
    
    load_muonPFiso_sequence(process, 'MuonPFIsoSequencePFWGT', algo = 'R04PFWGT',
      src = muon_src,
      src_neutral_hadron = 'pfWeightedNeutralHadrons',
      src_photon         = 'pfWeightedPhotons',
      coneR = cone_size
    )
    
    load_muonPFiso_sequence(process, 'MuonPFIsoSequencePUPPI', algo = 'R04PUPPI',
      src = muon_src,
      src_charged_hadron = 'pfPUPPIChargedHadrons',
      src_neutral_hadron = 'pfPUPPINeutralHadrons',
      src_photon         = 'pfPUPPIPhotons',
      coneR = cone_size
    )

    # change the input collections
    process.muPFIsoDepositCharged.src = 'slimmedMuons'
    process.muonMatch.src = 'slimmedMuons'
    process.muonMatch.matched = 'prunedGenParticles'
    process.patMuons.pvSrc = 'offlineSlimmedPrimaryVertices'
    #process.patMuons.embedTunePMuonBestTrack = False
    #process.patMuons.embedMuonBestTrack = False
    #process.patMuons.pfMuonSource = 'packedPFCandidates'
    process.p.remove(process.patMuons)
    
    process.MuonPFIsoSequences = cms.Sequence(
      process.MuonPFIsoSequenceSTAND *
      process.MuonPFIsoSequencePFWGT *
      process.MuonPFIsoSequencePUPPI
    )
    
    process.p.replace(
      process.selectedPatMuons,
      process.selectedPatMuons *
      process.MuonPFIsoSequences
    )

    # --- Output configuration ------------------------------------------------------------
    process.out = cms.OutputModule('PoolOutputModule',
      fileName = cms.untracked.string('pileupNtuple2.root'),
      ## save only events passing the full path
      #SelectEvents = cms.untracked.PSet( SelectEvents = cms.vstring('p') ),
      outputCommands = cms.untracked.vstring([
        'keep *_offlineSlimmedPrimaryVertices_*_*',
        'keep *_selectedPatMuons_*_*',
        'keep *_muPFIsoValue*STAND_*_*',
        'keep *_muPFIsoValue*PFWGT_*_*',
        'keep *_muPFIsoValue*PUPPI_*_*',
        'keep *_*PUPPI*_*_*'
      ])
    )
    
    #process.outpath = cms.EndPath(process.out)
