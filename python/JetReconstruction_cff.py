import FWCore.ParameterSet.Config as cms

# event setup
from Configuration.StandardSequences.Geometry_cff import *
from Configuration.StandardSequences.MagneticField_cff import *

# jet reconstruction
from RecoJets.Configuration.GenJetParticles_cff import *
from RecoJets.Configuration.RecoGenJets_cff import *
from RecoJets.Configuration.RecoJets_cff import *
from RecoJets.Configuration.RecoPFJets_cff import *

#########################
# ANTI-KT JET PRODUCERS #
#########################

#!
#! GEN JET PRODUCERS
#!
ak1GenJets      = ak5GenJets.clone  ( rParam=0.1 )
ak2GenJets      = ak5GenJets.clone  ( rParam=0.2 )
ak3GenJets      = ak5GenJets.clone  ( rParam=0.3 )
ak6GenJets      = ak5GenJets.clone  ( rParam=0.6 )
ak7GenJets      = ak5GenJets.clone  ( rParam=0.7 )
ak9GenJets      = ak5GenJets.clone  ( rParam=0.9 )
ak10GenJets     = ak5GenJets.clone  ( rParam=1.0 )

#!
#! GEN JETS WITHOUT NEUTRINOS
#!
ak1GenJetsNoNu  = ak1GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ak2GenJetsNoNu  = ak2GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ak3GenJetsNoNu  = ak3GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ak6GenJetsNoNu  = ak6GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ak7GenJetsNoNu  = ak7GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ak9GenJetsNoNu  = ak9GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ak10GenJetsNoNu = ak10GenJets.clone( src = 'genParticlesForJetsNoNu' )

#!
#! GENJETS WITHOUT MUONS & NEUTRINOS
#!
ak1GenJetsNoMuNoNu  = ak1GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ak2GenJetsNoMuNoNu  = ak2GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ak3GenJetsNoMuNoNu  = ak3GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ak6GenJetsNoMuNoNu  = ak6GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ak7GenJetsNoMuNoNu  = ak7GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ak9GenJetsNoMuNoNu  = ak9GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ak10GenJetsNoMuNoNu = ak10GenJets.clone( src = 'genParticlesForJetsNoMuNoNu' )

#!
#! HLT JETS
#!
ak5CaloHLTJets   = ak5CaloJets.clone( src = 'hltAntiKT5CaloJets' )
ak5PFHLTJets     = ak5PFJets.clone( src = 'hltAntiKT5PFJets' )
ak5PFchsHLTJets  = ak5PFJets.clone( src = 'hltAntiKT5PFJetsNoPUPixelVert' )

#!
#! CALO JETS
#!
ak1CaloJets     = ak5CaloJets.clone ( rParam=0.1 )
ak2CaloJets     = ak5CaloJets.clone ( rParam=0.2 )
ak3CaloJets     = ak5CaloJets.clone ( rParam=0.3 )
ak6CaloJets     = ak5CaloJets.clone ( rParam=0.6 )
ak8CaloJets     = ak5CaloJets.clone ( rParam=0.8 )
ak9CaloJets     = ak5CaloJets.clone ( rParam=0.9 )
ak10CaloJets    = ak5CaloJets.clone ( rParam=1.0 )

#!
#! PF JETS
#!
ak1PFJets       = ak5PFJets.clone   ( rParam=0.1 )
ak2PFJets       = ak5PFJets.clone   ( rParam=0.2 )
ak3PFJets       = ak5PFJets.clone   ( rParam=0.3 )
ak6PFJets       = ak5PFJets.clone   ( rParam=0.6 )
ak9PFJets       = ak5PFJets.clone   ( rParam=0.9 )
ak10PFJets      = ak5PFJets.clone   ( rParam=1.0 )

#!
#! PF JETS CHS
#!
ak1PFJetsCHS    = ak5PFJetsCHS.clone( rParam=0.1 )
ak2PFJetsCHS    = ak5PFJetsCHS.clone( rParam=0.2 )
ak3PFJetsCHS    = ak5PFJetsCHS.clone( rParam=0.3 )
ak6PFJetsCHS    = ak5PFJetsCHS.clone( rParam=0.6 )
ak7PFJetsCHS    = ak5PFJetsCHS.clone( rParam=0.7 )
ak9PFJetsCHS    = ak5PFJetsCHS.clone( rParam=0.9 )
ak10PFJetsCHS   = ak5PFJetsCHS.clone( rParam=1.0 )

