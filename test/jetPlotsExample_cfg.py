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
            
##isMC = False
isMC = True


##   _            _           _           
## (_)_ __   ___| |_   _  __| | ___  ___ 
## | | '_ \ / __| | | | |/ _` |/ _ \/ __|
## | | | | | (__| | |_| | (_| |  __/\__ \
## |_|_| |_|\___|_|\__,_|\__,_|\___||___/
    
process = cms.Process("Ana")
#############   Format MessageLogger #################
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 10



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


process.TFileService = cms.Service("TFileService",
        fileName = cms.string('jetPlotsExample.root')
    )
##   ______     _      _      _
##  |__  __|__ | |_   (_) __| |
##  _  | |/ _ \| __/  | |/ _` |
## | \_| |  __/| |_   | | (_| |
##  \____|\___| \__|  |_|\__,_|
##
from PhysicsTools.SelectorUtils.pfJetIDSelector_cfi import pfJetIDSelector
process.tightPatJetsPFlow = cms.EDFilter("PFJetIDSelectionFunctorFilter",
                                         filterParams = pfJetIDSelector.clone(quality=cms.string("TIGHT")),
                                         src = cms.InputTag("slimmedJets")
                                         )
##  ____  _       _       
## |  _ \| | ___ | |_ ___ 
## | |_) | |/ _ \| __/ __|
## |  __/| | (_) | |_\__ \
## |_|   |_|\___/ \__|___/


#############   AK4 Jets    ###########################
process.ak4plots = cms.EDAnalyzer("JetPlotsExample",
    jetSrc  = cms.InputTag("slimmedJets"),
    leadJetPtMin = cms.double( 20.0 ),
    jetPtMin = cms.double( 20.0 ),
    plotSubstructure = cms.bool( False )
)


#############   AK8 Jets    ###########################
process.ak8plots = cms.EDAnalyzer("JetPlotsExample",
    jetSrc  = cms.InputTag("slimmedJetsAK8"),
    leadJetPtMin = cms.double( 200.0 ),
    jetPtMin = cms.double( 50.0 ),
    plotSubstructure = cms.bool( True )
)



##  ____       _   _     
## |  _ \ __ _| |_| |__  
## | |_) / _` | __| '_ \ 
## |  __/ (_| | |_| | | |
## |_|   \__,_|\__|_| |_|

##process.myseq = cms.Sequence(process.calo*process.pf*process.jpt*process.gen)
process.myseq = cms.Sequence(process.ak4plots *
                             process.ak8plots *
                             process.tightPatJetsPFlow
                             )
  
process.p = cms.Path( process.myseq)
