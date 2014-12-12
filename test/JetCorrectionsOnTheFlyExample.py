# PYTHON configuration file for class: JetPlotsExample
# Description:  Example of simple EDAnalyzer for jets.
# Author: K. Kousouris
# Date:  25 - August - 2008
# Modified: Kalanand Mishra
# Date:  11 - January - 2011 (for CMS Data Analysis School jet exercise)


import FWCore.ParameterSet.Config as cms

##  ____        _                       __  __  ____ 
## |  _ \  __ _| |_ __ _    ___  _ __  |  \/  |/ ___|
## | | | |/ _` | __/ _` |  / _ \| '__| | |\/| | |    
## | |_| | (_| | || (_| | | (_) | |    | |  | | |___ 
## |____/ \__,_|\__\__,_|  \___/|_|    |_|  |_|\____|
            
isMC = True
##isMC = True

##   ____             __ _                       _     _           
##  / ___|___  _ __  / _(_) __ _ _   _ _ __ __ _| |__ | | ___  ___ 
## | |   / _ \| '_ \| |_| |/ _` | | | | '__/ _` | '_ \| |/ _ \/ __|
## | |__| (_) | | | |  _| | (_| | |_| | | | (_| | |_) | |  __/\__ \
##  \____\___/|_| |_|_| |_|\__, |\__,_|_|  \__,_|_.__/|_|\___||___/
##                         |___/

PFJetCollection   = "slimmedJets"


PlotSuffix = "_Data"

if isMC:
  PlotSuffix = "_MC"
  jecLevels = [
    'PHYS14_25_V1_L1FastJet_AK4PFchs.txt',
    'PHYS14_25_V1_L2Relative_AK4PFchs.txt',
    'PHYS14_25_V1_L3Absolute_AK4PFchs.txt'
  ]
else :
  jecLevels = [
    'PHYS14_25_V1_L1FastJet_AK4PFchs.txt',
    'PHYS14_25_V1_L2Relative_AK4PFchs.txt',
    'PHYS14_25_V1_L3Absolute_AK4PFchs.txt',
    'PHYS14_25_V1_L2L3Residual_AK4PFchs.txt'
  ]


if isMC:
  PlotSuffix = "_MC"  


##  _            _           _           
## (_)_ __   ___| |_   _  __| | ___  ___ 
## | | '_ \ / __| | | | |/ _` |/ _ \/ __|
## | | | | | (__| | |_| | (_| |  __/\__ \
## |_|_| |_|\___|_|\__,_|\__,_|\___||___/
    
process = cms.Process("Ana")
#############   Format MessageLogger #################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10


process.TFileService = cms.Service("TFileService",
  fileName = cms.string('jetCorrectionsOnTheFlyExample.root')
)


##  ____             _ ____                           
## |  _ \ ___   ___ | / ___|  ___  _   _ _ __ ___ ___ 
## | |_) / _ \ / _ \| \___ \ / _ \| | | | '__/ __/ _ \
## |  __/ (_) | (_) | |___) | (_) | |_| | | | (_|  __/
## |_|   \___/ \___/|_|____/ \___/ \__,_|_|  \___\___|
                                                   

#############   Set the number of events #############
process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(2000)
)
#############   Define the source file ###############

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring([
'/store/mc/Phys14DR/RSGluonToTT_M-3000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/4EFDC292-9D67-E411-A370-0025905AA9CC.root',
'/store/mc/Phys14DR/RSGluonToTT_M-3000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/88740B8A-9D67-E411-85EF-0025905A60F8.root',
'/store/mc/Phys14DR/RSGluonToTT_M-3000_Tune4C_13TeV-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/CA35A691-9D67-E411-93B4-0025905A6088.root'
        ])
)



process.source.inputCommands = cms.untracked.vstring("keep *","drop *_MEtoEDMConverter_*_*")


##  ____  _       _       
## |  _ \| | ___ | |_ ___ 
## | |_) | |/ _ \| __/ __|
## |  __/| | (_) | |_\__ \
## |_|   |_|\___/ \__|___/

#############   PF Jets    ###########################
process.pf = cms.EDAnalyzer("JetCorrectionsOnTheFly",
    jetSrc = cms.InputTag('slimmedJets'),
    rhoSrc = cms.InputTag('fixedGridRhoAll'),
    pvSrc  = cms.InputTag('offlineSlimmedPrimaryVertices'),
    jecPayloadNames = cms.vstring( jecLevels ),
    jecUncName = cms.string('PHYS14_25_V1_Uncertainty_AK4PFchs.txt') 
)



#############   Path       ###########################
##  ____       _   _     
## |  _ \ __ _| |_| |__  
## | |_) / _` | __| '_ \ 
## |  __/ (_| | |_| | | |
## |_|   \__,_|\__|_| |_|

process.myseq = cms.Sequence(process.pf )
process.p = cms.Path( process.myseq)
