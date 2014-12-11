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
from DataFormats.FWLite import Events, Handle
ROOT.gROOT.Macro("rootlogon.C")
jethandle0  = Handle ("std::vector<pat::Jet>")
jetlabel0 = ("slimmedJets")
jethandle1  = Handle ("std::vector<pat::Jet>")
jetlabel1 = ("slimmedJetsAK8")

##   ___ ___ .__          __                                             
##  /   |   \|__| _______/  |_  ____   ________________    _____   ______
## /    ~    \  |/  ___/\   __\/  _ \ / ___\_  __ \__  \  /     \ /  ___/
## \    Y    /  |\___ \  |  | (  <_> ) /_/  >  | \// __ \|  Y Y  \\___ \ 
##  \___|_  /|__/____  > |__|  \____/\___  /|__|  (____  /__|_|  /____  >
##        \/         \/             /_____/            \/      \/     \/

f = ROOT.TFile(options.outname, "RECREATE")
f.cd()

h_ptAK4 = ROOT.TH1F("h_ptAK4", "AK4 Jet p_{T};p_{T} (GeV)", 300, 0, 3000)
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
h_etaAK8 = ROOT.TH1F("h_etaAK8", "AK8 Jet #eta;#eta", 120, -6, 6)
h_yAK8 = ROOT.TH1F("h_yAK8", "AK8 Jet Rapidity;y", 120, -6, 6)
h_phiAK8 = ROOT.TH1F("h_phiAK8", "AK8 Jet #phi;#phi (radians)",100,-ROOT.Math.Pi(),ROOT.Math.Pi())
h_mAK8 = ROOT.TH1F("h_mAK8", "AK8 Jet Mass;Mass (GeV)", 100, 0, 1000)
h_areaAK8 = ROOT.TH1F("h_areaAK8", "AK8 Jet Area;Area", 250, 0, 5.0)
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
        s = 'root://cmsxrootd.fnal.gov/' + ifile.rstrip()
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


        # use getByLabel, just like in cmsRun
        event.getByLabel (jetlabel0, jethandle0)
        # get the product
        jets0 = jethandle0.product()
        # loop over jets and fill hists
        ijet = 0
        for jet in jets0 :
            if ijet > options.maxjets :
                break
            if jet.pt() > options.minAK4Pt and abs(jet.rapidity()) < options.maxAK4Rapidity :
                h_ptAK4.Fill( jet.pt() )
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
                    print ("Jet {0:4.0f}, pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, " +
                           "nda = {5:3.0f}, vtxmass = {6:6.2f}, area = {7:6.2f}, L1 = {8:6.2f}, L2 = {9:6.2f}, L3 = {10:6.2f}, " +
                           "currLevel = {11:s}").format(
                        ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(), jet.userFloat('secvtxMass'),
                        jet.jetArea(), jet.jecFactor("L1FastJet"), jet.jecFactor("L2Relative"), jet.jecFactor("L3Absolute"), jet.currentJECLevel()
                        ),
                    if jet.genJetFwdRef().isNonnull() and jet.genJetFwdRef().isAvailable() :
                        genPt = jet.genJetFwdRef().pt()
                        print (", gen pt = {0:6.2f}").format( genPt )
                    else :
                        print ''
            ijet += 1


        ##    _____   ____  __. ______        ____.       __    __________.__          __          
        ##   /  _  \ |    |/ _|/  __  \      |    | _____/  |_  \______   \  |   _____/  |_  ______
        ##  /  /_\  \|      <  >      <      |    |/ __ \   __\  |     ___/  |  /  _ \   __\/  ___/
        ## /    |    \    |  \/   --   \ /\__|    \  ___/|  |    |    |   |  |_(  <_> )  |  \___ \ 
        ## \____|__  /____|__ \______  / \________|\___  >__|    |____|   |____/\____/|__| /____  >
        ##         \/        \/      \/                \/                                       \/ 

        # use getByLabel, just like in cmsRun
        event.getByLabel (jetlabel1, jethandle1)
        # get the product
        jets1 = jethandle1.product()
        # loop over jets and fill hists
        ijet = 0
        for jet in jets1 :
            if ijet > options.maxjets :
                break
            if jet.pt() > options.minAK8Pt and abs(jet.rapidity()) < options.maxAK8Rapidity :
                h_ptAK8.Fill( jet.pt() )
                h_etaAK8.Fill( jet.eta() )
                h_yAK8.Fill( jet.y() )
                h_phiAK8.Fill( jet.phi() )
                h_mAK8.Fill( jet.mass() )
                h_areaAK8.Fill( jet.jetArea() )
                h_mprunedAK8.Fill( jet.userFloat('ak8PFJetsCHSPrunedLinks') )
                h_mtrimmedAK8.Fill( jet.userFloat('ak8PFJetsCHSTrimmedLinks') )
                h_mfilteredAK8.Fill( jet.userFloat('ak8PFJetsCHSFilteredLinks') )
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
                        print 'Jet {0:4.0f}, pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, nda = {5:3.0f}, pruned m = {6:6.2f}, trimmed m = {7:6.2f}, filtered m = {8:6.2f}, topmass = {9:6.2f}, minmass = {10:6.2f}'.format(
                            ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(), 
                            jet.userFloat('ak8PFJetsCHSPrunedLinks'), jet.userFloat('ak8PFJetsCHSTrimmedLinks'), jet.userFloat('ak8PFJetsCHSFilteredLinks'),
                            jet.tagInfo('caTop').properties().topMass, jet.tagInfo('caTop').properties().minMass
                            )
                    else :
                        print 'Jet {0:4.0f}, pt = {1:10.2f}, eta = {2:6.2f}, phi = {3:6.2f}, m = {4:6.2f}, nda = {5:3.0f}, pruned m = {6:6.2f}, trimmed m = {7:6.2f}, filtered m = {8:6.2f}, topmass = {9:6.2f}, minmass = {10:6.2f}'.format(
                            ijet, jet.pt(), jet.eta(), jet.phi(), jet.mass(), jet.numberOfDaughters(), 
                            jet.userFloat('ak8PFJetsCHSPrunedLinks'), jet.userFloat('ak8PFJetsCHSTrimmedLinks'), jet.userFloat('ak8PFJetsCHSFilteredLinks'), -1.0, -1.0
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
