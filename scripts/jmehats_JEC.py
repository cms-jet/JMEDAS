#! Text To ASCII from http://patorjk.com/software/taag/#p=display&f=Big&t=MUON%20ISOLATION

import FWCore.ParameterSet.Config as cms
import FWCore.ParameterSet.VarParsing as VarParsing
import collections
from Analysis.JMEDAS.colors import bcolors
from itertools import groupby
from optparse import OptionParser
 
#!   ____  _____ _______ _____ ____  _   _  _____ 
#!  / __ \|  __ \__   __|_   _/ __ \| \ | |/ ____|
#! | |  | | |__) | | |    | || |  | |  \| | (___  
#! | |  | |  ___/  | |    | || |  | | . ` |\___ \ 
#! | |__| | |      | |   _| || |__| | |\  |____) |
#!  \____/|_|      |_|  |_____\____/|_| \_|_____/ 

'''
How to pass command line arguments can be found at:
https://twiki.cern.ch/twiki/bin/view/CMSPublic/SWGuideAboutPythonConfigFile#Passing_Command_Line_Arguments_T
'''
options = VarParsing.VarParsing()

options.register('applyDBFile',
				 0, # default value, use integer for boolean flags (1 = True, 0 = False) 
                 VarParsing.VarParsing.multiplicity.singleton, # singleton or list
                 VarParsing.VarParsing.varType.int,          # string, int, or float
                 "Take the JEC not from a global tag or text files, but from an SQLite file.")
options.register('doMiniAOD',
                 1,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'If true, will use a MiniAOD sample as opposed to an AODSIM sample.')
options.register('doJetToolbox',
                 0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'If true, will use the JetToolbox to recluster the jets and apply the JEC.')
options.register('doReclustering',
                 0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'If true, will recluster the jets as opposed to taking them from the MC samples.')
options.register('useUpdater',
                 0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'If true, the jets taken from the MiniAOD sample and not reclustered will have new JEC applied.')
options.register('era',
                 'Spring16_25nsV3_MC',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'The era of the JEC. Used when accessing an SQLite file or a series of text files.')
options.register('jerfile',
                 'none',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'The path to a text file containing the JER scale factors. Used when applying them on-the-fly.')
options.register('UncertaintyOTF',
                 0,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'Controls whether or not the uncertainties are done on-the-fly (1) or using EDProducers (0).')
options.register('JERUncertainty',
                 'none',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'Controls the type of JER smearing, including the systematic uncertainties. The options are: {none,nominal,up,down}')
options.register('JESUncertainty',
                 'none',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'Controls whether of not the JES uncertainties are applied. The options are: {none,up,down}')
options.register('ofilename',
                 'JECNtuple.root',
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.string,
                 'The name of the output ROOT file.')
options.register('maxEvents',
                 1000,
                 VarParsing.VarParsing.multiplicity.singleton,
                 VarParsing.VarParsing.varType.int,
                 'The maximum number of events to process.')

options.parseArguments()

#Check the options
if options.doJetToolbox and not options.doReclustering:
	print bcolors.FAIL+"ERROR::In order to use the JetToolbox you must be willing to recluster your jets."+bcolors.ENDC
	exit(-4)
elif options.useUpdater and not options.doMiniAOD and not options.doJetToolbox:
	print bcolors.FAIL+"ERROR::Right now only reco::Jets come out of the PFBRECO method."+bcolors.ENDC
	print bcolors.FAIL+"\tThe patJetUpdater can't use reco::Jets and can onlyuse as input pat::Jets"+bcolors.ENDC
	exit(-5)
elif options.doMiniAOD and options.doReclustering and options.useUpdater:
	print bcolors.FAIL+"ERROR::This option will already have the latest corrections applied."+bcolors.ENDC
	print bcolors.FAIL+"\tNo need to use the patJetUpdater."+bcolors.ENDC
	exit(-6)
elif not options.doMiniAOD and options.doReclustering and options.useUpdater:
	print bcolors.FAIL+"ERROR::This option will already have the latest corrections applied."+bcolors.ENDC
	print bcolors.FAIL+"\tNo need to use the patJetUpdater."+bcolors.ENDC
	exit(-7)

