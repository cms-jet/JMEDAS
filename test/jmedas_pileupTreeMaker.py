#! Text To ASCII from http://patorjk.com/software/taag/#p=display&f=Big&t=MUON%20ISOLATION

import FWCore.ParameterSet.Config as cms
import collections

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	BOKGREEN = '\033[1m\033[92m'
	BWARNING = '\033[1m\033[93m'
	BFAIL = '\033[1m\033[91m'
 
#!  _____  _____   ____   _____ ______  _____ _____ 
#! |  __ \|  __ \ / __ \ / ____|  ____|/ ____/ ____|
#! | |__) | |__) | |  | | |    | |__  | (___| (___  
#! |  ___/|  _  /| |  | | |    |  __|  \___ \\___ \ 
#! | |    | | \ \| |__| | |____| |____ ____) |___) |
#! |_|    |_|  \_\\____/ \_____|______|_____/_____/ 

process = cms.Process("JRA")
process.options   = cms.untracked.PSet()
process.options.wantSummary = cms.untracked.bool(False)
process.options.allowUnscheduled = cms.untracked.bool(True)


#!   _____ ______ _______      _______ _____ ______  _____ 
#!  / ____|  ____|  __ \ \    / /_   _/ ____|  ____|/ ____|
#! | (___ | |__  | |__) \ \  / /  | || |    | |__  | (___  
#!  \___ \|  __| |  _  / \ \/ /   | || |    |  __|  \___ \ 
#!  ____) | |____| | \ \  \  /   _| || |____| |____ ____) |
#! |_____/|______|_|  \_\  \/   |_____\_____|______|_____/ 

process.load("Configuration.EventContent.EventContent_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Services_cff')
														 
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('CommonTools.UtilAlgos.TFileService_cfi')
process.TFileService.fileName=cms.string('pileupNtuple.root')


#!   _____ ____  _   _ _____ _____ _______ _____ ____  _   _  _____ 
#!  / ____/ __ \| \ | |  __ \_   _|__   __|_   _/ __ \| \ | |/ ____|
#! | |   | |  | |  \| | |  | || |    | |    | || |  | |  \| | (___  
#! | |   | |  | | . ` | |  | || |    | |    | || |  | | . ` |\___ \ 
#! | |___| |__| | |\  | |__| || |_   | |   _| || |__| | |\  |____) |
#!  \_____\____/|_| \_|_____/_____|  |_|  |_____\____/|_| \_|_____/ 
																  
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = cms.string('74X_mcRun2_asymptotic_v2')


#!  _____ _   _ _____  _    _ _______ 
#! |_   _| \ | |  __ \| |  | |__   __|
#!   | | |  \| | |__) | |  | |  | |   
#!   | | | . ` |  ___/| |  | |  | |   
#!  _| |_| |\  | |    | |__| |  | |   
#! |_____|_| \_|_|     \____/   |_|   

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))
process.load("Analysis.JMEDAS.qcdflat_MINIAODSIM_v2_cff")
#process.load("Analysis.JMEDAS.dy_MINIAODSIM_v2_cff")
dyFiles = cms.untracked.vstring(
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/FEE3CF68-796C-E411-ABF5-002590DB9214.root'
	)
#process.source = cms.Source("PoolSource", fileNames = dyFiles )


#!  __  __ _    _  ____  _   _   _____  _____  ____  _            _______ _____ ____  _   _ 
#! |  \/  | |  | |/ __ \| \ | | |_   _|/ ____|/ __ \| |        /\|__   __|_   _/ __ \| \ | |
#! | \  / | |  | | |  | |  \| |   | | | (___ | |  | | |       /  \  | |    | || |  | |  \| |
#! | |\/| | |  | | |  | | . ` |   | |  \___ \| |  | | |      / /\ \ | |    | || |  | | . ` |
#! | |  | | |__| | |__| | |\  |  _| |_ ____) | |__| | |____ / ____ \| |   _| || |__| | |\  |
#! |_|  |_|\____/ \____/|_| \_| |_____|_____/ \____/|______/_/    \_\_|  |_____\____/|_| \_|
																																													
process.PUPPIMuonRelIso = cms.EDProducer('PuppiLeptonIsolation'
										 , srcLepton = cms.InputTag( 'slimmedMuons' )
										 , dR = cms.double( 0.4 ) 
										 , mixFraction = cms.double( 0.5 ) 
										 , configuration = cms.string( "#detail#" )
)


