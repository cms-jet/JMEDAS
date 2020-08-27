import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10)  )

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                        '/store/mc/RunIIAutumn18MiniAOD/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/102X_upgrade2018_realistic_v15-v1/210000/DA20DC21-E781-C540-9FCD-7BCF2144CA4E.root'

                            )
                            )

process.demo = cms.EDAnalyzer("MiniAnalyzer",
                                  vertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
                                  jets = cms.InputTag("slimmedJets"),
                                  fatjets = cms.InputTag("slimmedJetsAK8")
                              )

process.p = cms.Path(process.demo)