#!  _____  _____   ____   _____ ______  _____ _____ 
#! |  __ \|  __ \ / __ \ / ____|  ____|/ ____/ ____|
#! | |__) | |__) | |  | | |    | |__  | (___| (___  
#! |  ___/|  _  /| |  | | |    |  __|  \___ \\___ \ 
#! | |    | | \ \| |__| | |____| |____ ____) |___) |
#! |_|    |_|  \_\\____/ \_____|______|_____/_____/ 

process = cms.Process("JRA")
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(False) )
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
process.MessageLogger.cerr.FwkReport.reportEvery = 500
process.load('CommonTools.UtilAlgos.TFileService_cfi')
process.TFileService.fileName=cms.string(options.ofilename)

#!  _____ _   _ _____  _    _ _______ 
#! |_   _| \ | |  __ \| |  | |__   __|
#!   | | |  \| | |__) | |  | |  | |   
#!   | | | . ` |  ___/| |  | |  | |   
#!  _| |_| |\  | |    | |__| |  | |   
#! |_____|_| \_|_|     \____/   |_|                                       

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(options.maxEvents))
if options.doMiniAOD:
	process.load("Analysis.JMEDAS.qcdflat_MINIAODSIM_v5_cff")
else:
	process.load("Analysis.JMEDAS.qcdflat_AODSIM_v5_cff")

#!           _      _____  ____  _____  _____ _______ _    _ __  __  _____ 
#!     /\   | |    / ____|/ __ \|  __ \|_   _|__   __| |  | |  \/  |/ ____|
#!    /  \  | |   | |  __| |  | | |__) | | |    | |  | |__| | \  / | (___  
#!   / /\ \ | |   | | |_ | |  | |  _  /  | |    | |  |  __  | |\/| |\___ \ 
#!  / ____ \| |___| |__| | |__| | | \ \ _| |_   | |  | |  | | |  | |____) |
#! /_/    \_\______\_____|\____/|_|  \_\_____|  |_|  |_|  |_|_|  |_|_____/                                                                        
jcr = cms.VPSet()
jrr = cms.VPSet()
jetsCollections = {
	'AK4L1L2L3': 	{
					'algo': 'ak4',
					'pu_methods': ['','CHS','Puppi'], #Options: {Puppi,CHS,''}
					'jec_payloads': ['AK4PF','AK4PFchs','AK4PFPuppi'], #Options: {AK4PFPuppi,AK4PFchs,AK4PF,AK8Calo,AK8JPT}
					'jec_levels': ['L1FastJet', 'L2Relative', 'L3Absolute'], #Options: {L1FastJet,L2Relative,L3Absolute,L2L3Residual,L5Flavor,L7Parton}
					},
	'AK8L1L2L3': 	{
					'algo': 'ak8',
					'pu_methods': ['','CHS','Puppi'], #Options: {Puppi,CHS,''}
					'jec_payloads': ['AK8PF','AK8PFchs','AK8PFPuppi'], #Options: {AK8PFPuppi,AK8PFchs,AK8PF,AK8Calo,AK8JPT}
					'jec_levels': ['L1FastJet', 'L2Relative', 'L3Absolute'], #Options: {L1FastJet,L2Relative,L3Absolute,L2L3Residual,L5Flavor,L7Parton}
					},
				  }
jetsCollectionsSorted = collections.OrderedDict(sorted(jetsCollections.items(), key=lambda x:x[0], reverse=False))

#Check for multiple collections of the same cone size
csCounter = {}
for name, params in jetsCollectionsSorted.items():
	if params['algo'] not in csCounter:
		csCounter[params['algo']] = 1
	else:
		csCounter[params['algo']]+=1
if any(v > 1 for v in csCounter.itervalues()):
	print bcolors.FAIL+"NOTE: This code has a problem running multiple collections of the same cone size."+bcolors.ENDC
	print "\tPlease choose one!"
	exit(-3)

