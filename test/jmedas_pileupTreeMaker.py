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


#!   _____ ____  _   _ _____ _____ _______ _____ ____  _   _  _____ 
#!  / ____/ __ \| \ | |  __ \_   _|__   __|_   _/ __ \| \ | |/ ____|
#! | |   | |  | |  \| | |  | || |    | |    | || |  | |  \| | (___  
#! | |   | |  | | . ` | |  | || |    | |    | || |  | | . ` |\___ \ 
#! | |___| |__| | |\  | |__| || |_   | |   _| || |__| | |\  |____) |
#!  \_____\____/|_| \_|_____/_____|  |_|  |_____\____/|_| \_|_____/ 
                                                                  
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = "START53_V7F::All"


#!  _____ _   _ _____  _    _ _______ 
#! |_   _| \ | |  __ \| |  | |__   __|
#!   | | |  \| | |__) | |  | |  | |   
#!   | | | . ` |  ___/| |  | |  | |   
#!  _| |_| |\  | |    | |__| |  | |   
#! |_____|_| \_|_|     \____/   |_|   
                                    
dyFiles = cms.untracked.vstring(
###########
# DY Jets #
###########
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0432E62A-7A6C-E411-87BB-002590DB92A8.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/06C61714-7E6C-E411-9205-002590DB92A8.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/0EAD09A8-7C6C-E411-B903-0025901D493E.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/1E4D0DAE-7C6C-E411-B488-002590DB923C.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/2286DCDB-796C-E411-AAB4-002481E14D72.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/2683B2C5-7C6C-E411-BE0B-002590DB9214.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/28EF4E6A-7D6C-E411-A54F-0025907DCA38.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/2A733A85-7D6C-E411-8D2B-002481E14D72.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3008BB28-7D6C-E411-AAC2-002590DB91F0.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/34167B14-7E6C-E411-A113-002590DB92A8.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/3A99E6A9-7B6C-E411-ADB4-00266CFFA6F8.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5610D8D0-7A6C-E411-B3AA-00237DE0BED6.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5EC2A65C-7A6C-E411-94D2-002590DB92A8.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/5EF8B51F-7C6C-E411-B13F-0025907DC9D6.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/600D5785-7C6C-E411-B90E-002590DBDFE0.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/629344EC-7C6C-E411-A19B-0025907DC9B0.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/8618D633-7D6C-E411-AB2C-003048F2FE3E.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/8E36F058-7C6C-E411-8424-0025901D493E.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/94708D15-7E6C-E411-BA0D-002590DB92A8.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/98175E8A-796C-E411-B612-002590DB923C.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/A266FB5C-796C-E411-B6EE-0025901D493E.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B6F6C960-7B6C-E411-916C-002481E0DE14.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/B81F3E5F-796C-E411-9105-002590DB91CE.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C27BA5BA-7D6C-E411-BBA9-002590DB9358.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/C84D5C9B-7C6C-E411-8825-002590DB91CE.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/CAD84EE9-7C6C-E411-912C-003048D437A0.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/F63F9E51-7D6C-E411-AFD9-002590DB92A8.root',
	'/store/mc/Phys14DR/DYJetsToLL_M-50_13TeV-madgraph-pythia8/MINIAODSIM/PU20bx25_PHYS14_25_V1-v1/00000/FEE3CF68-796C-E411-ABF5-002590DB9214.root'
    )
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10000))
process.source = cms.Source("PoolSource", fileNames = dyFiles )


#!   _____ ______ _______      _______ _____ ______  _____ 
#!  / ____|  ____|  __ \ \    / /_   _/ ____|  ____|/ ____|
#! | (___ | |__  | |__) \ \  / /  | || |    | |__  | (___  
#!  \___ \|  __| |  _  / \ \/ /   | || |    |  __|  \___ \ 
#!  ____) | |____| | \ \  \  /   _| || |____| |____ ____) |
#! |_____/|______|_|  \_\  \/   |_____\_____|______|_____/ 
                                                         