#!           _      _____  ____  _____  _____ _______ _    _ __  __  _____ 
#!     /\   | |    / ____|/ __ \|  __ \|_   _|__   __| |  | |  \/  |/ ____|
#!    /  \  | |   | |  __| |  | | |__) | | |    | |  | |__| | \  / | (___  
#!   / /\ \ | |   | | |_ | |  | |  _  /  | |    | |  |  __  | |\/| |\___ \ 
#!  / ____ \| |___| |__| | |__| | | \ \ _| |_   | |  | |  | | |  | |____) |
#! /_/    \_\______\_____|\____/|_|  \_\_____|  |_|  |_|  |_|_|  |_|_____/                                                                        

jcr = cms.VPSet()
jetsCollections = {
#		'AK4': {
#				'algo': 'ak4',
#				'pu_methods': ['Puppi', 'CHS', ''],
#				'jec_payloads': ['None','None','None'],
#				'jec_levels': []
#				},
#		'AK4L1': {
#				  'algo': 'ak4',
#				  'pu_methods': ['Puppi', 'CHS', ''],
#				  'jec_payloads': ['AK4PFPuppi', 'AK4PFchs', 'AK4PF'],
#				  'jec_levels': ['L1FastJet']
#				  },
		'AK4L1L2L3': {
					  'algo': 'ak4',
					  'pu_methods': ['Puppi', 'CHS', ''],
					  'jec_payloads': ['AK4PFPuppi', 'AK4PFchs', 'AK4PF'],
					  'jec_levels': ['L1FastJet', 'L2Relative', 'L3Absolute']
					  },
#		'AK8': {
#				'algo': 'ak8',
#				'pu_methods': ['Puppi', 'CHS', ''],
#                'jec_payloads': ['None','None','None'],
#                'jec_levels': []
#				},
#		'AK8L1': {
#				  'algo': 'ak8',
#				  'pu_methods': ['Puppi', 'CHS', ''],
#				  'jec_payloads': ['AK8PFPuppi', 'AK8PFchs', 'AK8PF'],
#				  'jec_levels': ['L1FastJet']
#				  },
		'AK8L1L2L3': {
					  'algo': 'ak8',
					  'pu_methods': ['Puppi', 'CHS', ''],
					  'jec_payloads': ['AK8PFPuppi', 'AK8PFchs', 'AK8PF'],
					  'jec_levels': ['L1FastJet', 'L2Relative', 'L3Absolute']
					  },
					  }
jetsCollectionsSorted = collections.OrderedDict(sorted(jetsCollections.items(), key=lambda x:x[0], reverse=False))

process.p = cms.Path()
print "{:<15} {:<30} {:<30}".format('Algorithm','Jet Collection',"Correction Levels")
print "{:<15} {:<30} {:<30}".format('---------','--------------',"-----------------")

#      _ _____ _____   _____ ___   ___  _     ____   _____  __
#     | | ____|_   _| |_   _/ _ \ / _ \| |   | __ ) / _ \ \/ /
#  _  | |  _|   | |     | || | | | | | | |   |  _ \| | | \  /
# | |_| | |___  | |     | || |_| | |_| | |___| |_) | |_| /  \
#  \___/|_____| |_|     |_| \___/ \___/|_____|____/ \___/_/\_\


