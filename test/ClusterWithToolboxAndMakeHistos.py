import FWCore.ParameterSet.Config as cms
###
### cmsRun ClusterWithToolboxAndPlot.py
###  make jet plots from miniAOD with some additional jet collections clustered 
### Jet Algorithm HATS 2015 - Dolen, Rappoccio, Stupak
###
### cmsrel CMSSW_7_4_4
### cd CMSSW_7_4_4/src
### git clone https://github.com/cms-jet/JMEDAS.git Analysis/JMEDAS
### git clone https://github.com/cms-jet/JetToolbox Analysis/JetToolbox -b jetToolbox_74X
### scram b
### cmsenv

process = cms.Process("Ana")

### SETUP
process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
process.GlobalTag.globaltag = 'MCRUN2_74_V7'
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
process.options.allowUnscheduled = cms.untracked.bool(True)

### INPUT
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(30) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
#'file:jettoolbox.root'
        'root://cmsxrootd-site.fnal.gov///store/mc/RunIISpring15DR74/TT_Mtt-1000toInf_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9_ext1-v2/10000/A8EB631F-640C-E511-B828-0025905964BC.root'
    )
)


### ADD SOME NEW JET COLLECTIONS
from Analysis.JetToolbox.jetToolbox_cff import *

# add an AK R=1.2 jets with basic grooming, W tagging, and top tagging
jetToolbox( process, 'ak12', 'ak12JetSubs', 'out', 
  addPruning=True, addSoftDrop=True ,           # add basic grooming
  addTrimming=True, addFiltering=True, 
  addNsub=True, maxTau=4,                       # add Nsubjettiness tau1, tau2, tau3, tau4
  addCMSTopTagger=True, addHEPTopTagger=False   # Add top tagging algorithms
)

# add an AK R=0.8 jets with non-default grooming paramters 
jetToolbox( process, 'ak8', 'ak8JetSub', 'out', 
  addSoftDrop=True ,  betaCut=0.0,  zCutSD=0.2, 
  addTrimming=True,   rFiltTrim=0.2, ptFrac=0.10,
  addFiltering=True,  rfilt=0.2, nfilt=3,
  addPruning=True
)

# add an AK R=0.8 jets clustered from PUPPI
jetToolbox( process, 'ak8', 'ak8JetSub', 'out', 
  PUMethod='Puppi',                    #### Options: Puppi, CS, SK, Plain
  addSoftDrop=True ,  
  addTrimming=True,  
  addFiltering=True,
  addPruning=True
)

# add an AK R=0.8 jets clustered from all PF paritles
jetToolbox( process, 'ak8', 'ak8JetSub', 'out', 
  PUMethod='Plain',                    #### Options: Puppi, CS, SK, Plain
  addSoftDrop=True ,  
  addTrimming=True,  
  addFiltering=True,
  addPruning=True
)


# Example snipet for correcting jets with the toolbox
#  JETCorrPayload='AK8PFchs', subJETCorrPayload='AK3PFchs', JETCorrLevels=['L1FastJet', 'L2Relative'] 

# Example snipet to add subjets
#  addPrunedSubjets=False, addSoftDropSubjets=False, 

#jetToolbox( process, jetType, jetSequence, outputFile, 
#		PUMethod='CHS',                    #### Options: Puppi, CS, SK, Plain
#		JETCorrPayload='None', JETCorrLevels = [ 'None' ],
#		subJETCorrPayload='None', subJETCorrLevels = [ 'None' ],
#		miniAOD=True,
#		Cut = '', 
#		addPruning=False, zCut=0.1, rCut=0.5, addPrunedSubjets=False,
#		addSoftDrop=False, betaCut=0.0,  zCutSD=0.1, addSoftDropSubjets=False,
#		addTrimming=False, rFiltTrim=0.2, ptFrac=0.03,
#		addFiltering=False, rfilt=0.3, nfilt=3,
#		addCMSTopTagger=False,
#		addMassDrop=False,
#		addHEPTopTagger=False,
#		addNsub=False, maxTau=4, 
#		addQJets=False 
#		):


# Soft drop defaut https://github.com/cms-sw/cmssw/blob/3f7acf4b12067e3e7eec1066995cf3e88953894d/RecoJets/JetProducers/python/ak4PFJetsSoftDrop_cfi.py
#    zcut = cms.double(0.1),
#    beta = cms.double(0.0),
#    R0   = cms.double(0.4),

# Trimming https://github.com/cms-sw/cmssw/blob/3f7acf4b12067e3e7eec1066995cf3e88953894d/RecoJets/JetProducers/python/ak4PFJetsTrimmed_cfi.py
# rFilt = cms.double(0.2),
#    trimPtFracMin = cms.double(0.03),

# Prune https://github.com/cms-sw/cmssw/blob/743bde9939bbc4f34c2b4fd022cfb980314f912a/RecoJets/JetProducers/python/SubJetParameters_cfi.py
#nFilt = cms.int32(2),                # number of subjets to decluster the fat jet into (actual value can be less if less than 6 constituents in fat jet).
#    zcut = cms.double(0.1),                 # zcut parameter for pruning (see ref. for details)
#    rcut_factor = cms.double(0.5)           # rcut factor for pruning (the ref. uses 0.5)

# Filt
#   nFilt = cms.int32(3),
#    rFilt = cms.double(0.3),


### MAKE SOME HISTOGRAMS
process.ana = cms.EDAnalyzer('JetTester'
)

### OUT
process.TFileService = cms.Service("TFileService",
      fileName = cms.string("histos.root"),
      closeFileFast = cms.untracked.bool(True)
  )

#process.endpath = cms.EndPath(process.out) #output jet collections in a root file

# process.p = cms.Path(process.selectedPatJetsAK12PFCHS*process.demo)
process.p = cms.Path(process.ana)