process.load('FWCore.MessageLogger.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 500
process.load('CommonTools.UtilAlgos.TFileService_cfi')
process.TFileService.fileName=cms.string('pileupNtuple.root')


#!  __  __ _    _  ____  _   _   _____  _____  ____  _            _______ _____ ____  _   _ 
#! |  \/  | |  | |/ __ \| \ | | |_   _|/ ____|/ __ \| |        /\|__   __|_   _/ __ \| \ | |
#! | \  / | |  | | |  | |  \| |   | | | (___ | |  | | |       /  \  | |    | || |  | |  \| |
#! | |\/| | |  | | |  | | . ` |   | |  \___ \| |  | | |      / /\ \ | |    | || |  | | . ` |
#! | |  | | |__| | |__| | |\  |  _| |_ ____) | |__| | |____ / ____ \| |   _| || |__| | |\  |
#! |_|  |_|\____/ \____/|_| \_| |_____|_____/ \____/|______/_/    \_\_|  |_____\____/|_| \_|
                                                                                                                                                                                    
from Analysis.JMEDAS.run2muoniso_cff import run2muoniso
run2muoniso(process)


#!           _      _____  ____  _____  _____ _______ _    _ __  __  _____ 
#!     /\   | |    / ____|/ __ \|  __ \|_   _|__   __| |  | |  \/  |/ ____|
#!    /  \  | |   | |  __| |  | | |__) | | |    | |  | |__| | \  / | (___  
#!   / /\ \ | |   | | |_ | |  | |  _  /  | |    | |  |  __  | |\/| |\___ \ 
#!  / ____ \| |___| |__| | |__| | | \ \ _| |_   | |  | |  | | |  | |____) |
#! /_/    \_\______\_____|\____/|_|  \_\_____|  |_|  |_|  |_|_|  |_|_____/                                                                        

algsizetype = {'AK':[4,8]}
jettype = ['PFchs','PUPPI']
#jettype = ['PFchs']
corrs = ['','l1']
prefix = 'slimmedJets'

algorithms = {}

for k, v in algsizetype.iteritems():
	for s in v:
		for j in jettype:
			for c in corrs:
				corrLevels = []
				if 'l1' in c:
					corrLevels.append('L1FastJet')
				if 'l2' in c:
					corrLevels.append('L2Relative')
				if 'l3' in c:
					corrLevels.append('L3Relative')

				if j=='PUPPI' and 'l1' in c:
					continue
				elif j=='PUPPI':
					algorithms[str(k+str(s)+j+c)]='patJets'+k+str(s)+'PUPPIJets',corrLevels
				elif s!=4:
					algorithms[str(k+str(s)+j+c)]=prefix+k+str(s),corrLevels
				else:
					algorithms[str(k+str(s)+j+c)]=prefix,corrLevels

print "{:<15} {:<20} {:<30}".format('Algorithm','Jet Collection',"Correction Levels")
print "{:<15} {:<20} {:<30}".format('---------','--------------',"-----------------")
for algorithm, tup in algorithms.iteritems():

    jetCollection, corrLevels = tup

    pnm = cms.EDAnalyzer('pileupTreeMaker',
                         PileupNtupleMakerParameters,
			 			 JetCorLabel       = cms.string(algorithm),
			 			 JetCorLevels      = cms.vstring(corrLevels),
                         srcJet            = cms.InputTag(jetCollection),
                         srcRho            = cms.InputTag('fixedGridRhoAll'),
                         srcVtx            = cms.InputTag('offlineSlimmedPrimaryVertices'),
                         srcMuons          = cms.InputTag('selectedPatMuons'),
                         srcVMCHSTAND      = cms.InputTag('muPFIsoValueCHR04STAND'),
                         srcVMNHSTAND      = cms.InputTag('muPFIsoValueNHR04STAND'),
                         srcVMPhSTAND      = cms.InputTag('muPFIsoValuePhR04STAND'),
                         srcVMPUSTAND      = cms.InputTag('muPFIsoValuePUR04STAND'),
                         srcVMCHPFWGT      = cms.InputTag('muPFIsoValueCHR04PFWGT'),
                         srcVMNHPFWGT      = cms.InputTag('muPFIsoValueNHR04PFWGT'),
                         srcVMPhPFWGT      = cms.InputTag('muPFIsoValuePhR04PFWGT'),
                         srcVMCHPUPPI      = cms.InputTag('muPFIsoValueCHR04PUPPI'),
                         srcVMNHPUPPI      = cms.InputTag('muPFIsoValueNHR04PUPPI'),
                         srcVMPhPUPPI      = cms.InputTag('muPFIsoValuePhR04PUPPI')
			 )
    setattr(process,algorithm,pnm)
    sequence = cms.Sequence(pnm)

    sequence = cms.Sequence(sequence)
    setattr(process, algorithm + 'Sequence', sequence)
    #path = cms.Path( sequence )
    path = process.p.copy()
    path *= sequence
    setattr(process, algorithm + 'Path', path)
    print "{:<15} {:<20} {:<30}".format(algorithm,jetCollection,corrLevels)

process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

#!
#! THAT'S ALL! CAN YOU BELIEVE IT? :-D
#!