from JMEAnalysis.JetToolbox.jetToolbox_cff import *
#jetToolbox( process, jetType, jetSequence, outputFile,
#	            newPFCollection=False, nameNewPFCollection = '',
#               PUMethod='CHS',                    #### Options: Puppi, CS, SK, Plain
#               JETCorrPayload='None', JETCorrLevels = [ 'None' ],
#               subJETCorrPayload='None', subJETCorrLevels = [ 'None' ],
#               miniAOD=True,
#               Cut = '',
#               addPruning=False, zCut=0.1, rCut=0.5, addPrunedSubjets=False,
#               addSoftDrop=False, betaCut=0.0,  zCutSD=0.1, addSoftDropSubjets=False,
#               addTrimming=False, rFiltTrim=0.2, ptFrac=0.03,
#               addFiltering=False, rfilt=0.3, nfilt=3,
#               addCMSTopTagger=False,
#               addMassDrop=False,
#               addHEPTopTagger=False,
#               addNsub=False, maxTau=4,
#               addQJets=False
#               ):
for name, params in jetsCollectionsSorted.items():
	for index, pu_method in enumerate(params['pu_methods']):
		# Add the jet collection
		if pu_method=='Puppi':
			process.load('CommonTools.PileupAlgos.Puppi_cff')
			#process.puppiOnTheFly = process.puppi.clone()
			#process.puppiOnTheFly.useExistingWeights = True
			process.puppi.useExistingWeights = True
			process.puppi.candName = "packedPFCandidates"
			process.puppi.vertexName = "offlineSlimmedPrimaryVertices"
			jetToolbox(process, params['algo'], 'dummy', 'out', PUMethod = pu_method, JETCorrPayload = params['jec_payloads'][index], JETCorrLevels = params['jec_levels'], miniAOD = True, newPFCollection=True, nameNewPFCollection='puppi')#nameNewPFCollection='puppiOnTheFly')#
		else:
			jetToolbox(process, params['algo'], 'dummy', 'out', PUMethod = pu_method, JETCorrPayload = params['jec_payloads'][index], JETCorrLevels = params['jec_levels'], miniAOD = True)


		PUSuffix = ''
		for c in params['jec_levels']:
			PUSuffix += c[:2]
		PUSuffix = PUSuffix.lower()

		algorithm = params['algo'].upper()+'PF'+pu_method+PUSuffix.upper()
		jetCollection = 'selectedPatJets'+params['algo'].upper()+'PF'+pu_method

		vtxCol = 'offlineSlimmedPrimaryVertices'

		PileupNtupleMakerParameters = cms.PSet(
			# record flavor information, consider both RefPt and JetPt
			doComposition   = cms.bool(True),
			doFlavor        = cms.bool(True),
			doRefPt         = cms.bool(True),
			doJetPt         = cms.bool(True),
			# MATCHING MODE: deltaR(ref,jet)
			deltaRMax       = cms.double(99.9),
			# deltaR(ref,parton) IF doFlavor is True
			deltaRPartonMax = cms.double(0.25),
			# consider all matched references
			nJetMax         = cms.uint32(0),
			)


		pnm = cms.EDAnalyzer('pileupTreeMaker',
							 PileupNtupleMakerParameters,
							 srcJet            = cms.InputTag(jetCollection),
							 srcRho            = cms.InputTag('fixedGridRhoFastjetAll'),
							 srcVtx            = cms.InputTag(vtxCol),
							 srcMuons          = cms.InputTag('slimmedMuons'),
							 srcPuppuMuIso_Combined = cms.InputTag("PUPPIMuonRelIso","PuppiCombined" ,"JRA"),
							 srcPuppuMuIso_Combined_CH = cms.InputTag("PUPPIMuonRelIso","PuppiCombinedCH" ,"JRA"),
							 srcPuppuMuIso_Combined_NH = cms.InputTag("PUPPIMuonRelIso","PuppiCombinedNH" ,"JRA"),
							 srcPuppuMuIso_Combined_PH = cms.InputTag("PUPPIMuonRelIso","PuppiCombinedPH" ,"JRA"),
							 srcPuppuMuIso_WithLep = cms.InputTag("PUPPIMuonRelIso","PuppiWithLepton","JRA"),
							 srcPuppuMuIso_WithLep_CH = cms.InputTag("PUPPIMuonRelIso","PuppiWithLeptonCH","JRA"),
							 srcPuppuMuIso_WithLep_NH = cms.InputTag("PUPPIMuonRelIso","PuppiWithLeptonNH","JRA"),
							 srcPuppuMuIso_WithLep_PH = cms.InputTag("PUPPIMuonRelIso","PuppiWithLeptonPH","JRA"),
							 srcPuppuMuIso_WithoutLep = cms.InputTag("PUPPIMuonRelIso","PuppiWithoutLepton","JRA"),
							 srcPuppuMuIso_WithoutLep_CH = cms.InputTag("PUPPIMuonRelIso","PuppiWithLeptonPH","JRA"),
							 srcPuppuMuIso_WithoutLep_NH = cms.InputTag("PUPPIMuonRelIso","PuppiWithoutLeptonNH","JRA"),
							 srcPuppuMuIso_WithoutLep_PH = cms.InputTag("PUPPIMuonRelIso","PuppiWithoutLeptonPH","JRA"),
							 srcMET = cms.InputTag("slimmedMETs"),
							 srcMETNoHF = cms.InputTag("slimmedMETsNoHF"),
							 srcPuppiMET = cms.InputTag("slimmedMETsPuppi")
							)

		setattr(process,algorithm,pnm)
		sequence = cms.Sequence(process.PUPPIMuonRelIso*pnm)

		sequence = cms.Sequence(sequence)
		setattr(process, algorithm + 'Sequence', sequence)
		path = process.p.copy()
		path *= sequence
		setattr(process, algorithm + 'Path', path)
		print str(bcolors.BFAIL+"{:<15}"+bcolors.BWARNING+" {:<30}"+bcolors.BOKGREEN+" {:<30}"+bcolors.ENDC).format(algorithm,jetCollection,params['jec_levels'])

#!
#! THAT'S ALL! CAN YOU BELIEVE IT? :-D
#!