maxA = maxJC = maxJP = maxCL = 0
for name, params in jetsCollections.items():
	maxCL = len(str(params['jec_levels'])) if len(str(params['jec_levels'])) > maxCL else maxCL
	for index, pu_method in enumerate(params['pu_methods']):
		PUSuffix = ''
		for c in params['jec_levels']:
			PUSuffix += c[:2]
		PUSuffix = PUSuffix.lower()
		maxJC = len('selectedPatJets'+params['algo'].upper()+'PF'+pu_method) if len('selectedPatJets'+params['algo'].upper()+'PF'+pu_method) > maxJC else maxJC
		maxA = len(params['algo'].upper()+'PF'+pu_method+PUSuffix.upper()) if len(params['algo'].upper()+'PF'+pu_method+PUSuffix.upper()) > maxA else maxA
		maxJP = len(params['jec_payloads'][index]) if len(params['jec_payloads'][index]) > maxJP else maxJP 

		jcr.append(cms.PSet(record = cms.string("JetCorrectionsRecord"),
				   			tag = cms.string("JetCorrectorParametersCollection_"+options.era+"_"+params['jec_payloads'][index]),
				   			label = cms.untracked.string(params['jec_payloads'][index])))

		JERera = options.jerfile.split('/')[-1]
		jrr.append(cms.PSet(record = cms.string('JetResolutionRcd'),
		            		tag = cms.string('JR_'+JERera+'_PtResolution_AK4PFchs'),
		            		label = cms.untracked.string(params['jec_payloads'][index]+'_pt')))
		jrr.append(cms.PSet(record = cms.string('JetResolutionScaleFactorRcd'),
                    		tag    = cms.string('JR_'+JERera+'_SF_'+params['jec_payloads'][index]),
                    		label  = cms.untracked.string(params['jec_payloads'][index])))

		if options.doMiniAOD and not options.doReclustering:
			doExit = False
			if not any(alg in params['algo'] for alg in ['ak4','ak8']):
				print bcolors.FAIL+"ERROR::Can't continue because doReclustering is set to False and the 2017 MiniAOD files only contain AK4 and AK8 jets"+bcolors.ENDC
				doExit = True
			if params['algo'] == 'ak4' and not any(pu in pu_method for pu in ['CHS','Puppi']):
				print bcolors.FAIL+"ERROR::Can't continue because doReclustering is set to False and the 2017 MiniAOD files only have AK4 jets using CHS or PFPuppi"+bcolors.ENDC
				doExit = True
			if params['algo'] == 'ak8' and pu_method!='Puppi':
				print bcolors.FAIL+"ERROR::Can't continue because doReclustering is set to False and the 2017 MiniAOD files only have AK8 jets using Puppi"+bcolors.ENDC
				doExit = True
			if doExit:
				exit(-1)

maxA = max(maxA,len("Algorithm"))
maxJC = max(maxJC,len("Jet Collection"))
maxJP = max(maxJP,len("JEC Payload"))
maxCL = max(maxCL,len("Correction Levels"))

#!   _____ ____  _   _ _____ _____ _______ _____ ____  _   _  _____ 
#!  / ____/ __ \| \ | |  __ \_   _|__   __|_   _/ __ \| \ | |/ ____|
#! | |   | |  | |  \| | |  | || |    | |    | || |  | |  \| | (___  
#! | |   | |  | | . ` | |  | || |    | |    | || |  | | . ` |\___ \ 
#! | |___| |__| | |\  | |__| || |_   | |   _| || |__| | |\  |____) |
#!  \_____\____/|_| \_|_____/_____|  |_|  |_____\____/|_| \_|_____/ 
																  
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff")
process.GlobalTag.globaltag = cms.string('80X_mcRun2_asymptotic_2016_TrancheIV_v8')
if options.applyDBFile:
	from CondCore.DBCommon.CondDBSetup_cfi import *
	process.jec = cms.ESSource("PoolDBESSource",CondDBSetup,
							   connect = cms.string('sqlite_file:../data/JECs/'+options.era+'.db'),
							   #cms.string("frontier://FrontierPrep/CMS_COND_PHYSICSTOOLS"),
							   toGet =  cms.VPSet(jcr))
	process.es_prefer_jec = cms.ESPrefer("PoolDBESSource","jec")

	if not options.jerfile == 'none':
		process.jer = cms.ESSource("PoolDBESSource",CondDBSetup,
								   connect = cms.string('sqlite_file:../data/JERs/'+options.jerfile+'.db'),
								   toGet = cms.VPSet(jrr))	
		process.es_prefer_jer = cms.ESPrefer("PoolDBESSource","jer")