#!
#! PF JETS PUPPI
#!
ak1PFJetsPuppi  = ak4PFJetsPuppi.clone( rParam=0.1 )
ak2PFJetsPuppi  = ak4PFJetsPuppi.clone( rParam=0.2 )
ak3PFJetsPuppi  = ak4PFJetsPuppi.clone( rParam=0.3 )
ak5PFJetsPuppi  = ak4PFJetsPuppi.clone( rParam=0.5 )
ak6PFJetsPuppi  = ak4PFJetsPuppi.clone( rParam=0.6 )
ak7PFJetsPuppi  = ak4PFJetsPuppi.clone( rParam=0.7 )
ak8PFJetsPuppi  = ak4PFJetsPuppi.clone( rParam=0.8 )
ak9PFJetsPuppi  = ak4PFJetsPuppi.clone( rParam=0.9 )
ak10PFJetsPuppi = ak4PFJetsPuppi.clone( rParam=1.0 )

####################
# KT JET PRODUCERS #
####################

#!
#! GEN JET PRODUCERS
#!
kt1GenJets    = kt4GenJets.clone( rParam=0.1 )
kt2GenJets    = kt4GenJets.clone( rParam=0.2 )
kt3GenJets    = kt4GenJets.clone( rParam=0.3 )
kt5GenJets    = kt4GenJets.clone( rParam=0.5 )
kt7GenJets    = kt4GenJets.clone( rParam=0.7 )
kt8GenJets    = kt4GenJets.clone( rParam=0.8 )
kt9GenJets    = kt4GenJets.clone( rParam=0.9 )
kt10GenJets   = kt4GenJets.clone( rParam=1.0 )

#!
#! GEN JETS WITHOUT NEUTRINOS
#!
kt1GenJetsNoNu  = kt1GenJets.clone ( src = 'genParticlesForJetsNoNu' )
kt2GenJetsNoNu  = kt2GenJets.clone ( src = 'genParticlesForJetsNoNu' )
kt3GenJetsNoNu  = kt3GenJets.clone ( src = 'genParticlesForJetsNoNu' )
kt5GenJetsNoNu  = kt5GenJets.clone ( src = 'genParticlesForJetsNoNu' )
kt7GenJetsNoNu  = kt7GenJets.clone ( src = 'genParticlesForJetsNoNu' )
kt8GenJetsNoNu  = kt8GenJets.clone ( src = 'genParticlesForJetsNoNu' )
kt9GenJetsNoNu  = kt9GenJets.clone ( src = 'genParticlesForJetsNoNu' )
kt10GenJetsNoNu = kt10GenJets.clone( src = 'genParticlesForJetsNoNu' )

#!
#! GENJETS WITHOUT MUONS & NEUTRINOS
#!
kt1GenJetsNoMuNoNu  = kt1GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
kt2GenJetsNoMuNoNu  = kt2GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
kt3GenJetsNoMuNoNu  = kt3GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
kt5GenJetsNoMuNoNu  = kt5GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
kt7GenJetsNoMuNoNu  = kt7GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
kt8GenJetsNoMuNoNu  = kt8GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
kt9GenJetsNoMuNoNu  = kt9GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
kt10GenJetsNoMuNoNu = kt10GenJets.clone( src = 'genParticlesForJetsNoMuNoNu' )

#!
#! CALO JETS
#!
kt1CaloJets   = kt4CaloJets.clone( rParam=0.1 )
kt2CaloJets   = kt4CaloJets.clone( rParam=0.2 )
kt3CaloJets   = kt4CaloJets.clone( rParam=0.3 )
kt5CaloJets   = kt4CaloJets.clone( rParam=0.5 )
kt7CaloJets   = kt4CaloJets.clone( rParam=0.7 )
kt8CaloJets   = kt4CaloJets.clone( rParam=0.8 )
kt9CaloJets   = kt4CaloJets.clone( rParam=0.9 )
kt10CaloJets  = kt4CaloJets.clone( rParam=1.0 )

#!
#! PF JETS
#!
kt1PFJets     = kt4PFJets.clone( rParam=0.1 )
kt2PFJets     = kt4PFJets.clone( rParam=0.2 )
kt3PFJets     = kt4PFJets.clone( rParam=0.3 )
kt5PFJets     = kt4PFJets.clone( rParam=0.5 )
kt7PFJets     = kt4PFJets.clone( rParam=0.7 )
kt8PFJets     = kt4PFJets.clone( rParam=0.8 )
kt9PFJets     = kt4PFJets.clone( rParam=0.9 )
kt10PFJets    = kt4PFJets.clone( rParam=1.0 )

