#! /usr/bin/env python
import os
import ROOT
import sys
import copy
import re
from array import array
import math
import time

ts_start = time.time()

## _________                _____.__                            __  .__               
## \_   ___ \  ____   _____/ ____\__| ____  __ ______________ _/  |_|__| ____   ____  
## /    \  \/ /  _ \ /    \   __\|  |/ ___\|  |  \_  __ \__  \\   __\  |/  _ \ /    \ 
## \     \___(  <_> )   |  \  |  |  / /_/  >  |  /|  | \// __ \|  | |  (  <_> )   |  \
##  \______  /\____/|___|  /__|  |__\___  /|____/ |__|  (____  /__| |__|\____/|___|  /
##         \/            \/        /_____/                   \/                    \/ 

from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument('--files', type=str,
                  dest='files',
                  help='Input files')

parser.add_argument('--maxFiles', type=int, 
                  dest='maxFiles',
                  default=-1,
                  help='Maximum number of files to use')

parser.add_argument('--outname', type=str,
                  default='outplots.root',
                  dest='outname',
                  help='Name of output file')

parser.add_argument('--verbose', action='store_true',
                  default=False,
                  dest='verbose',
                  help='Print debugging info')

parser.add_argument('--correctJets', type=str,
                  default=None,
                  dest='correctJets',
                  help='Apply latest jet corrections. Specify JEC name based on https://twiki.cern.ch/twiki/bin/view/CMS/JECDataMC.')



parser.add_argument('--isData', action='store_true',
                  default=False,
                  dest='isData',
                  help='Run on data')


parser.add_argument('--smearJets', action='store_true',
                  default=False,
                  dest='smearJets',
                  help='Smear jet energy.')


parser.add_argument('--maxevents', type=int,
                  default=-1,
                  dest='maxevents',
                  help='Number of events to run. -1 is all events')

parser.add_argument('--maxjets', type=int,
                  default=999,
                  dest='maxjets',
                  help='Number of jets to plot. To plot all jets, set to a big number like 999')



parser.add_argument('--minAK8Pt', type=float,
                  default=200.,
                  dest='minAK8Pt',
                  help='Minimum PT for AK8 jets')

parser.add_argument('--maxAK8Rapidity', type=float,
                  default=2.4,
                  dest='maxAK8Rapidity',
                  help='Maximum AK8 rapidity')


parser.add_argument('--minAK4Pt', type=float,
                  default=30.,
                  dest='minAK4Pt',
                  help='Minimum PT for AK4 jets')

parser.add_argument('--maxAK4Rapidity', type=float,
                  default=2.4,
                  dest='maxAK4Rapidity',
                  help='Maximum AK4 rapidity')

parser.add_argument('--xrootd', type=str,
                  #default='cmsxrootd.fnal.gov',
                  default = "xrootd-cms.infn.it",
                  dest='xrootd',
                  help='xrootd redirect string')

parser.add_argument('--matchPdgIdAK4', type=str, nargs=2,
                  dest='matchPdgIdAK4',
                  help='Perform truth matching of AK4 jets (specify PDG ID and DeltaR)')

parser.add_argument('--matchPdgIdAK8', type=str, nargs=2,
                  dest='matchPdgIdAK8',
                  help='Perform truth matching of AK8 jets (specify PDG ID and DeltaR)')


args = parser.parse_args()


## _____________      __.____    .__  __             _________ __          _____  _____ 
## \_   _____/  \    /  \    |   |__|/  |_  ____    /   _____//  |_ __ ___/ ____\/ ____\
##  |    __) \   \/\/   /    |   |  \   __\/ __ \   \_____  \\   __\  |  \   __\\   __\ 
##  |     \   \        /|    |___|  ||  | \  ___/   /        \|  | |  |  /|  |   |  |   
##  \___  /    \__/\  / |_______ \__||__|  \___  > /_______  /|__| |____/ |__|   |__|   
##      \/          \/          \/             \/          \/                           

from DataFormats.FWLite import Events, Handle

jethandle0  = Handle ("std::vector<pat::Jet>")
jetlabel0 = ("slimmedJets")
jethandle1  = Handle ("std::vector<pat::Jet>")
jetlabel1 = ("slimmedJetsAK8")

rhoHandle = Handle ("double")
rhoLabel = ("fixedGridRhoAll")

pvHandle = Handle("std::vector<reco::Vertex>")
pvLabel = ("offlineSlimmedPrimaryVertices")

if args.smearJets and args.isData:
    print 'Misconfiguration. I cannot access generator-level jets on data. Not smearing jets.'
    args.smearJets = False

