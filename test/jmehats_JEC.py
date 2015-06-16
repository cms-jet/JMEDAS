#! Text To ASCII from http://patorjk.com/software/taag/#p=display&f=Big&t=MUON%20ISOLATION

import FWCore.ParameterSet.Config as cms

#!       _ ______ _______            _____  ______ ______ ______ _____  ______ _   _  _____ ______   _  _______ _   _ ______ __  __       _______ _____ _____    _____ _    _ _______ _____ 
#!      | |  ____|__   __|   ___    |  __ \|  ____|  ____|  ____|  __ \|  ____| \ | |/ ____|  ____| | |/ /_   _| \ | |  ____|  \/  |   /\|__   __|_   _/ ____|  / ____| |  | |__   __/ ____|
#!      | | |__     | |     ( _ )   | |__) | |__  | |__  | |__  | |__) | |__  |  \| | |    | |__    | ' /  | | |  \| | |__  | \  / |  /  \  | |    | || |      | |    | |  | |  | | | (___  
#!  _   | |  __|    | |     / _ \/\ |  _  /|  __| |  __| |  __| |  _  /|  __| | . ` | |    |  __|   |  <   | | | . ` |  __| | |\/| | / /\ \ | |    | || |      | |    | |  | |  | |  \___ \ 
#! | |__| | |____   | |    | (_>  < | | \ \| |____| |    | |____| | \ \| |____| |\  | |____| |____  | . \ _| |_| |\  | |____| |  | |/ ____ \| |   _| || |____  | |____| |__| |  | |  ____) |
#!  \____/|______|  |_|     \___/\/ |_|  \_\______|_|    |______|_|  \_\______|_| \_|\_____|______| |_|\_\_____|_| \_|______|_|  |_/_/    \_\_|  |_____\_____|  \_____|\____/   |_| |_____/ 

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
 
#!  _____  _____   ____   _____ ______  _____ _____ 
#! |  __ \|  __ \ / __ \ / ____|  ____|/ ____/ ____|
#! | |__) | |__) | |  | | |    | |__  | (___| (___  
#! |  ___/|  _  /| |  | | |    |  __|  \___ \\___ \ 
#! | |    | | \ \| |__| | |____| |____ ____) |___) |
#! |_|    |_|  \_\\____/ \_____|______|_____/_____/ 

process = cms.Process("JRA")
applyDBFile = False
era = 'PHYS14_V4_MC'
doJetToolbox = True
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.options.allowUnscheduled = cms.untracked.bool(True)
doMiniAOD = True

#!  _____ _   _ _____  _    _ _______ 
#! |_   _| \ | |  __ \| |  | |__   __|
#!   | | |  \| | |__) | |  | |  | |   
#!   | | | . ` |  ___/| |  | |  | |   
#!  _| |_| |\  | |    | |__| |  | |   
#! |_____|_| \_|_|     \____/   |_|                                       

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(1000))
if doMiniAOD:
	process.load("Analysis.JMEDAS.qcdflat_MINIAODSIM_cff")
else:
	process.load("Analysis.JMEDAS.qcdflat_AODSIM_cff")

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
process.MessageLogger.cerr.FwkReport.reportEvery = 500
process.load('CommonTools.UtilAlgos.TFileService_cfi')
process.TFileService.fileName=cms.string('JECNtuple.root')

#!           _      _____  ____  _____  _____ _______ _    _ __  __  _____ 
#!     /\   | |    / ____|/ __ \|  __ \|_   _|__   __| |  | |  \/  |/ ____|
#!    /  \  | |   | |  __| |  | | |__) | | |    | |  | |__| | \  / | (___  
#!   / /\ \ | |   | | |_ | |  | |  _  /  | |    | |  |  __  | |\/| |\___ \ 
#!  / ____ \| |___| |__| | |__| | | \ \ _| |_   | |  | |  | | |  | |____) |
#! /_/    \_\______\_____|\____/|_|  \_\_____|  |_|  |_|  |_|_|  |_|_____/                                                                        
jcr = cms.VPSet()
jetsCollections = {
        'AK4': {
		'algo': 'ak4',
#		'pu_methods': ['Puppi', 'CHS', ''],
		'pu_methods': ['CHS', ''],
#		'jec_payloads': ['AK4PFPUPPI', 'AK4PFchs', 'AK4PF'],
		'jec_payloads': ['AK4PFchs', 'AK4PF'],
#		'jec_levels': ['L1FastJet', 'L2Relative', 'L3Absolute']
		'jec_levels': []
		},

        'AK8': {
		'algo': 'ak8',
#		'pu_methods': ['Puppi', 'CHS', ''],
		'pu_methods': ['CHS', ''],
#		'jec_payloads': ['AK8PFPUPPI', 'AK8PFchs', 'AK8PF'],
		'jec_payloads': ['AK8PFchs', 'AK8PF'],
#		'jec_levels': ['L1FastJet', 'L2Relative', 'L3Absolute']
		'jec_levels': []
		},
	}