#!
#! PF JETS CHS
#!
kt1PFJetsCHS  = kt1PFJets.clone( src = 'pfNoPileUpJME' )
kt2PFJetsCHS  = kt1PFJetsCHS.clone( rParam=0.2 )
kt3PFJetsCHS  = kt1PFJetsCHS.clone( rParam=0.3 )
kt4PFJetsCHS  = kt1PFJetsCHS.clone( rParam=0.4 )
kt5PFJetsCHS  = kt1PFJetsCHS.clone( rParam=0.5 )
kt6PFJetsCHS  = kt1PFJetsCHS.clone( rParam=0.6 )
kt7PFJetsCHS  = kt1PFJetsCHS.clone( rParam=0.7 )
kt8PFJetsCHS  = kt1PFJetsCHS.clone( rParam=0.8 )
kt9PFJetsCHS  = kt1PFJetsCHS.clone( rParam=0.9 )
kt10PFJetsCHS = kt1PFJetsCHS.clone( rParam=1.0 )

#!
#! PF JETS PUPPI
#!
kt1PFJetsPuppi  = kt5PFJets.clone( rParam=0.1, src = cms.InputTag('puppi'))
kt2PFJetsPuppi  = kt5PFJets.clone( rParam=0.2, src = cms.InputTag('puppi'))
kt3PFJetsPuppi  = kt5PFJets.clone( rParam=0.3, src = cms.InputTag('puppi'))
kt4PFJetsPuppi  = kt5PFJets.clone( rParam=0.4, src = cms.InputTag('puppi'))
kt5PFJetsPuppi  = kt5PFJets.clone( rParam=0.5, src = cms.InputTag('puppi'))
kt6PFJetsPuppi  = kt5PFJets.clone( rParam=0.6, src = cms.InputTag('puppi'))
kt7PFJetsPuppi  = kt5PFJets.clone( rParam=0.7, src = cms.InputTag('puppi'))
kt8PFJetsPuppi  = kt5PFJets.clone( rParam=0.8, src = cms.InputTag('puppi'))
kt9PFJetsPuppi  = kt5PFJets.clone( rParam=0.9, src = cms.InputTag('puppi'))
kt10PFJetsPuppi = kt5PFJets.clone( rParam=1.0, src = cms.InputTag('puppi'))

####################
# CA JET PRODUCERS #
####################

#!
#! GEN JET PRODUCERS
#!
ca1GenJets   = ca4GenJets.clone( rParam=0.1 )
ca2GenJets   = ca4GenJets.clone( rParam=0.2 )
ca3GenJets   = ca4GenJets.clone( rParam=0.3 )
ca5GenJets   = ca4GenJets.clone( rParam=0.5 )
ca6GenJets   = ca4GenJets.clone( rParam=0.6 )
ca7GenJets   = ca4GenJets.clone( rParam=0.7 )
ca9GenJets   = ca4GenJets.clone( rParam=0.9 )
ca10GenJets  = ca4GenJets.clone( rParam=1.0 )

#!
#! GEN JETS WITHOUT NEUTRINOS
#!
ca1GenJetsNoNu  = ca1GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ca2GenJetsNoNu  = ca2GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ca3GenJetsNoNu  = ca3GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ca5GenJetsNoNu  = ca5GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ca6GenJetsNoNu  = ca6GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ca7GenJetsNoNu  = ca7GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ca9GenJetsNoNu  = ca9GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ca10GenJetsNoNu = ca10GenJets.clone ( src = 'genParticlesForJetsNoNu' )

#!
#! GENJETS WITHOUT MUONS & NEUTRINOS
#!
ca1GenJetsNoMuNoNu  = ca1GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ca2GenJetsNoMuNoNu  = ca2GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ca3GenJetsNoMuNoNu  = ca3GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ca5GenJetsNoMuNoNu  = ca5GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ca6GenJetsNoMuNoNu  = ca6GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ca7GenJetsNoMuNoNu  = ca7GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ca9GenJetsNoMuNoNu  = ca9GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ca10GenJetsNoMuNoNu = ca10GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )

#!
#! CALO JETS
#!
ca1CaloJets  = ca4CaloJets.clone( rParam=0.1 )
ca2CaloJets  = ca4CaloJets.clone( rParam=0.2 )
ca3CaloJets  = ca4CaloJets.clone( rParam=0.3 )
ca5CaloJets  = ca4CaloJets.clone( rParam=0.5 )
ca7CaloJets  = ca4CaloJets.clone( rParam=0.7 )
ca8CaloJets  = ca4CaloJets.clone( rParam=0.8 )
ca9CaloJets  = ca4CaloJets.clone( rParam=0.9 )
ca10CaloJets = ca4CaloJets.clone( rParam=1.0 )

