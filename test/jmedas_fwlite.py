#! /usr/bin/env python


## _________                _____.__                            __  .__               
## \_   ___ \  ____   _____/ ____\__| ____  __ ______________ _/  |_|__| ____   ____  
## /    \  \/ /  _ \ /    \   __\|  |/ ___\|  |  \_  __ \__  \\   __\  |/  _ \ /    \ 
## \     \___(  <_> )   |  \  |  |  / /_/  >  |  /|  | \// __ \|  | |  (  <_> )   |  \
##  \______  /\____/|___|  /__|  |__\___  /|____/ |__|  (____  /__| |__|\____/|___|  /
##         \/            \/        /_____/                   \/                    \/ 

from optparse import OptionParser
parser = OptionParser()

parser.add_option('--files', type='string', action='store',
                  dest='files',
                  help='Input files')

parser.add_option('--outname', type='string', action='store',
                  default='outplots.root',
                  dest='outname',
                  help='Name of output file')

parser.add_option('--verbose', action='store_true',
                  default=False,
                  dest='verbose',
                  help='Print debugging info')

parser.add_option('--correctJets', action='store_true',
                  default=False,
                  dest='correctJets',
                  help='Apply latest jet corrections.')

parser.add_option('--smearJets', action='store_true',
                  default=False,
                  dest='smearJets',
                  help='Smear jet energy.')


parser.add_option('--maxevents', type='int', action='store',
                  default=-1,
                  dest='maxevents',
                  help='Number of events to run. -1 is all events')

parser.add_option('--maxjets', type='int', action='store',
                  default=999,
                  dest='maxjets',
                  help='Number of jets to plot. To plot all jets, set to a big number like 999')



parser.add_option('--minAK8Pt', type='float', action='store',
                  default=200.,
                  dest='minAK8Pt',
                  help='Minimum PT for AK8 jets')

parser.add_option('--maxAK8Rapidity', type='float', action='store',
                  default=2.4,
                  dest='maxAK8Rapidity',
                  help='Maximum AK8 rapidity')


parser.add_option('--minAK4Pt', type='float', action='store',
                  default=30.,
                  dest='minAK4Pt',
                  help='Minimum PT for AK4 jets')

parser.add_option('--maxAK4Rapidity', type='float', action='store',
                  default=2.4,
                  dest='maxAK4Rapidity',
                  help='Maximum AK4 rapidity')


parser.add_option('--xrootd', type='string', action='store',
                  default='cmsxrootd.fnal.gov',
                  dest='xrootd',
                  help='xrootd redirect string')


(options, args) = parser.parse_args()
argv = []


## _____________      __.____    .__  __             _________ __          _____  _____ 
## \_   _____/  \    /  \    |   |__|/  |_  ____    /   _____//  |_ __ ___/ ____\/ ____\
##  |    __) \   \/\/   /    |   |  \   __\/ __ \   \_____  \\   __\  |  \   __\\   __\ 
##  |     \   \        /|    |___|  ||  | \  ___/   /        \|  | |  |  /|  |   |  |   
##  \___  /    \__/\  / |_______ \__||__|  \___  > /_______  /|__| |____/ |__|   |__|   
##      \/          \/          \/             \/          \/                           

import ROOT
import sys
import copy
from DataFormats.FWLite import Events, Handle
ROOT.gROOT.Macro("rootlogon.C")
jethandle0  = Handle ("std::vector<pat::Jet>")
jetlabel0 = ("slimmedJets")
jethandle1  = Handle ("std::vector<pat::Jet>")
jetlabel1 = ("slimmedJetsAK8")

rhoHandle = Handle ("double")
rhoLabel = ("fixedGridRhoAll")

pvHandle = Handle("std::vector<reco::Vertex>")
pvLabel = ("offlineSlimmedPrimaryVertices")



if options.correctJets : 
    ### JEC implementation

    vPar = ROOT.vector(ROOT.JetCorrectorParameters)()
    vPar.push_back( ROOT.JetCorrectorParameters('PHYS14_25_V1_L1FastJet_AK4PFchs.txt') )
    vPar.push_back( ROOT.JetCorrectorParameters('PHYS14_25_V1_L2Relative_AK4PFchs.txt') )
    vPar.push_back( ROOT.JetCorrectorParameters('PHYS14_25_V1_L3Absolute_AK4PFchs.txt') )
    jec = ROOT.FactorizedJetCorrector( vPar )
    jecUnc = ROOT.JetCorrectionUncertainty( 'PHYS14_25_V1_Uncertainty_AK4PFchs.txt' )

    vParAK8 = ROOT.vector(ROOT.JetCorrectorParameters)()
    vParAK8.push_back( ROOT.JetCorrectorParameters('PHYS14_25_V1_L1FastJet_AK8PFchs.txt') )
    vParAK8.push_back( ROOT.JetCorrectorParameters('PHYS14_25_V1_L2Relative_AK8PFchs.txt') )
    vParAK8.push_back( ROOT.JetCorrectorParameters('PHYS14_25_V1_L3Absolute_AK8PFchs.txt') )
    jecAK8 = ROOT.FactorizedJetCorrector( vParAK8 )

    jecUncAK8 = ROOT.JetCorrectionUncertainty( 'PHYS14_25_V1_Uncertainty_AK8PFchs.txt' )