for name, params in jetsCollections.items():
	for index, pu_method in enumerate(params['pu_methods']):
		jcr.append(cms.PSet(record = cms.string("JetCorrectionsRecord"),
				    tag = cms.string("JetCorrectorParametersCollection_"+era+"_"+params['jec_payloads'][index]),
				    label= cms.untracked.string(params['jec_payloads'][index])))

#!   _____ ____  _   _ _____ _____ _______ _____ ____  _   _  _____ 
#!  / ____/ __ \| \ | |  __ \_   _|__   __|_   _/ __ \| \ | |/ ____|
#! | |   | |  | |  \| | |  | || |    | |    | || |  | |  \| | (___  
#! | |   | |  | | . ` | |  | || |    | |    | || |  | | . ` |\___ \ 
#! | |___| |__| | |\  | |__| || |_   | |   _| || |__| | |\  |____) |
#!  \_____\____/|_| \_|_____/_____|  |_|  |_____\____/|_| \_|_____/ 
                                                                  
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "MCRUN2_74_V7::All"
if applyDBFile:
        from CondCore.DBCommon.CondDBSetup_cfi import *
        process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
                                   connect = cms.string('sqlite_file:'+era+'.db'),
                                   #cms.string("frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS"),
                                   toGet =  cms.VPSet(jcr))
        process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")

#      _ _____ _____   _____ ___   ___  _     ____   _____  __
#     | | ____|_   _| |_   _/ _ \ / _ \| |   | __ ) / _ \ \/ /
#  _  | |  _|   | |     | || | | | | | | |   |  _ \| | | \  / 
# | |_| | |___  | |     | || |_| | |_| | |___| |_) | |_| /  \ 
#  \___/|_____| |_|     |_| \___/ \___/|_____|____/ \___/_/\_\
                                                             

from JMEAnalysis.JetToolbox.jetToolbox_cff import *
#jetToolbox( process, jetType, jetSequence, outputFile,
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
if doJetToolbox:
	for name, params in jetsCollections.items():
		for index, pu_method in enumerate(params['pu_methods']):
			# Add the jet collection
			if len(params['jec_levels'])>0:
				jetToolbox(process, params['algo'], 'dummy', 'out', PUMethod = pu_method, JETCorrPayload = params['jec_payloads'][index], JETCorrLevels = params['jec_levels'], miniAOD = doMiniAOD)
			else:
				jetToolbox(process, params['algo'], 'dummy', 'out', PUMethod = pu_method, miniAOD = doMiniAOD)
elif not doJetToolbox and doMiniAOD:
	# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015#Advanced_topics_re_clustering_ev
	from Analysis.JMEDAS.JetReconstruction_cff import *
	
	## Filter out neutrinos from packed GenParticles
	process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16"))

	for name, params in jetsCollections.items():
		for index, pu_method in enumerate(params['pu_methods']):
			#################################################
			## Remake jets
			#################################################

			## Define GenJets
			eval(params['algo']+'GenJetsNoNu').src = 'packedGenParticlesForJetsNoNu'

			if pu_method == 'CHS':
				## Select charged hadron subtracted packed PF candidates
				process.pfCHS = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedPFCandidates"), cut = cms.string("fromPV"))

				## Define PFJetsCHS
				eval(params['algo']+'PFJets'+pu_method).src = 'pfCHS'
				eval(params['algo']+'PFJets'+pu_method).doAreaFastjet = True
			elif pu_method == '':
				eval(params['algo']+'PFJets'+pu_method).src = 'packedPFCandidates'

			#################################################
			## Remake PAT jets
			#################################################
	
			## b-tag discriminators
			bTagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags']

			from PhysicsTools.PatAlgos.tools.jetTools import *
			from itertools import groupby
			## Add PAT jet collection based on the above-defined ak5PFJetsCHS
			if len(params['jec_levels'])>0:
				addJetCollection(
					process,
					labelName = params['algo'].upper()+'PF'+pu_method,
					jetSource = cms.InputTag(params['algo']+'PFJets'+pu_method),
					pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
					pfCandidates = cms.InputTag('packedPFCandidates'),
					svSource = cms.InputTag('slimmedSecondaryVertices'),
					btagDiscriminators = bTagDiscriminators,
					jetCorrections = (params['algo'].upper()+'PF'+pu_method.replace("CHS","chs"), params['jec_levels'], 'None'),
					genJetCollection = cms.InputTag(params['algo']+'GenJetsNoNu'),
					genParticles = cms.InputTag('prunedGenParticles'),
					algo = [''.join(g) for _, g in groupby(params['algo'], str.isalpha)][0].upper(),
					rParam = float([''.join(g) for _, g in groupby(params['algo'], str.isalpha)][1])/10.0
					)
			else:
				addJetCollection(
					process,
					labelName = params['algo'].upper()+'PF'+pu_method,
					jetSource = cms.InputTag(params['algo']+'PFJets'+pu_method),
					pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
					pfCandidates = cms.InputTag('packedPFCandidates'),
					svSource = cms.InputTag('slimmedSecondaryVertices'),
					btagDiscriminators = bTagDiscriminators,
					genJetCollection = cms.InputTag(params['algo']+'GenJetsNoNu'),
					genParticles = cms.InputTag('prunedGenParticles'),
					algo = [''.join(g) for _, g in groupby(params['algo'], str.isalpha)][0].upper(),
					rParam = float([''.join(g) for _, g in groupby(params['algo'], str.isalpha)][1])/10.0
					)
	
			getattr(process,'selectedPatJets'+params['algo'].upper()+'PF'+pu_method).cut = cms.string('pt > 10')
			setattr(process,params['algo']+'PFJets'+pu_method,eval(params['algo']+'PFJets'+pu_method))
			setattr(process,params['algo']+'GenJetsNoNu',eval(params['algo']+'GenJetsNoNu'))