if args.correctJets: 
    ### JEC implementation

    if not args.isData : 
        vPar = ROOT.vector(ROOT.JetCorrectorParameters)()
        vPar.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L1FastJet_AK4PFchs.txt'.format(args.correctJets, args.correctJets))))
        vPar.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L2Relative_AK4PFchs.txt'.format(args.correctJets, args.correctJets))))
        vPar.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L3Absolute_AK4PFchs.txt'.format(args.correctJets, args.correctJets))))
        jec = ROOT.FactorizedJetCorrector( vPar )
        jecUnc = ROOT.JetCorrectionUncertainty(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_Uncertainty_AK4PFchs.txt'.format(args.correctJets, args.correctJets)))

        vParAK8 = ROOT.vector(ROOT.JetCorrectorParameters)()
        vParAK8.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L1FastJet_AK8PFchs.txt'.format(args.correctJets, args.correctJets))))
        vParAK8.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L2Relative_AK8PFchs.txt'.format(args.correctJets, args.correctJets))))
        vParAK8.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L3Absolute_AK8PFchs.txt'.format(args.correctJets, args.correctJets))))
        jecAK8 = ROOT.FactorizedJetCorrector( vParAK8 )

        jecUncAK8 = ROOT.JetCorrectionUncertainty( os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_Uncertainty_AK8PFchs.txt'.format(args.correctJets, args.correctJets)))
    else :
        vPar = ROOT.vector(ROOT.JetCorrectorParameters)()
        vPar.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L1FastJet_AK4PFchs.txt'.format(args.correctJets, args.correctJets))))
        vPar.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L2Relative_AK4PFchs.txt'.format(args.correctJets, args.correctJets))))
        vPar.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L3Absolute_AK4PFchs.txt'.format(args.correctJets, args.correctJets))))
        vPar.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L2L3Residual_AK4PFchs.txt') )) # Need residual correction for data
        jec = ROOT.FactorizedJetCorrector( vPar )
        jecUnc = ROOT.JetCorrectionUncertainty( os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_Uncertainty_AK4PFchs.txt'.format(args.correctJets, args.correctJets) ))

        vParAK8 = ROOT.vector(ROOT.JetCorrectorParameters)()
        vParAK8.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L1FastJet_AK8PFchs.txt'.format(args.correctJets, args.correctJets))))
        vParAK8.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L2Relative_AK8PFchs.txt'.format(args.correctJets, args.correctJets))))
        vParAK8.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L3Absolute_AK8PFchs.txt'.format(args.correctJets, args.correctJets))))
        vParAK8.push_back( ROOT.JetCorrectorParameters(os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_L2L3Residual_AK8PFchs.txt') )) # Need residual correction for data
        jecAK8 = ROOT.FactorizedJetCorrector( vParAK8 )

        jecUncAK8 = ROOT.JetCorrectionUncertainty( os.path.expandvars('$CMSSW_BASE/src/Analysis/JMEDAS/data/JECs/{}/{}_Uncertainty_AK8PFchs.txt'.format(args.correctJets, args.correctJets) ))

if args.matchPdgIdAK4:
    doMatchingAK4 = True
    matchAK4PdgId = int(args.matchPdgIdAK4[0])
    matchAK4DR = int(args.matchPdgIdAK4[1])
else:
    doMatchingAK4 = False

if args.matchPdgIdAK8:
    doMatchingAK8 = True
    matchAK8PdgId = int(args.matchPdgIdAK8[0])
    matchAK8DR = int(args.matchPdgIdAK8[1])
else:
    doMatchingAK8 = False

if doMatchingAK4 or doMatchingAK8:
    genParticlesHandle = Handle("std::vector<reco::GenParticle>")
    genParticlesLabel = ("prunedGenParticles")

##   ___ ___ .__          __                                             
##  /   |   \|__| _______/  |_  ____   ________________    _____   ______
## /    ~    \  |/  ___/\   __\/  _ \ / ___\_  __ \__  \  /     \ /  ___/
## \    Y    /  |\___ \  |  | (  <_> ) /_/  >  | \// __ \|  Y Y  \\___ \ 
##  \___|_  /|__/____  > |__|  \____/\___  /|__|  (____  /__|_|  /____  >
##        \/         \/             /_____/            \/      \/     \/

f = ROOT.TFile(args.outname, "RECREATE")
f.cd()

h_ptAK4       = ROOT.TH1F("h_ptAK4", "AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptUpAK4     = ROOT.TH1F("h_ptUpAK4", "JEC Up AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptDownAK4   = ROOT.TH1F("h_ptDownAK4", "JEC Down AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptUncorrAK4 = ROOT.TH1F("h_ptUncorrAK4", "UnCorrected AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_JECValueAK4 = ROOT.TH1F("h_JECValueAK4", "Value of JEC for AK4 Jet", 100, 0.8, 1.1)
h_etaAK4      = ROOT.TH1F("h_etaAK4", "AK4 Jet #eta;#eta", 120, -6, 6)
h_yAK4        = ROOT.TH1F("h_yAK4", "AK4 Jet Rapidity;y", 120, -6, 6)
h_phiAK4      = ROOT.TH1F("h_phiAK4", "AK4 Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK4        = ROOT.TH1F("h_mAK4", "AK4 Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK4     = ROOT.TH1F("h_areaAK4", "AK4 Jet Area;Area", 250, 0, 5.0)

h_ptAK4Gen   = ROOT.TH1F("h_ptAK4Gen", "AK4Gen Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_etaAK4Gen  = ROOT.TH1F("h_etaAK4Gen", "AK4Gen Jet #eta;#eta", 120, -6, 6)
h_yAK4Gen    = ROOT.TH1F("h_yAK4Gen", "AK4Gen Jet Rapidity;y", 120, -6, 6)
h_phiAK4Gen  = ROOT.TH1F("h_phiAK4Gen", "AK4Gen Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK4Gen    = ROOT.TH1F("h_mAK4Gen", "AK4Gen Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK4Gen = ROOT.TH1F("h_areaAK4Gen", "AK4Gen Jet Area;Area", 250, 0, 5.0)


h_ptAK8            = ROOT.TH1F("h_ptAK8", "AK8 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptAK8Puppi       = ROOT.TH1F("h_ptAK8Puppi", "AK8Puppi Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptUpAK8          = ROOT.TH1F("h_ptUpAK8", "JEC Up AK8 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptDownAK8        = ROOT.TH1F("h_ptDownAK8", "JEC Down AK8 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptUncorrAK8      = ROOT.TH1F("h_ptUncorrAK8", "UnCorrected AK8 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_JECValueAK8      = ROOT.TH1F("h_JECValueAK8", "Value of JEC for AK8 Jet", 100, 0.8, 1.1)
h_etaAK8           = ROOT.TH1F("h_etaAK8", "AK8 Jet #eta;#eta", 120, -6, 6)
h_etaAK8Puppi      = ROOT.TH1F("h_etaAK8Puppi", "AK8Puppi Jet #eta;#eta", 120, -6, 6)
h_yAK8             = ROOT.TH1F("h_yAK8", "AK8 Jet Rapidity;y", 120, -6, 6)
h_phiAK8           = ROOT.TH1F("h_phiAK8", "AK8 Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_phiAK8Puppi      = ROOT.TH1F("h_phiAK8Puppi", "AK8Puppi Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK8             = ROOT.TH1F("h_mAK8", "AK8 Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK8          = ROOT.TH1F("h_areaAK8", "AK8 Jet Area;Area", 250, 0, 5.0)
h_msoftdropAK8     = ROOT.TH1F("h_msoftdropAK8", "AK8 Softdrop Jet Mass;Mass (GeV)", 100, 0, 1000)
h_mprunedAK8       = ROOT.TH1F("h_mprunedAK8", "AK8 Pruned Jet Mass;Mass (GeV)", 100, 0, 1000)
h_mpuppiAK8        = ROOT.TH1F("h_mpuppiAK8", "AK8 PUPPI Jet Mass;Mass (GeV)", 100, 0, 1000)
h_mSDpuppiAK8      = ROOT.TH1F("h_mSDpuppiAK8", "AK8 PUPPI SD Jet Mass;Mass (GeV)", 100, 0, 1000)
h_minmassAK8       = ROOT.TH1F("h_minmassAK8", "AK8 CMS Top Tagger Min Mass Paring;m_{min} (GeV)", 100, 0, 1000)
h_nsjAK8           = ROOT.TH1F("h_nsjAK8", "AK8 CMS Top Tagger N_{subjets};N_{subjets}", 5, 0, 5)
h_tau21AK8         = ROOT.TH1F("h_tau21AK8", "AK8 Jet #tau_{2} / #tau_{1};#tau_{21}", 100, 0, 1.0)
h_tau32AK8         = ROOT.TH1F("h_tau32AK8", "AK8 Jet #tau_{3} / #tau_{2};#tau_{32}", 100, 0, 1.0)
h_ptGroomedCorrAK8 = ROOT.TH1F("h_ptGroomedCorrAK8", "AK8 Corrected Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_msoftdropCorrAK8 = ROOT.TH1F("h_msoftdropCorrAK8", "AK8 Softdrop Jet Mass, Corrected;Mass (GeV)", 100, 0, 1000)
h_rhoRatioAK8      = ROOT.TH1F("h_rhoRatioAK8", "AK8 Jet #rho = (m/p_{T}R)^{2};#rho", 100, 0, 1.0)
h_logrhoRatioAK8   = ROOT.TH1F("h_logrhoRatioAK8", "AK8 Jet log(#rho=(m/p_{T}R)^{2});log(#rho)", 1100, -10,1.)
h_mSubjet0AK8      = ROOT.TH1F("h_mSubjet0AK8", "AK8 Highest-mass Subjet Jet Mass;Mass (GeV)", 100, 0, 400)
h_mSubjet1AK8      = ROOT.TH1F("h_mSubjet1AK8", "AK8 Lowest-mass Subjet Jet Mass;Mass (GeV)", 100, 0, 400)
h_ak8_N2_beta1     = ROOT.TH1F("h_ak8_N2_beta1", "AK8 N2_beta1;N_{2}^{#beta=1}", 100, 0., 1.)
h_ak8_N2_beta2     = ROOT.TH1F("h_ak8_N2_beta2", "AK8 N2_beta2;N_{2}^{#beta=2}", 100, 0., 1.)
h_ak8_N3_beta1     = ROOT.TH1F("h_ak8_N3_beta1", "AK8 N3_beta1;N_{3}^{#beta=1}", 100, 0., 3.)
h_ak8_N3_beta2     = ROOT.TH1F("h_ak8_N3_beta2", "AK8 N3_beta2;N_{3}^{#beta=2}", 100, 0., 3.)



h_ptAK8Gen   = ROOT.TH1F("h_ptAK8Gen", "AK8Gen Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_etaAK8Gen  = ROOT.TH1F("h_etaAK8Gen", "AK8Gen Jet #eta;#eta", 120, -6, 6)
h_yAK8Gen    = ROOT.TH1F("h_yAK8Gen", "AK8Gen Jet Rapidity;y", 120, -6, 6)
h_phiAK8Gen  = ROOT.TH1F("h_phiAK8Gen", "AK8Gen Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK8Gen    = ROOT.TH1F("h_mAK8Gen", "AK8Gen Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK8Gen = ROOT.TH1F("h_areaAK8Gen", "AK8Gen Jet Area;Area", 250, 0, 5.0)

varTree = ROOT.TTree("varTree", "varTree")
ak4pt           = array('f', [-1.])
ak4mass         = array('f', [-1.])
ak8pt           = array('f', [-1.])
ak8eta          = array('f', [-1.])
ak8phi          = array('f', [-1.])
ak8PUPPIpt      = array('f', [-1.])
ak8PUPPIeta     = array('f', [-1.])
ak8PUPPIphi     = array('f', [-1.])
ak8mass         = array('f', [-1.])
ak8csv          = array('f', [-1.])
ak8PrunedMass   = array('f', [-1.])
ak8SDmass       = array('f', [-1.])
ak8PUPPImass    = array('f', [-1.])
ak8SDPUPPImass  = array('f', [-1.])
ak8tau32        = array('f', [-1.])
ak8tau21        = array('f', [-1.])
ak8SD_sub0_mass = array('f', [-1.])
ak8SD_sub1_mass = array('f', [-1.])
ak8SD_sub0_csv  = array('f', [-1.])
ak8SD_sub1_csv  = array('f', [-1.])
ak8_N2_beta1    = array('f', [-1.])
ak8_N3_beta1    = array('f', [-1.])
ak8_N2_beta2    = array('f', [-1.])
ak8_N3_beta2    = array('f', [-1.])
npv             = array('f', [-1.])

varTree.Branch('ak4pt', ak4pt, 'ak4pt/F')
varTree.Branch('ak4mass', ak4mass, 'ak4mass/F')
varTree.Branch('ak8pt', ak8pt, 'ak8pt/F')
varTree.Branch('ak8eta', ak8eta, 'ak8eta/F')
varTree.Branch('ak8phi', ak8phi, 'ak8phi/F')
varTree.Branch('ak8PUPPIpt', ak8PUPPIpt, 'ak8PUPPIpt/F')
varTree.Branch('ak8PUPPIeta', ak8PUPPIeta, 'ak8PUPPIeta/F')
varTree.Branch('ak8PUPPIphi', ak8PUPPIphi, 'ak8PUPPIphi/F')
varTree.Branch('ak8mass', ak8mass, 'ak8mass/F')
varTree.Branch('ak8csv', ak8csv, 'ak8csv/F')
varTree.Branch('ak8CHSSDmass', ak8SDmass, 'ak8SDmass/F')
varTree.Branch('ak8PUPPImass', ak8PUPPImass, 'ak8PUPPImass/F')
varTree.Branch('ak8PUPPISDmass', ak8SDPUPPImass, 'ak8PUPPISDmass/F')
varTree.Branch('ak8tau32', ak8tau32, 'ak8tau32/F')
varTree.Branch('ak8tau21', ak8tau21, 'ak8tau21/F')
varTree.Branch('ak8SD_sub0_mass', ak8SD_sub0_mass, 'ak8SD_sub0_mass/F')
varTree.Branch('ak8SD_sub1_mass', ak8SD_sub1_mass, 'ak8SD_sub1_mass/F')
varTree.Branch('ak8SD_sub0_csv', ak8SD_sub0_csv, 'ak8SD_sub0_csv/F')
varTree.Branch('ak8SD_sub1_csv', ak8SD_sub1_csv, 'ak8SD_sub1_csv/F')
varTree.Branch('ak8_N2_beta1', ak8_N2_beta1, 'ak8_N2_beta1/F')
varTree.Branch('ak8_N2_beta2', ak8_N2_beta2, 'ak8_N2_beta2/F')
varTree.Branch('ak8_N3_beta1', ak8_N3_beta1, 'ak8_N3_beta1/F')
varTree.Branch('ak8_N3_beta2', ak8_N3_beta2, 'ak8_N3_beta2/F')
varTree.Branch('npv', npv, 'npv/F')

##      ____.       __    __________                    .__          __  .__               
##     |    | _____/  |_  \______   \ ____   __________ |  |  __ ___/  |_|__| ____   ____  
##     |    |/ __ \   __\  |       _// __ \ /  ___/  _ \|  | |  |  \   __\  |/  _ \ /    \ 
## /\__|    \  ___/|  |    |    |   \  ___/ \___ (  <_> )  |_|  |  /|  | |  (  <_> )   |  \
## \________|\___  >__|    |____|_  /\___  >____  >____/|____/____/ |__| |__|\____/|___|  /
##               \/               \/     \/     \/                                      \/ 
def getJER(jetEta, sysType) :
    """
    Here, jetEta should be the jet pseudorapidity, and sysType is :
        nominal : 0
        down    : -1
        up      : +1
    """

    jerSF = 1.0

    if ( (sysType==0 or sysType==-1 or sysType==1) == False):
        print "ERROR: Can't get JER! use type=0 (nom), -1 (down), +1 (up)"
        return float(jerSF)

    # Values from https://twiki.cern.ch/twiki/bin/view/CMS/JetResolution
    etamin = [0.0,0.5,0.8,1.1,1.3,1.7,1.9,2.1,2.3,2.5,2.8,3.0,3.2]
    etamax = [0.5,0.8,1.1,1.3,1.7,1.9,2.1,2.3,2.5,2.8,3.0,3.2,5.0]
    
    scale_nom = [1.109,1.138,1.114,1.123,1.084,1.082,1.140,1.067,1.177,1.364,1.857,1.328,1.16]
    scale_unc = [0.008,0.013,0.013,0.024,0.011,0.035,0.047,0.053,0.041,0.039,0.071,0.022,0.029] 


    for iSF in range(0,len(scale_nom)) :
        if abs(jetEta) >= etamin[iSF] and abs(jetEta) < etamax[iSF] :
            if sysType < 0 :
                jerSF =  scale_nom[iSF]-scale_unc[iSF]
            elif sysType > 0 :
                jerSF =  scale_nom[iSF]+scale_unc[iSF]
            else :
                jerSF = scale_nom[iSF]
            break

    return float(jerSF)



## ___________                    __    .____                         
## \_   _____/__  __ ____   _____/  |_  |    |    ____   ____ ______  
##  |    __)_\  \/ // __ \ /    \   __\ |    |   /  _ \ /  _ \\____ \ 
##  |        \\   /\  ___/|   |  \  |   |    |__(  <_> |  <_> )  |_> >
## /_______  / \_/  \___  >___|  /__|   |_______ \____/ \____/|   __/ 
##         \/           \/     \/               \/            |__|    


# IMPORTANT : Run one FWLite instance per file. Otherwise,
# FWLite aggregates ALL of the information immediately, which
# can take a long time to parse. 
filelist = file(args.files)
filesraw = filelist.readlines()
files = []
nevents = 0
for i, ifile in enumerate(filesraw):
    if args.maxFiles >= 0:
      if i >= args.maxFiles:
        break
    if len( ifile ) > 2 : 
        s = 'root://' + args.xrootd + '/' + ifile.rstrip()
        files.append( s )
        print 'Added ' + s

#if args.maxFiles:
#  files = files[:args.maxFiles]

# loop over files
for ifile in files :
    if args.maxevents > 0 and nevents > args.maxevents :
        break
    print 'Processing file ' + ifile
    events = Events(ifile)

    # loop over events in this file
    i = 0
    for event in events:
        if args.maxevents > 0 and nevents > args.maxevents :
            break
        i += 1
        nevents += 1

        if i % 1000 == 0 :
            print '    ---> Event ' + str(i)
        
        ##    _____   ____  __.  _____        ____.       __    __________.__          __          
        ##   /  _  \ |    |/ _| /  |  |      |    | _____/  |_  \______   \  |   _____/  |_  ______
        ##  /  /_\  \|      <  /   |  |_     |    |/ __ \   __\  |     ___/  |  /  _ \   __\/  ___/
        ## /    |    \    |  \/    ^   / /\__|    \  ___/|  |    |    |   |  |_(  <_> )  |  \___ \ 
        ## \____|__  /____|__ \____   |  \________|\___  >__|    |____|   |____/\____/|__| /____  >
        ##         \/        \/    |__|                \/                                       \/ 


        # get rho and vertices for JEC
        event.getByLabel (rhoLabel, rhoHandle)
        event.getByLabel (pvLabel, pvHandle)

        rhoValue = rhoHandle.product()
        pvs = pvHandle.product()
        #print rhoValue[0]
        
        if doMatchingAK4 or doMatchingAK8:
            event.getByLabel(genParticlesLabel, genParticlesHandle)
            genParticles = genParticlesHandle.product()

            if doMatchingAK4:
                genPartsAK4 = []
                for genParticle in genParticles:
                    if abs(genParticle.pdgId()) == matchAK4PdgId:
                        genPartsAK4.append(genParticle)

            if doMatchingAK8:
                genPartsAK8 = []
                for genParticle in genParticles:
                    if abs(genParticle.pdgId()) == matchAK8PdgId:
                        genPartsAK8.append(genParticle)


        if args.verbose :
            print '------ AK4 jets ------'
        # use getByLabel, just like in cmsRun
        event.getByLabel (jetlabel0, jethandle0)
        # get the product
        jets0 = jethandle0.product()
        # loop over jets and fill hists
        ijet = 0
        for jet in jets0 :
            if ijet >= args.maxjets :
                break

            if doMatchingAK4:
                matched = False
                for genPart in genPartsAK4:
                    if math.sqrt(
                            math.acos(math.cos(genPart.phi() - jet.phi()))**2 
                            + (genPart.eta() - jet.eta())**2) < matchAK4DR:
                        matched = True
                        break
                if not matched:
                    continue

            if jet.pt() > args.minAK4Pt and abs(jet.rapidity()) < args.maxAK4Rapidity :
                
                
                #Find the jet correction
                uncorrJet = copy.copy( jet.correctedP4(0) ) # For some reason, in python this is interfering with jet.genJet() in strange ways without the copy.copy

                if uncorrJet.E() < 0.00001 :
                    print 'Very strange. Uncorrected jet E = ' + str( uncorrJet.E()) + ', but Corrected jet E = ' + str( jet.energy() )
                    continue
                    
                # Apply loose jet ID to uncorrected jet  https://twiki.cern.ch/twiki/bin/view/CMS/JetID13TeVRun2016
                # the folling is valid only for eta < 2.4. see twiki for full definition
                nhf = jet.neutralHadronEnergy() / uncorrJet.E()
                nef = jet.neutralEmEnergy() / uncorrJet.E()
                chf = jet.chargedHadronEnergy() / uncorrJet.E()
                cef = jet.chargedEmEnergy() / uncorrJet.E()
                nconstituents = jet.numberOfDaughters()
                nch = jet.chargedMultiplicity()
                goodJet = \
                  nhf < 0.99 and \
                  nef < 0.99 and \
                  chf > 0.00 and \
                  cef < 0.99 and \
                  nch > 0 and \
                  nconstituents


                if not goodJet :
                    continue


                # Corrections and smears for jet energy will be stored here.
                corr = 1.0
                corrUp = 1.0
                corrDn = 1.0

                # Get the smeared jets for jet resolution
                if args.smearJets  :
                    genJet = jet.genJet()
                    if genJet != None : 
                        smear = getJER(jet.eta(), 0) #JER nominal=0, up=+1, down=-1
                        smearUp = getJER(jet.eta(), 1) #JER nominal=0, up=+1, down=-1
                        smearDn = getJER(jet.eta(), -1) #JER nominal=0, up=+1, down=-1
                        recopt = jet.pt()
                        genpt = genJet.pt()
                        deltapt = (recopt-genpt)*(smear-1.0)
                        deltaptUp = (recopt-genpt)*(smearUp-1.0)
                        deltaptDn = (recopt-genpt)*(smearDn-1.0)
                        ptsmear = max(0.0, (recopt+deltapt)/recopt)
                        ptsmearUp = max(0.0, (recopt+deltaptUp)/recopt)
                        ptsmearDn = max(0.0, (recopt+deltaptDn)/recopt)
                        corr *= ptsmear
                        corrUp *= ptsmearUp
                        corrDn *= ptsmearDn

                # Get the latest, greatest jet corrections
                if args.correctJets : 
                    jec.setJetEta( uncorrJet.eta() )
                    jec.setJetPt ( uncorrJet.pt() )
                    jec.setJetE  ( uncorrJet.energy() )
                    jec.setJetA  ( jet.jetArea() )
                    jec.setRho   ( rhoValue[0] )
                    jec.setNPV   ( len(pvs) )
                    icorr = jec.getCorrection()
                    corr *= icorr
                    corrUp *= icorr
                    corrDn *= icorr


                    #JEC Uncertainty
                    jecUnc.setJetEta( uncorrJet.eta() )
                    jecUnc.setJetPhi( uncorrJet.phi() )
                    jecUnc.setJetPt( corr * uncorrJet.pt() )
                    corrUp += jecUnc.getUncertainty(1)
                    jecUnc.setJetEta( uncorrJet.eta() )
                    jecUnc.setJetPhi( uncorrJet.phi() )
                    jecUnc.setJetPt( corr * uncorrJet.pt() )
                    corrDn -= jecUnc.getUncertainty(0)


                h_ptAK4.Fill( corr * uncorrJet.pt() )
                h_JECValueAK4.Fill( corr )
                h_ptUncorrAK4.Fill( uncorrJet.pt() )
                h_ptDownAK4.Fill( corrDn * uncorrJet.pt() )
                h_ptUpAK4.Fill( corrUp * uncorrJet.pt() )

                h_etaAK4.Fill( jet.eta() )
                h_yAK4.Fill( jet.y() )
                h_phiAK4.Fill( jet.phi() )
                h_mAK4.Fill( jet.mass() )
                h_areaAK4.Fill( jet.jetArea() )
                ak8pt[0] = -999.
		ak4mass[0] = jet.mass()
		ak4pt[0] = jet.pt()
		varTree.Fill()

		genJet = jet.genJet()
                if genJet != None :
                    h_ptAK4Gen.Fill( genJet.pt() )
                    h_etaAK4Gen.Fill( genJet.eta() )
                    h_yAK4Gen.Fill( genJet.y() )
                    h_phiAK4Gen.Fill( genJet.phi() )
                    h_mAK4Gen.Fill( genJet.mass() )
                    h_areaAK4Gen.Fill( genJet.jetArea() )
                if args.verbose == True : 
                    print ("Jet {0:4.0f}, orig pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, " +
                           "nda = {5:3.0f}, vtxmass = {6:6.2f}, area = {7:6.2f}, corr = {8:6.3f} +{9:6.3f} -{10:6.3f} ").format(
                        ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(), jet.userFloat('vtxMass'),
                        jet.jetArea(), corr, abs(corrUp - corr), abs(corr - corrDn)
                        ),
                    if genJet != None :
                        print (", gen pt = {0:6.2f}").format( genJet.pt() )
                    else :
                        print ''
            ijet += 1


        ##    _____   ____  __. ______        ____.       __    __________.__          __          
        ##   /  _  \ |    |/ _|/  __  \      |    | _____/  |_  \______   \  |   _____/  |_  ______
        ##  /  /_\  \|      <  >      <      |    |/ __ \   __\  |     ___/  |  /  _ \   __\/  ___/
        ## /    |    \    |  \/   --   \ /\__|    \  ___/|  |    |    |   |  |_(  <_> )  |  \___ \ 
        ## \____|__  /____|__ \______  / \________|\___  >__|    |____|   |____/\____/|__| /____  >
        ##         \/        \/      \/                \/                                       \/ 
        if args.verbose :
            print '------ AK8 jets ------'
        # use getByLabel, just like in cmsRun
        event.getByLabel (jetlabel1, jethandle1)
        # get the product
        jets1 = jethandle1.product()
        # loop over jets and fill hists
        if args.verbose :
          print jets1.size()
        ijet = 0
        for jet in jets1 :
            if ijet >= args.maxjets :
                break

            if doMatchingAK8:
                matched = False
                for genPart in genPartsAK8:
                    if math.sqrt(
                            math.acos(math.cos(genPart.phi() - jet.phi()))**2 
                            + (genPart.eta() - jet.eta())**2) < matchAK8DR:
                        matched = True
                        break
                if not matched:
                    continue

            if jet.pt() > args.minAK8Pt and abs(jet.rapidity()) < args.maxAK8Rapidity :
                
                #FInd the jet correction
                uncorrJet = copy.copy( jet.correctedP4(0) ) # For some reason, in python this is interfering with jet.genJet() in strange ways without the copy.copy


                if uncorrJet.E() < 0.000001 :
                    continue
                # Apply jet ID to uncorrected jet
                nhf = jet.neutralHadronEnergy() / uncorrJet.E()
                nef = jet.neutralEmEnergy() / uncorrJet.E()
                chf = jet.chargedHadronEnergy() / uncorrJet.E()
                cef = jet.chargedEmEnergy() / uncorrJet.E()
                nconstituents = jet.numberOfDaughters()
                nch = jet.chargedMultiplicity()
                goodJet = \
                  nhf < 0.99 and \
                  nef < 0.99 and \
                  chf > 0.00 and \
                  cef < 0.99 and \
                  nconstituents > 1 and \
                  nch > 0

                if not goodJet :
                    continue

                # Corrections and smears for jet energy will be stored here.
                corr = 1.0
                corrUp = 1.0
                corrDn = 1.0

                # Get the smeared jets for jet resolution
                if args.smearJets  :
                    genJet = jet.genJet()
                    if genJet != None : 
                        smear = getJER(jet.eta(), 0) #JER nominal=0, up=+1, down=-1
                        smearUp = getJER(jet.eta(), 1) #JER nominal=0, up=+1, down=-1
                        smearDn = getJER(jet.eta(), -1) #JER nominal=0, up=+1, down=-1
                        recopt = jet.pt()
                        genpt = genJet.pt()
                        deltapt = (recopt-genpt)*(smear-1.0)
                        deltaptUp = (recopt-genpt)*(smearUp-1.0)
                        deltaptDn = (recopt-genpt)*(smearDn-1.0)
                        ptsmear = max(0.0, (recopt+deltapt)/recopt)
                        ptsmearUp = max(0.0, (recopt+deltaptUp)/recopt)
                        ptsmearDn = max(0.0, (recopt+deltaptDn)/recopt)
                        corr *= ptsmear
                        corrUp *= ptsmearUp
                        corrDn *= ptsmearDn
                    

                # Get the latest, greatest jet corrections
                if args.correctJets : 
                    jecAK8.setJetEta( uncorrJet.eta() )
                    jecAK8.setJetPt ( uncorrJet.pt() )
                    jecAK8.setJetE  ( uncorrJet.energy() )
                    jecAK8.setJetA  ( jet.jetArea() )
                    jecAK8.setRho   ( rhoValue[0] )
                    jecAK8.setNPV   ( len(pvs) )
                    icorr = jecAK8.getCorrection()
                    corr *= icorr
                    corrUp *= icorr
                    corrDn *= icorr

                    #JEC Uncertainty
                    jecUncAK8.setJetEta( uncorrJet.eta() )
                    jecUncAK8.setJetPt( corr * uncorrJet.pt() )
                    corrUp += jecUncAK8.getUncertainty(1)
                    jecUncAK8.setJetEta( uncorrJet.eta() )
                    jecUncAK8.setJetPt( corr * uncorrJet.pt() )
                    corrDn -= jecUncAK8.getUncertainty(0)

                    # Get individual JEC levels
                    #  need to first reset jecAK8
                    jecAK8.setJetEta( uncorrJet.eta() )
                    jecAK8.setJetPt ( uncorrJet.pt() )
                    jecAK8.setJetE  ( uncorrJet.energy() )
                    jecAK8.setJetA  ( jet.jetArea() )
                    jecAK8.setRho   ( rhoValue[0] )
                    jecAK8.setNPV   ( len(pvs) )
                    factors = jecAK8.getSubCorrections();
                    L1cor = 1.0
                    L12cor = 1.0
                    L123cor = 1.0
                    L123rescor = 1.0
                    if factors.size() > 0:
                        L1cor = factors[0]
                    if factors.size() > 1:
                        L12cor = factors[1]
                    if factors.size() > 2:
                        L123cor = factors[2]
                    
                    #calculate L2L3 correction (needed for correcting jet mass)
                    L2cor = L12cor/L1cor
                    L3cor = L123cor/L12cor
                    L23cor = L2cor*L3cor
                    #print 'L1cor '+str(L1cor)+' L2cor '+str(L2cor)+' L3cor '+str(L3cor)+' L23cor '+str(L23cor)+' L123cor '+str(L123cor)

                subjets = jet.subjets("SoftDropPuppi")
                groomedJet = None
                rhoRatio = None
                msubjet0 = -999.
                msubjet1 = -999.
                csv0 = -999.
                csv1 = -999.                
                if len(subjets) >= 2 : 
                    groomedJet = subjets[0].p4() + subjets[1].p4()
                    if subjets[1].mass() > subjets[0].mass() : 
                        msubjet0 = subjets[1].mass()
                        msubjet1 = subjets[0].mass()
                        csv0 = subjets[1].bDiscriminator('pfDeepCSVJetTags:probb')
                        csv1 = subjets[0].bDiscriminator('pfDeepCSVJetTags:probb')
                    else :
                        msubjet0 = subjets[0].mass()
                        msubjet1 = subjets[1].mass()
                        csv1 = subjets[1].bDiscriminator('pfDeepCSVJetTags:probb')
                        csv0 = subjets[0].bDiscriminator('pfDeepCSVJetTags:probb')
                    rhoRatio = pow( groomedJet.mass() / (groomedJet.pt()*0.8), 2)
                
                h_ptAK8.Fill( corr * jet.userFloat('ak8PFJetsCHSValueMap:pt') )
                h_ptAK8Puppi.Fill( corr * uncorrJet.pt())
                h_JECValueAK8.Fill( corr )
                h_ptUncorrAK8.Fill( uncorrJet.pt() )
                h_ptDownAK8.Fill( corrDn * uncorrJet.pt() )
                h_ptUpAK8.Fill( corrUp * uncorrJet.pt() )
                h_etaAK8.Fill( jet.userFloat('ak8PFJetsCHSValueMap:eta') )
                h_yAK8.Fill( jet.y() )
                h_phiAK8.Fill( jet.userFloat('ak8PFJetsCHSValueMap:phi') )
                h_etaAK8Puppi.Fill( jet.eta() )
                h_phiAK8Puppi.Fill( jet.phi() )
                h_mAK8.Fill(  jet.userFloat('ak8PFJetsCHSValueMap:mass') )
                h_areaAK8.Fill( jet.jetArea() )
                h_msoftdropAK8.Fill( jet.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSSoftDropMass') )
                h_mprunedAK8.Fill( jet.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass') )
                h_mpuppiAK8.Fill( jet.mass() )
                h_mSDpuppiAK8.Fill( jet.userFloat('ak8PFJetsPuppiSoftDropMass') )
                ak8pt[0] = corr * jet.userFloat('ak8PFJetsCHSValueMap:pt')
                ak8eta[0] = jet.userFloat('ak8PFJetsCHSValueMap:eta')
                ak8phi[0] = jet.userFloat('ak8PFJetsCHSValueMap:phi')
                ak8PUPPIpt[0] = corr * uncorrJet.pt()
                ak8PUPPIeta[0] = jet.eta()
                ak8PUPPIphi[0] = jet.phi()
                ak8mass[0] = jet.userFloat('ak8PFJetsCHSValueMap:mass')
                ak8csv[0] = jet.bDiscriminator('pfDeepCSVJetTags:probb')
                ak8SDmass[0] = jet.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSSoftDropMass')
                ak8PrunedMass[0] = jet.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass') 
                ak8PUPPImass[0] = jet.mass()
                ak8SDPUPPImass[0] = jet.userFloat('ak8PFJetsPuppiSoftDropMass')
                ak8SD_sub0_mass[0] = msubjet0
                ak8SD_sub1_mass[0] = msubjet1
                ak8SD_sub0_csv[0] = csv0
                ak8SD_sub1_csv[0] = csv1
                ak8_N2_beta1[0] = jet.userFloat('ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN2')
                ak8_N2_beta2[0] = jet.userFloat('ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN2')
                ak8_N3_beta1[0] = jet.userFloat('ak8PFJetsPuppiSoftDropValueMap:nb1AK8PuppiSoftDropN3')
                ak8_N3_beta2[0] = jet.userFloat('ak8PFJetsPuppiSoftDropValueMap:nb2AK8PuppiSoftDropN3')
                npv[0] = float(len(pvs))
                if groomedJet != None : 
                    h_ptGroomedCorrAK8.Fill( groomedJet.pt() )
                    h_msoftdropCorrAK8.Fill( groomedJet.mass() )
                    h_rhoRatioAK8.Fill( rhoRatio )
                    if rhoRatio > 0:
                      h_logrhoRatioAK8.Fill( math.log(rhoRatio) )
                    h_mSubjet0AK8.Fill( msubjet0 )
                    h_mSubjet1AK8.Fill( msubjet1 )
                # Make sure there are top tags if we want to plot them 
                tagInfoLabels = jet.tagInfoLabels()
                hasTopTagInfo = 'caTop' in tagInfoLabels 
                if hasTopTagInfo : 
                    h_minmassAK8.Fill( jet.tagInfo('caTop').properties().minMass )
                    h_nsjAK8.Fill( jet.tagInfo('caTop').properties().nSubJets )
                else :
                    h_minmassAK8.Fill( -1.0 )
                    h_nsjAK8.Fill( -1 )
                # Get n-subjettiness "tau" variables
                tau1 = jet.userFloat('NjettinessAK8Puppi:tau1')
                tau2 = jet.userFloat('NjettinessAK8Puppi:tau2')
                tau3 = jet.userFloat('NjettinessAK8Puppi:tau3')
                if tau1 > 0.0001 :
                    tau21 = tau2 / tau1
                    ak8tau21[0] = tau21
                    h_tau21AK8.Fill( tau21 )
                else :
                    h_tau21AK8.Fill( -1.0 )
                if tau2 > 0.0001 :
                    tau32 = tau3 / tau2
                    ak8tau32[0] = tau32
                    h_tau32AK8.Fill( tau32 )
                else :
                    h_tau32AK8.Fill( -1.0 )

                # Energy correlation functions
                h_ak8_N2_beta1.Fill(ak8_N2_beta1[0])
                h_ak8_N2_beta2.Fill(ak8_N2_beta2[0])
                h_ak8_N3_beta1.Fill(ak8_N3_beta1[0])
                h_ak8_N3_beta2.Fill(ak8_N3_beta2[0])
                varTree.Fill()
                genJet = jet.genJet()
                if genJet != None :
                    h_ptAK8Gen.Fill( genJet.pt() )
                    h_etaAK8Gen.Fill( genJet.eta() )
                    h_yAK8Gen.Fill( genJet.y() )
                    h_phiAK8Gen.Fill( genJet.phi() )
                    h_mAK8Gen.Fill( genJet.mass() )
                    h_areaAK8Gen.Fill( genJet.jetArea() )                    
                if args.verbose == True :
                    if hasTopTagInfo : 
                        print 'Jet {0:4.0f}, pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, nda = {5:3.0f}, softdrop m = {6:6.2f}, pruned m = {7:6.2f}, topmass = {10:6.2f}, minmass = {11:6.2f}'.format(
                            ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(),
                            jet.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSSoftDropMass'),
                            jet.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass'),
                            jet.tagInfo('caTop').properties().topMass, jet.tagInfo('caTop').properties().minMass
                            )
                    else :
                       print 'Jet {0:4.0f}, pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, nda = {5:3.0f}, softdrop m = {6:6.2f}, pruned m = {7:6.2f}'.format(
                            ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(),
                            jet.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSSoftDropMass'),
                            jet.userFloat('ak8PFJetsCHSValueMap:ak8PFJetsCHSPrunedMass'),
                            )
            ijet += 1

        

## _________ .__                                     
## \_   ___ \|  |   ____ _____    ____  __ ________  
## /    \  \/|  | _/ __ \\__  \  /    \|  |  \____ \ 
## \     \___|  |_\  ___/ / __ \|   |  \  |  /  |_> >
##  \______  /____/\___  >____  /___|  /____/|   __/ 
##         \/          \/     \/     \/      |__|    
f.cd()
f.Write()
f.Close()

ts_end = time.time()
print "Total time: {} s".format(ts_end - ts_start)