#      _ _____ _____   _____ ___   ___  _     ____   _____  __
#     | | ____|_   _| |_   _/ _ \ / _ \| |   | __ ) / _ \ \/ /
#  _  | |  _|   | |     | || | | | | | | |   |  _ \| | | \  / 
# | |_| | |___  | |     | || |_| | |_| | |___| |_) | |_| /  \ 
#  \___/|_____| |_|     |_| \___/ \___/|_____|____/ \___/_/\_\
															 

from Analysis.JetToolbox.jetToolbox_cff import *
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
if options.doJetToolbox:
	for name, params in jetsCollectionsSorted.items():
		for index, pu_method in enumerate(params['pu_methods']):
			# Add the jet collection
			nPFc = False
			nNPFc = ''
			if pu_method=='Puppi' and options.doMiniAOD:
				process.load('CommonTools.PileupAlgos.Puppi_cff')
				#This will speed up the processing of PUPPI by using the pre-existing weights in MiniAOD
				process.puppi.useExistingWeights = True
				process.puppi.candName = "packedPFCandidates"
				process.puppi.vertexName = "offlineSlimmedPrimaryVertices"
				nPFc = True
				nNPFc = 'puppi'
			if len(params['jec_levels'])>0:
				jetToolbox(process, params['algo'], 'dummy', 'out', newPFCollection = nPFc, nameNewPFCollection = nNPFc, PUMethod = pu_method, JETCorrPayload = params['jec_payloads'][index], JETCorrLevels = params['jec_levels'], miniAOD = options.doMiniAOD)
			else:
				jetToolbox(process, params['algo'], 'dummy', 'out', newPFCollection = nPFc, nameNewPFCollection = nNPFc, PUMethod = pu_method, miniAOD = options.doMiniAOD)

elif not options.doJetToolbox and options.doMiniAOD and options.doReclustering:
	# https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2015#Advanced_topics_re_clustering_ev
	from Analysis.JMEDAS.JetReconstruction_cff import *
	
	## Filter out neutrinos from packed GenParticles
	process.packedGenParticlesForJetsNoNu = cms.EDFilter("CandPtrSelector", src = cms.InputTag("packedGenParticles"), cut = cms.string("abs(pdgId) != 12 && abs(pdgId) != 14 && abs(pdgId) != 16"))

	for name, params in jetsCollectionsSorted.items():
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
			elif pu_method == 'Puppi':
				process.load('CommonTools.PileupAlgos.Puppi_cff')
				#This will speed up the processing of PUPPI by using the pre-existing weights in MiniAOD
				process.puppi.useExistingWeights = True
				process.puppi.candName = "packedPFCandidates"
				process.puppi.vertexName = "offlineSlimmedPrimaryVertices"
			elif pu_method == '':
				eval(params['algo']+'PFJets'+pu_method).src = 'packedPFCandidates'

			#################################################
			## Remake PAT jets
			#################################################
	
			## b-tag discriminators
			bTagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags']

			from PhysicsTools.PatAlgos.tools.jetTools import *
			## Add PAT jet collection based on the above-defined jet collection
			if len(params['jec_levels'])>0:
				jetCorrectionsParameter = (params['algo'].upper()+'PF'+pu_method.replace("CHS","chs"), params['jec_levels'], 'None')
			else:
				jetCorrectionsParameter = None

			addJetCollection(process,
							 labelName = params['algo'].upper()+'PF'+pu_method,
							 jetSource = cms.InputTag(params['algo']+'PFJets'+pu_method),
							 pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
							 pfCandidates = cms.InputTag('packedPFCandidates'),
							 svSource = cms.InputTag('slimmedSecondaryVertices'),
							 btagDiscriminators = bTagDiscriminators,
							 jetCorrections = jetCorrectionsParameter,
							 genJetCollection = cms.InputTag(params['algo']+'GenJetsNoNu'),
							 genParticles = cms.InputTag('prunedGenParticles'),
							 algo = [''.join(g) for _, g in groupby(params['algo'], str.isalpha)][0].upper(),
							 rParam = float([''.join(g) for _, g in groupby(params['algo'], str.isalpha)][1])/10.0
							 )
	
			getattr(process,'selectedPatJets'+params['algo'].upper()+'PF'+pu_method).cut = cms.string('pt > 10')
			setattr(process,params['algo']+'PFJets'+pu_method,eval(params['algo']+'PFJets'+pu_method))
			setattr(process,params['algo']+'GenJetsNoNu',eval(params['algo']+'GenJetsNoNu'))
