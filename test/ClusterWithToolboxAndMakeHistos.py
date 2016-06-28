import FWCore.ParameterSet.Config as cms
###
### cmsRun ClusterWithToolboxAndPlot.py
###  make jet plots from miniAOD with some additional jet collections clustered 
### Jet Algorithm HATS 2015 - Dolen, Rappoccio, Stupak
### Updated for Jet Algorithm HATS 2016 - Dolen, Pilot, Kries, Perloff, Tran
###
# setenv SCRAM_ARCH slc6_amd64_gcc530
# cmsrel CMSSW_8_0_8
# cd CMSSW_8_0_8/src
# git clone git@github.com:cms-jet/JMEDAS.git Analysis/JMEDAS
# git clone git@github.com:cms-jet/JetToolbox.git Analysis/JetToolbox -b jetToolbox_763
# scram b -j 8
# cmsenv
# cd Analysis/JMEDAS/test/
# cmsRun ClusterWithToolboxAndMakeHistos.py

process = cms.Process("Ana")

### SETUP
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = '80X_mcRun2_asymptotic_2016_miniAODv2'
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.options.allowUnscheduled = cms.untracked.bool(True)

### INPUT
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        # 'root://cmseos.fnal.gov:///store/user/jdolen/HATS/2016/MINIAOD/ZprimeToTT_M-4000_W-40_RunIISpring16MiniAODv2_0C59.root'
        'root://cmsxrootd.fnal.gov:///store/mc/RunIISpring16MiniAODv2/ZprimeToTT_M-3000_W-900_13TeV-madgraph/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/00694A03-DB3A-E611-AEDF-002590552120.root',
        'root://cmsxrootd.fnal.gov:///store/mc/RunIISpring16MiniAODv2/ZprimeToTT_M-3000_W-900_13TeV-madgraph/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/82738509-B33A-E611-ACAA-0CC47AA98F98.root',
        'root://cmsxrootd.fnal.gov:///store/mc/RunIISpring16MiniAODv2/ZprimeToTT_M-3000_W-900_13TeV-madgraph/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/EAA4BB9E-DF3A-E611-B1B1-0CC47A6C1818.root'
    )
)

### ADD SOME NEW JET COLLECTIONS
from Analysis.JetToolbox.jetToolbox_cff import *

# AK R=0.4 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak4', 'ak4JetSubs', 'out', 
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK4PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=0.8 jets from PF inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', 
  PUMethod='Plain',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PF', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=0.8 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', 
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=0.8 from PUPPI inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak8', 'ak8JetSubs', 'out', 
  PUMethod='Puppi',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFPuppi', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# CA R=0.8 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ca8', 'ca8JetSubs', 'out', 
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# KT R=0.8 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'kt8', 'kt8JetSubs', 'out',
  PUMethod='CHS', 
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=1.2 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak12', 'ak12JetSubs', 'out', 
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

# AK R=1.5 jets from CHS inputs with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak15', 'ak15JetSubs', 'out', 
  PUMethod='CHS',
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addSoftDropSubjets=True,
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  JETCorrPayload = 'AK8PFchs', JETCorrLevels = ['L2Relative', 'L3Absolute']
)

### MAKE SOME HISTOGRAMS
process.ana = cms.EDAnalyzer('JetTester'
)

### OUT
process.TFileService = cms.Service("TFileService",
      fileName = cms.string("JetClusterHistos_ZP3000w900.root"),
      closeFileFast = cms.untracked.bool(True)
  )

# Uncomment the following line if you would like to output the jet collections in a root file
# process.endpath = cms.EndPath(process.out) 

process.p = cms.Path(process.ana)