#!
#! PF JETS
#!
ca1PFJets    = ca4PFJets.clone( rParam=0.1 )
ca2PFJets    = ca4PFJets.clone( rParam=0.2 )
ca3PFJets    = ca4PFJets.clone( rParam=0.3 )
ca5PFJets    = ca4PFJets.clone( rParam=0.5 )
ca6PFJets    = ca4PFJets.clone( rParam=0.6 )
ca7PFJets    = ca4PFJets.clone( rParam=0.7 )
ca9PFJets    = ca4PFJets.clone( rParam=0.9 )
ca10PFJets   = ca4PFJets.clone( rParam=1.0 )

#!
#! PF JETS CHS
#!
ca1PFJetsCHS  = ca1PFJets.clone( src = 'pfNoPileUpJME' )
ca2PFJetsCHS  = ca1PFJetsCHS.clone( rParam=0.2 )
ca3PFJetsCHS  = ca1PFJetsCHS.clone( rParam=0.3 )
ca4PFJetsCHS  = ca1PFJetsCHS.clone( rParam=0.4 )
ca5PFJetsCHS  = ca1PFJetsCHS.clone( rParam=0.5 )
ca6PFJetsCHS  = ca1PFJetsCHS.clone( rParam=0.6 )
ca7PFJetsCHS  = ca1PFJetsCHS.clone( rParam=0.7 )
ca8PFJetsCHS  = ca1PFJetsCHS.clone( rParam=0.8 )
ca9PFJetsCHS  = ca1PFJetsCHS.clone( rParam=0.9 )
ca10PFJetsCHS = ca1PFJetsCHS.clone( rParam=1.0 )

#!
#! PF JETS PUPPI
#!
ca1PFJetsPuppi  = ca5PFJets.clone( rParam=0.1, src = cms.InputTag('puppi'))
ca2PFJetsPuppi  = ca5PFJets.clone( rParam=0.2, src = cms.InputTag('puppi'))
ca3PFJetsPuppi  = ca5PFJets.clone( rParam=0.3, src = cms.InputTag('puppi'))
ca4PFJetsPuppi  = ca5PFJets.clone( rParam=0.4, src = cms.InputTag('puppi'))
ca5PFJetsPuppi  = ca5PFJets.clone( rParam=0.5, src = cms.InputTag('puppi'))
ca6PFJetsPuppi  = ca5PFJets.clone( rParam=0.6, src = cms.InputTag('puppi'))
ca7PFJetsPuppi  = ca5PFJets.clone( rParam=0.7, src = cms.InputTag('puppi'))
ca8PFJetsPuppi  = ca5PFJets.clone( rParam=0.8, src = cms.InputTag('puppi'))
ca9PFJetsPuppi  = ca5PFJets.clone( rParam=0.9, src = cms.InputTag('puppi'))
ca10PFJetsPuppi = ca5PFJets.clone( rParam=1.0, src = cms.InputTag('puppi'))

###############################
# SIS CONE & IC JET PRODUCERS #
###############################

#!
#! GEN JET PRODUCERS
#!
sc5GenJets = sisCone5GenJets.clone()
sisCone7GenJets = sisCone5GenJets.clone ( rParam=0.7 )
sc7GenJets = sisCone7GenJets.clone()
ic5GenJets = iterativeCone5GenJets.clone()

#!
#! GEN JETS WITHOUT NEUTRINOS
#!
sc5GenJetsNoNu  = sc5GenJets.clone ( src = 'genParticlesForJetsNoNu' )
sc7GenJetsNoNu  = sc7GenJets.clone ( src = 'genParticlesForJetsNoNu' )
ic5GenJetsNoNu  = ic5GenJets.clone ( src = 'genParticlesForJetsNoNu' )

#!
#! GENJETS WITHOUT MUONS & NEUTRINOS
#!
sc5GenJetsNoMuNoNu  = sc5GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
sc7GenJetsNoMuNoNu  = sc7GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )
ic5GenJetsNoMuNoNu  = ic5GenJets.clone ( src = 'genParticlesForJetsNoMuNoNu' )

#!
#! CALO JETS
#!
sc5CaloJets = sisCone5CaloJets.clone()
sc7CaloJets = sisCone7CaloJets.clone()
ic5CaloJets = iterativeCone5CaloJets.clone()

#!
#! PF JETS
#!
sc5PFJets = sisCone5PFJets.clone()
sc7PFJets = sisCone7PFJets.clone()
ic5PFJets = iterativeCone5PFJets.clone()