elif not options.doJetToolbox and options.doMiniAOD and not options.doReclustering:
	print bcolors.WARNING+"NOTE: These jets will be taken straight from the MiniAOD file."+bcolors.ENDC
else:
	if not options.doReclustering:
		print bcolors.WARNING+"NOTE: The way this method is implemented only works with reclustering on."+bcolors.ENDC
		exit(-2)

	process.load('CommonTools.ParticleFlow.pfNoPileUpJME_cff')
	process.pfPileUp.checkClosestZVertex = False
	from Analysis.JMEDAS.JetReconstruction_cff import *
	from Analysis.JMEDAS.JetCorrection_cff     import *
	from CommonTools.PileupAlgos.Puppi_cff import *
	process.load('Analysis.JMEDAS.JetCorrection_cff')

	for name, params in jetsCollectionsSorted.items():
		for index, pu_method in enumerate(params['pu_methods']):

			#Gen Particle
			setattr(process,'genParticlesForJetsNoNu',genParticlesForJetsNoNu)
			sequence = cms.Sequence(genParticlesForJetsNoNu)

			#Algo Specific
			if pu_method == 'Puppi':
				process.load('CommonTools.PileupAlgos.Puppi_cff')
				sequence = cms.Sequence(sequence * puppi)
			elif pu_method == 'CHS':
				sequence = cms.Sequence(process.pfNoPileUpJMESequence * sequence)

			#Gen Jets
			setattr(process, params['algo']+"GenJetsNoNu", eval(params['algo']+"GenJetsNoNu"))
			sequence = cms.Sequence(sequence * eval(params['algo']+"GenJetsNoNu"))

			#Rec Jets
			eval(params['algo']+"PFJets"+pu_method).jetPtMin = cms.double(3.0)
			setattr(process, params['algo']+"PFJets"+pu_method, eval(params['algo']+"PFJets"+pu_method))
			sequence = cms.Sequence(sequence * eval(params['algo']+"PFJets"+pu_method))

			PUSuffix = ''
			for c in params['jec_levels']:
				PUSuffix += c[:2]
			PUSuffix = PUSuffix.replace('L1','L1Fast')

			if len(params['jec_levels'])>0:
				#Cor Rec Jets
				setattr(process, params['algo']+"PFJets"+pu_method+PUSuffix, eval(params['algo']+"PFJets"+pu_method+PUSuffix))
				sequence = cms.Sequence(sequence * eval(params['algo']+"PFJets"+pu_method+PUSuffix))

			#Ref Jet Kinematics
			refPtEta = cms.EDFilter('EtaPtMinCandViewRefSelector',
				etaMin = cms.double(-5.5),
				etaMax = cms.double(5.5),
				ptMin = cms.double(1.0),
				src = cms.InputTag(params['algo']+"GenJetsNoNu")
			)
			setattr(process, params['algo']+"PFJets"+pu_method+'GenPtEta', refPtEta)
			if not options.doReclustering:
				refPtEta.src = params['algo']+"GenJets"
			sequence = cms.Sequence(sequence * refPtEta)

			#Cor Rec Jet Kinematics
			jetPtEta = cms.EDFilter('EtaPtMinCandViewRefSelector',
				etaMin = cms.double(-5.5),
				etaMax = cms.double(5.5),
				ptMin = cms.double(1.0),
				src = cms.InputTag(params['algo']+"PFJets"+pu_method)
			)
			setattr(process, params['algo']+"PFJets"+pu_method+PUSuffix+'PtEta', jetPtEta)
			if len(params['jec_levels'])>0:	
				jetPtEta.src = params['algo']+"PFJets"+pu_method+PUSuffix
			sequence = cms.Sequence(sequence * jetPtEta)

			setattr(process, params['algo']+"PFJets"+pu_method+PUSuffix + 'Sequence', sequence)

			#################################################
			## Remake PAT jets
			#################################################
			from PhysicsTools.PatAlgos.tools.jetTools import *
			## b-tag discriminators
			bTagDiscriminators = ['pfCombinedInclusiveSecondaryVertexV2BJetTags']
			addJetCollection(process,
							 labelName = params['algo'].upper()+'PF'+pu_method,
							 jetSource = cms.InputTag(params['algo']+'PFJets'+pu_method+PUSuffix+'PtEta'),
							 pvSource = cms.InputTag('offlinePrimaryVertices'),
							 pfCandidates = cms.InputTag('PFCandidates'),
							 svSource = cms.InputTag('SecondaryVertices'),
							 btagDiscriminators = bTagDiscriminators,
							 jetCorrections = None,
							 genJetCollection = cms.InputTag(params['algo']+'GenJetsNoNu'),
							 genParticles = cms.InputTag('genParticlesForJetsNoNu'),
							 algo = [''.join(g) for _, g in groupby(params['algo'], str.isalpha)][0].upper(),
							 rParam = float([''.join(g) for _, g in groupby(params['algo'], str.isalpha)][1])/10.0
							 )
	
			getattr(process,'selectedPatJets'+params['algo'].upper()+'PF'+pu_method).cut = cms.string('pt > 10')

			print "For this to work you will need to convert from reco jets to pat jets, which will contain the gen jets. Otherwise the analyzer will have problems. Right now it's not finding some collections"
			print "You should really use PFBRECO only when your analyzer uses reco::Jets"
			print "ERROR::Not equipped to handle AODSIM without PAT."
			exit(0)

