import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(5000) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(
        'root://cmsxrootd.fnal.gov:///store/mc/RunIISpring16MiniAODv2/ZprimeToTT_M-3000_W-900_13TeV-madgraph/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/00694A03-DB3A-E611-AEDF-002590552120.root',
        'root://cmsxrootd.fnal.gov:///store/mc/RunIISpring16MiniAODv2/ZprimeToTT_M-3000_W-900_13TeV-madgraph/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/82738509-B33A-E611-ACAA-0CC47AA98F98.root',
        'root://cmsxrootd.fnal.gov:///store/mc/RunIISpring16MiniAODv2/ZprimeToTT_M-3000_W-900_13TeV-madgraph/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/EAA4BB9E-DF3A-E611-B1B1-0CC47A6C1818.root'
    )
)

process.ana = cms.EDAnalyzer('JetMiniValidation',
          jecPayloads = cms.vstring([
                                    '../data/Spring16_25nsV5_MC/Spring16_25nsV5_MC_L1FastJet_AK8PFchs.txt',
                                    '../data/Spring16_25nsV5_MC/Spring16_25nsV5_MC_L2Relative_AK8PFchs.txt',
                                    '../data/Spring16_25nsV5_MC/Spring16_25nsV5_MC_L3Absolute_AK8PFchs.txt',
                                    '../data/Spring16_25nsV5_MC/Spring16_25nsV5_MC_L2L3Residual_AK8PFchs.txt',
                                    '../data/Spring16_25nsV5_MC/Spring16_25nsV5_MC_Uncertainty_AK8PFchs.txt'
                                    ]),
)


### OUT
process.TFileService = cms.Service("TFileService",
      fileName = cms.string("out_JetMiniValidation.root"),
      closeFileFast = cms.untracked.bool(True)
  )

process.p = cms.Path(process.ana)
