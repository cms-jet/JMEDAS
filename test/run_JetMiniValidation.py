import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
'file:/uscmst1b_scratch/lpc1/lpcphys/jdolen/JMAR/Relval805/RelValTTbar_13_CMSSW_8_0_5-80X_mcRun2_asymptotic_v12_gs7120p2-v1_MINIAODSIM_168.root',
'file:/uscmst1b_scratch/lpc1/lpcphys/jdolen/JMAR/Relval805/RelValTTbar_13_CMSSW_8_0_5-80X_mcRun2_asymptotic_v12_gs7120p2-v1_MINIAODSIM_3AC.root'
#'file:/uscmst1b_scratch/lpc1/lpcphys/jdolen/JMAR/Relval805/RelValZpTT_1500_13_CMSSW_8_0_5-80X_mcRun2_asymptotic_v12_gs7120p2-v1_MINIAODSIM_3C7.root'
#'file:/uscmst1b_scratch/lpc1/lpcphys/jdolen/JMAR/Relval805/RelValTTbar_13.root'
#        'root://cmsxrootd.fnal.gov//store/relval/CMSSW_8_0_0/RelValTTbar_13/MINIAODSIM/PU25ns_80X_mcRun2_asymptotic_v4-v1/10000/A65CD249-BFDA-E511-813A-0025905A6066.root'
    )
)

process.ana = cms.EDAnalyzer('JetMiniValidation'
)


### OUT
process.TFileService = cms.Service("TFileService",
      fileName = cms.string("out_JetMiniValidation.root"),
      closeFileFast = cms.untracked.bool(True)
  )

process.p = cms.Path(process.ana)