#           _   _          _  __     ______________ _____  
#     /\   | \ | |   /\   | | \ \   / /___  /  ____|  __ \ 
#    /  \  |  \| |  /  \  | |  \ \_/ /   / /| |__  | |__) |
#   / /\ \ | . ` | / /\ \ | |   \   /   / / |  __| |  _  / 
#  / ____ \| |\  |/ ____ \| |____| |   / /__| |____| | \ \ 
# /_/    \_\_| \_/_/    \_\______|_|  /_____|______|_|  \_\

print "{A:<{widthA}s} {JC:<{widthJC}s} {JP:<{widthJP}s} {CL:<{widthCL}s}".format(A='Algorithm',JC='Jet Collection',JP='JEC Payload',CL="Correction Levels",widthA=maxA,widthJC=maxJC,widthJP=maxJP,widthCL=maxCL)
print "{A:<{widthA}s} {JC:<{widthJC}s} {JP:<{widthJP}s} {CL:<{widthCL}s}".format(A='---------',JC='--------------',JP='-----------',CL="-----------------",widthA=maxA,widthJC=maxJC,widthJP=maxJP,widthCL=maxCL)
for name, params in jetsCollectionsSorted.items():
	for index, pu_method in enumerate(params['pu_methods']):
		PUSuffix = ''
		for c in params['jec_levels']:
			PUSuffix += c[:2]
		PUSuffix = PUSuffix.lower()

		algorithm = params['algo'].upper()+'PF'+pu_method+PUSuffix.upper()

		#################################################
		## Controls the sequence
		#################################################
		if hasattr(process, params['algo']+"PFJets"+pu_method+PUSuffix.upper().replace("L1","L1Fast") + 'Sequence'):
			sequence = cms.Sequence(getattr(process,params['algo']+"PFJets"+pu_method+PUSuffix.upper().replace("L1","L1Fast") + 'Sequence') * pnm)
		else:
			sequence = cms.Sequence()
		sequence = cms.Sequence(sequence)
		setattr(process, algorithm + 'Sequence', sequence)

		#################################################
		## Controls the jet collection used in the analyzer
		#################################################
		if options.doJetToolbox:
			jetCollection = 'selectedPatJets'+params['algo'].upper()+'PF'+pu_method
		elif options.doMiniAOD and not options.doReclustering:
			#straight from MiniAOD
			jetCollection = "slimmedJets"
			if params['algo'] == 'ak4' and pu_method == "Puppi":
				jetCollection+= "Puppi"
			elif params['algo'] == 'ak8':
				jetCollection+="AK8"
			#If updated the JEC using the patJetUpdater
			if options.useUpdater:
				from PhysicsTools.PatAlgos.tools.jetTools import updateJetCollection
				updateJetCollection(process,
									jetSource = cms.InputTag(jetCollection),
									postfix = 'UpdatedJEC'+params['jec_payloads'][index],
									jetCorrections = (params['jec_payloads'][index], params['jec_levels'], 'None')
				)
				jetCollection = 'updatedPatJetsUpdatedJEC'+params['jec_payloads'][index]
		elif not options.doMiniAOD and not options.doJetToolbox:
			jetCollection = 'selectedPatJets'+params['algo'].upper()+'PF'+pu_method
			#jetCollection = params['algo']+'PFJets'+pu_method+PUSuffix.upper().replace("L1","L1Fast")

		#################################################
		## Controls the JER and JES used in the analyzer
		#################################################
		from Analysis.JMEDAS.JetDepot import JetDepot

		if not options.UncertaintyOTF:
			if options.JESUncertainty!='none':
				process, jetCollection = JetDepot(process,
												  sequence=algorithm + 'Sequence',
												  JetTag=cms.InputTag(jetCollection),
												  JetType=params['jec_payloads'][index],
												  jecUncDir=1 if options.JESUncertainty=="up" else -1,
												  doSmear=False,
												  jerUncDir=0
												  )
			if options.JERUncertainty!='none':
				process, jetCollection = JetDepot(process,
												  sequence=algorithm + 'Sequence',
												  JetTag=cms.InputTag(jetCollection),
												  JetType=params['jec_payloads'][index],
												  jecUncDir=0,
												  doSmear=True,
												  jerUncDir=1 if options.JERUncertainty=="up" else -1 if options.JERUncertainty=="down" else 0
												  )


		#################################################
		## Controls the vertex collection used in the analyzer
		#################################################
		if options.doMiniAOD:
			vtxCol = 'offlineSlimmedPrimaryVertices'
		else:
			vtxCol = 'offlinePrimaryVertices'

		#################################################
		## Controls the analyzer
		#################################################

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
				     jetType 	       = cms.string(params['jec_payloads'][index]),
				     srcJet            = cms.InputTag(jetCollection),
				     srcRho            = cms.InputTag('fixedGridRhoFastjetAll'),
				     srcVtx            = cms.InputTag(vtxCol),
				     srcPileupInfo     = cms.InputTag("slimmedAddPileupInfo") if options.doMiniAOD else cms.InputTag("addPileupInfo"),
				     JERUncertainty    = cms.string(options.JERUncertainty if options.UncertaintyOTF else 'none'),
				     JERLegacy         = cms.bool(False),
				     JERUncertaintyFile= cms.string(""),
				     JESUncertainty    = cms.string(options.JESUncertainty if options.UncertaintyOTF else 'none'),
				     JESUncertaintyType= cms.string("TotalNoTime"),
				     JESUncertaintyFile= cms.string("../data/Spring16_25nsV5_DATA/Spring16_25nsV5_DATA_UncertaintySources_AK4PFchs.txt"),
				     ptMinFilter       = cms.double(170 if params['algo'] == 'ak8' else 1.0),
				     )
		setattr(process,algorithm,pnm)

		# dump everything into a task so it can run unscheduled
		process.myTask = cms.Task()
		process.myTask.add(*[getattr(process,prod) for prod in process.producers_()])
		process.myTask.add(*[getattr(process,filt) for filt in process.filters_()])

		path = cms.Path()
		if options.doJetToolbox:
			path *= sequence *pnm
		elif not options.doJetToolbox and options.doMiniAOD and options.doReclustering and not options.useUpdater:
			path *= eval(params['algo']+'GenJetsNoNu') * eval(params['algo']+'PFJets'+pu_method) * getattr(process, 'selectedPatJets'+params['algo'].upper()+'PF'+pu_method) * sequence *pnm
		elif not options.doJetToolbox and options.doMiniAOD and not options.doReclustering and options.useUpdater:
			path *= eval("process.patJetCorrFactorsUpdatedJEC"+params['jec_payloads'][index]) * eval("process.updatedPatJetsUpdatedJEC"+params['jec_payloads'][index]) * sequence *pnm
		else:
			path *= sequence *pnm
		path.associate(process.myTask)
		setattr(process, algorithm + 'Path', path)

		print str(bcolors.BFAIL+"{A:<{widthA}s}"+bcolors.BWARNING+" {JC:<{widthJC}s}"+bcolors.OKBLUE+" {JP:<{widthJP}s}"+bcolors.BOKGREEN+" {CL:<{widthCL}s}"+bcolors.ENDC).format(A=algorithm,JC=jetCollection,JP=params['jec_payloads'][index],CL=params['jec_levels'],widthA=maxA,widthJC=maxJC,widthJP=maxJP,widthCL=maxCL)

#!
#! THAT'S ALL! CAN YOU BELIEVE IT? :-D
#!