##   ___ ___ .__          __                                             
##  /   |   \|__| _______/  |_  ____   ________________    _____   ______
## /    ~    \  |/  ___/\   __\/  _ \ / ___\_  __ \__  \  /     \ /  ___/
## \    Y    /  |\___ \  |  | (  <_> ) /_/  >  | \// __ \|  Y Y  \\___ \ 
##  \___|_  /|__/____  > |__|  \____/\___  /|__|  (____  /__|_|  /____  >
##        \/         \/             /_____/            \/      \/     \/

f = ROOT.TFile(options.outname, "RECREATE")
f.cd()

h_ptAK4 = ROOT.TH1F("h_ptAK4", "AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptUpAK4 = ROOT.TH1F("h_ptUpAK4", "JEC Up AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptDownAK4 = ROOT.TH1F("h_ptDownAK4", "JEC Down AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptUncorrAK4 = ROOT.TH1F("h_ptUncorrAK4", "UnCorrected AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_JECValueAK4 = ROOT.TH1F("h_JECValueAK4", "Value of JEC for AK4 Jet", 100, 0.8, 1.1)
h_etaAK4 = ROOT.TH1F("h_etaAK4", "AK4 Jet #eta;#eta", 120, -6, 6)
h_yAK4 = ROOT.TH1F("h_yAK4", "AK4 Jet Rapidity;y", 120, -6, 6)
h_phiAK4 = ROOT.TH1F("h_phiAK4", "AK4 Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK4 = ROOT.TH1F("h_mAK4", "AK4 Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK4 = ROOT.TH1F("h_areaAK4", "AK4 Jet Area;Area", 250, 0, 5.0)

h_ptAK4Gen = ROOT.TH1F("h_ptAK4Gen", "AK4Gen Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_etaAK4Gen = ROOT.TH1F("h_etaAK4Gen", "AK4Gen Jet #eta;#eta", 120, -6, 6)
h_yAK4Gen = ROOT.TH1F("h_yAK4Gen", "AK4Gen Jet Rapidity;y", 120, -6, 6)
h_phiAK4Gen = ROOT.TH1F("h_phiAK4Gen", "AK4Gen Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK4Gen = ROOT.TH1F("h_mAK4Gen", "AK4Gen Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK4Gen = ROOT.TH1F("h_areaAK4Gen", "AK4Gen Jet Area;Area", 250, 0, 5.0)


h_ptAK8 = ROOT.TH1F("h_ptAK8", "AK8 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptUpAK8 = ROOT.TH1F("h_ptUpAK8", "JEC Up AK8 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptDownAK8 = ROOT.TH1F("h_ptDownAK8", "JEC Down AK8 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_ptUncorrAK8 = ROOT.TH1F("h_ptUncorrAK8", "UnCorrected AK8 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_JECValueAK8 = ROOT.TH1F("h_JECValueAK8", "Value of JEC for AK8 Jet", 100, 0.8, 1.1)
h_etaAK8 = ROOT.TH1F("h_etaAK8", "AK8 Jet #eta;#eta", 120, -6, 6)
h_yAK8 = ROOT.TH1F("h_yAK8", "AK8 Jet Rapidity;y", 120, -6, 6)
h_phiAK8 = ROOT.TH1F("h_phiAK8", "AK8 Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK8 = ROOT.TH1F("h_mAK8", "AK8 Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK8 = ROOT.TH1F("h_areaAK8", "AK8 Jet Area;Area", 250, 0, 5.0)
h_msoftdropAK8 = ROOT.TH1F("h_msoftdropAK8", "AK8 Softdrop Jet Mass;Mass (GeV)", 100, 0, 1000)
h_mprunedAK8 = ROOT.TH1F("h_mprunedAK8", "AK8 Pruned Jet Mass;Mass (GeV)", 100, 0, 1000)
h_mfilteredAK8 = ROOT.TH1F("h_mfilteredAK8", "AK8 Filtered Jet Mass;Mass (GeV)", 100, 0, 1000)
h_mtrimmedAK8 = ROOT.TH1F("h_mtrimmedAK8", "AK8 Trimmed Jet Mass;Mass (GeV)", 100, 0, 1000)
h_minmassAK8 = ROOT.TH1F("h_minmassAK8", "AK8 CMS Top Tagger Min Mass Paring;m_{min} (GeV)", 100, 0, 1000)
h_nsjAK8 = ROOT.TH1F("h_nsjAK8", "AK8 CMS Top Tagger N_{subjets};N_{subjets}", 5, 0, 5)
h_tau21AK8 = ROOT.TH1F("h_tau21AK8", "AK8 Jet #tau_{2} / #tau_{1};Mass#tau_{21}", 100, 0, 1.0)
h_tau32AK8 = ROOT.TH1F("h_tau32AK8", "AK8 Jet #tau_{3} / #tau_{2};Mass#tau_{32}", 100, 0, 1.0)

h_ptAK8Gen = ROOT.TH1F("h_ptAK8Gen", "AK8Gen Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
h_etaAK8Gen = ROOT.TH1F("h_etaAK8Gen", "AK8Gen Jet #eta;#eta", 120, -6, 6)
h_yAK8Gen = ROOT.TH1F("h_yAK8Gen", "AK8Gen Jet Rapidity;y", 120, -6, 6)
h_phiAK8Gen = ROOT.TH1F("h_phiAK8Gen", "AK8Gen Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK8Gen = ROOT.TH1F("h_mAK8Gen", "AK8Gen Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK8Gen = ROOT.TH1F("h_areaAK8Gen", "AK8Gen Jet Area;Area", 250, 0, 5.0)




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
    etamin = [0.0,0.5,1.1,1.7,2.3,2.8,3.2]
    etamax = [0.5,1.1,1.7,2.3,2.8,3.2,5.0]
    
    scale_nom = [1.079,1.099,1.121,1.208,1.254,1.395,1.056]
    scale_dn  = [1.053,1.071,1.092,1.162,1.192,1.332,0.865]
    scale_up  = [1.105,1.127,1.150,1.254,1.316,1.458,1.247]

    for iSF in range(0,len(scale_nom)) :
        if abs(jetEta) >= etamin[iSF] and abs(jetEta) < etamax[iSF] :
            if sysType < 0 :
                jerSF = scale_dn[iSF]
            elif sysType > 0 :
                jerSF = scale_up[iSF]
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
filelist = file( options.files )
filesraw = filelist.readlines()
files = []
nevents = 0
for ifile in filesraw :
    if len( ifile ) > 2 : 
        s = 'root://' + options.xrootd + '/' + ifile.rstrip()
        files.append( s )
        print 'Added ' + s


# loop over files
for ifile in files :
    print 'Processing file ' + ifile
    events = Events (ifile)
    if options.maxevents > 0 and nevents > options.maxevents :
        break

    # loop over events in this file
    i = 0
    for event in events:
        if options.maxevents > 0 and nevents > options.maxevents :
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


        if options.verbose :
            print '------ AK4 jets ------'
        # use getByLabel, just like in cmsRun
        event.getByLabel (jetlabel0, jethandle0)
        # get the product
        jets0 = jethandle0.product()
        # loop over jets and fill hists
        ijet = 0
        for jet in jets0 :
            if ijet >= options.maxjets :
                break
            if jet.pt() > options.minAK4Pt and abs(jet.rapidity()) < options.maxAK4Rapidity :
                
                
                #FInd the jet correction
                uncorrJet = copy.copy( jet.correctedP4(0) ) # For some reason, in python this is interfering with jet.genJet() in strange ways without the copy.copy

                if uncorrJet.E() < 0.00001 :
                    print 'Very strange. Uncorrected jet E = ' + str( uncorrJet.E()) + ', but Corrected jet E = ' + str( jet.energy() )
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
                if options.smearJets  :
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
                if options.correctJets : 
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
                    jecUnc.setJetPt( corr * uncorrJet.pt() )
                    corrUp += jecUnc.getUncertainty(1)
                    jecUnc.setJetEta( uncorrJet.eta() )
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
                genJet = jet.genJet()
                if genJet != None :
                    h_ptAK4Gen.Fill( genJet.pt() )
                    h_etaAK4Gen.Fill( genJet.eta() )
                    h_yAK4Gen.Fill( genJet.y() )
                    h_phiAK4Gen.Fill( genJet.phi() )
                    h_mAK4Gen.Fill( genJet.mass() )
                    h_areaAK4Gen.Fill( genJet.jetArea() )
                if options.verbose == True : 
                    print ("Jet {0:4.0f}, orig pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, " +
                           "nda = {5:3.0f}, vtxmass = {6:6.2f}, area = {7:6.2f}, corr = {8:6.3f} +{9:6.3f} -{10:6.3f} ").format(
                        ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(), jet.userFloat('secvtxMass'),
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
        if options.verbose :
            print '------ AK8 jets ------'
        # use getByLabel, just like in cmsRun
        event.getByLabel (jetlabel1, jethandle1)
        # get the product
        jets1 = jethandle1.product()
        # loop over jets and fill hists
        ijet = 0
        for jet in jets1 :
            if ijet >= options.maxjets :
                break
            if jet.pt() > options.minAK8Pt and abs(jet.rapidity()) < options.maxAK8Rapidity :
                
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
                if options.smearJets  :
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
                if options.correctJets : 
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


                h_ptAK8.Fill( corr * uncorrJet.pt() )
                h_JECValueAK8.Fill( corr )
                h_ptUncorrAK8.Fill( uncorrJet.pt() )
                h_ptDownAK8.Fill( corrDn * uncorrJet.pt() )
                h_ptUpAK8.Fill( corrUp * uncorrJet.pt() )
                h_etaAK8.Fill( jet.eta() )
                h_yAK8.Fill( jet.y() )
                h_phiAK8.Fill( jet.phi() )
                h_mAK8.Fill( jet.mass() )
                h_areaAK8.Fill( jet.jetArea() )
                h_msoftdropAK8.Fill( jet.userFloat('ak8PFJetsCHSSoftdropMass') )
                h_mprunedAK8.Fill( jet.userFloat('ak8PFJetsCHSPrunedMass') )
                h_mtrimmedAK8.Fill( jet.userFloat('ak8PFJetsCHSTrimmedMass') )
                h_mfilteredAK8.Fill( jet.userFloat('ak8PFJetsCHSFilteredMass') )
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
                tau1 = jet.userFloat('NjettinessAK8:tau1')
                tau2 = jet.userFloat('NjettinessAK8:tau2')
                tau3 = jet.userFloat('NjettinessAK8:tau3')
                if tau1 > 0.0001 :
                    tau21 = tau2 / tau1
                    h_tau21AK8.Fill( tau21 )
                else :
                    h_tau21AK8.Fill( -1.0 )
                if tau2 > 0.0001 :
                    tau32 = tau3 / tau2
                    h_tau32AK8.Fill( tau32 )
                else :
                    h_tau32AK8.Fill( -1.0 )

                genJet = jet.genJet()
                if genJet != None :
                    h_ptAK8Gen.Fill( genJet.pt() )
                    h_etaAK8Gen.Fill( genJet.eta() )
                    h_yAK8Gen.Fill( genJet.y() )
                    h_phiAK8Gen.Fill( genJet.phi() )
                    h_mAK8Gen.Fill( genJet.mass() )
                    h_areaAK8Gen.Fill( genJet.jetArea() )                    
                if options.verbose == True :
                    if hasTopTagInfo : 
                        print 'Jet {0:4.0f}, pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, nda = {5:3.0f}, softdrop m = {6:6.2f}, pruned m = {7:6.2f}, trimmed m = {8:6.2f}, filtered m = {9:6.2f}, topmass = {10:6.2f}, minmass = {11:6.2f}'.format(
                            ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(),
                            jet.userFloat('ak8PFJetsCHSSoftDropMass'),
                            jet.userFloat('ak8PFJetsCHSPrunedMass'), jet.userFloat('ak8PFJetsCHSTrimmedMass'), jet.userFloat('ak8PFJetsCHSFilteredMass'),
                            jet.tagInfo('caTop').properties().topMass, jet.tagInfo('caTop').properties().minMass
                            )
                    else :
                       print 'Jet {0:4.0f}, pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, nda = {5:3.0f}, softdrop m = {6:6.2f}, pruned m = {7:6.2f}, trimmed m = {8:6.2f}, filtered m = {9:6.2f}, topmass = {10:6.2f}, minmass = {11:6.2f}'.format(
                            ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(),
                            jet.userFloat('ak8PFJetsCHSSoftDropMass'),
                            jet.userFloat('ak8PFJetsCHSPrunedMass'), jet.userFloat('ak8PFJetsCHSTrimmedMass'), jet.userFloat('ak8PFJetsCHSFilteredMass'),
                            -1.0, -1.0
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
