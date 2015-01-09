import FWCore.ParameterSet.Config as cms

from Dummy.Puppi.Puppi_cff import *

from CommonTools.ParticleFlow.ParticleSelectors.pfAllChargedHadrons_cfi import *
from CommonTools.ParticleFlow.ParticleSelectors.pfAllNeutralHadrons_cfi import *
from CommonTools.ParticleFlow.ParticleSelectors.pfAllPhotons_cfi import *

def load_pfPUPPI_sequence(proc, seq_name, algo, src_puppi='particleFlow', src_vtx='offlinePrimaryVertices', cone_puppi_central=0.3):

    setattr(proc, 'pfAllHadronsAndPhotonsFor'+algo,
      pfAllNeutralHadrons.clone( src = cms.InputTag('particleFlow'),
        pdgId = cms.vint32(22,111,130,310,2112,211,-211,321,-321,999211,2212,-2212)
      )
    )

    setattr(proc, 'particleFlow'+algo,
      puppi.clone( PuppiName = '',
        candName   = src_puppi,
        vertexName = src_vtx
      )
    )
    # configure parameter PuppiCentral.cone
    getattr(proc, 'particleFlow'+algo).algos[0].puppiAlgos[0].cone = cone_puppi_central

    setattr(proc, 'pf'+algo+'ChargedHadrons', pfAllChargedHadrons.clone(src = cms.InputTag('particleFlow'+algo)))
    setattr(proc, 'pf'+algo+'NeutralHadrons', pfAllNeutralHadrons.clone(src = cms.InputTag('particleFlow'+algo)))
    setattr(proc, 'pf'+algo+'Photons', pfAllPhotons.clone(src = cms.InputTag('particleFlow'+algo)))

    pf_puppi_seq = cms.Sequence(
        getattr(proc, 'pfAllHadronsAndPhotonsFor'+algo)
      * getattr(proc, 'particleFlow'+algo)
      * getattr(proc, 'pf'+algo+'ChargedHadrons')
      * getattr(proc, 'pf'+algo+'NeutralHadrons')
      * getattr(proc, 'pf'+algo+'Photons')
    )

    setattr(proc, seq_name, pf_puppi_seq)