else:
	print "ERROR::Not equipped to handle AODSIM without PAT."
	exit(0)

#           _   _          _  __     ______________ _____  
#     /\   | \ | |   /\   | | \ \   / /___  /  ____|  __ \ 
#    /  \  |  \| |  /  \  | |  \ \_/ /   / /| |__  | |__) |
#   / /\ \ | . ` | / /\ \ | |   \   /   / / |  __| |  _  / 
#  / ____ \| |\  |/ ____ \| |____| |   / /__| |____| | \ \ 
# /_/    \_\_| \_/_/    \_\______|_|  /_____|______|_|  \_\


process.p = cms.Path()
print "{:<15} {:<20} {:<30}".format('Algorithm','Jet Collection',"Correction Levels")
print "{:<15} {:<20} {:<30}".format('---------','--------------',"-----------------")
for name, params in jetsCollections.items():
	for index, pu_method in enumerate(params['pu_methods']):
		PUSuffix = ''
		for c in params['jec_levels']:
			PUSuffix += c[:2]
		PUSuffix = PUSuffix.lower()

		algorithm = params['algo'].upper()+'PF'+pu_method+PUSuffix
		jetCollection = 'selectedPatJets'+params['algo'].upper()+'PF'+pu_method
		if doMiniAOD:
			vtxCol = 'offlineSlimmedPrimaryVertices'
		else:
			vtxCol = 'offlinePrimaryVertices'
		pnm = cms.EDAnalyzer('treeMaker',
				     PileupNtupleMakerParameters,
				     JetCorLabel       = cms.string(algorithm),
				     JetCorLevels      = cms.vstring(params['jec_levels']),
				     srcJet            = cms.InputTag(jetCollection),
				     srcRho            = cms.InputTag('fixedGridRhoAll'),
				     srcVtx            = cms.InputTag(vtxCol),
				     doJER             = cms.bool(False),
				     JERUncertainty    = cms.string("none"), #Options: {none,up,down}
				     doJESUncertainty  = cms.bool(False),
				     JESUncertainty    = cms.string("none"), #Options: {none,up,down}
				     JESUncertaintyType= cms.string("TotalNoTime"),
				     JESUncertaintyFile= cms.string("../data/Winter14_V5_DATA_UncertaintySources_AK5PFchs.txt"),
				     )
		setattr(process,algorithm,pnm)
		sequence = cms.Sequence(pnm)
		
		sequence = cms.Sequence(sequence)
		setattr(process, algorithm + 'Sequence', sequence)
		path = process.p.copy()
		if doJetToolbox:
			path *= sequence
		elif not doJetToolbox and doMiniAOD:
			path *= eval(params['algo']+'GenJetsNoNu') * eval(params['algo']+'PFJets'+pu_method) * getattr(process, 'selectedPatJets'+params['algo'].upper()+'PF'+pu_method) * sequence
		else:
			print "ERROR::Not equipped to handle AODSIM without PAT."
			exit(0)
		setattr(process, algorithm + 'Path', path)
		print "{:<15} {:<20} {:<30}".format(algorithm,jetCollection,params['jec_levels'])

#!
#! THAT'S ALL! CAN YOU BELIEVE IT? :-D
#!
