# import ROOT in batch mode
import sys
oldargv = sys.argv[:]
sys.argv = [ '-b-' ]
import ROOT
from ROOT import *
ROOT.gROOT.SetBatch(True)
sys.argv = oldargv

inputFile = TFile.Open('root://xrootd-cms.infn.it//store/mc/RunIIAutumn18NanoAODv4/QCD_HT1000to1500_TuneCP5_13TeV-madgraphMLM-pythia8/NANOAODSIM/Nano14Dec2018_102X_upgrade2018_realistic_v16-v1/110000/C23F77AA-3909-C74E-ADCD-8266FF68AB5D.root' )
events = inputFile.Get('Events')

for iev in xrange(events.GetEntries()):
    events.GetEntry(iev)
    if iev >= 10: break

    print "\nEvent %d: run %6d, lumi %4d, event %12d" % (iev, events.run, events.luminosityBlock, events.event )

    # AK4 CHS Jets
    for ijet in range(events.nJet):
        if events.Jet_pt < 20: continue
        print 'AK4 jet '+ str(ijet) + ': pt ' + str(events.Jet_pt[ijet]) + ', eta ' + str(events.Jet_eta[ijet]) + ', mass ' + str(events.Jet_mass[ijet]) + ',phi ' + str(events.Jet_phi[ijet]) + ', puId ' + str(events.Jet_puId[ijet]) + ', deepJet btag disc. ' + str(events.Jet_btagDeepB[ijet])

    # AK8 PUPPI Jets
    for ijet in range(events.nFatJet):
        if events.FatJet_pt < 20: continue
        print 'AK8 jet '+ str(ijet) + ': pt ' + str(events.FatJet_pt[ijet]) + ', eta ' + str(events.FatJet_eta[ijet]) + ', mass ' + str(events.FatJet_mass[ijet]) + ',phi ' + str(events.FatJet_phi[ijet]) + ', deepAK8 W tag disc. ' + str(events.FatJet_deepTag_WvsQCD[ijet])+ ', deepAK8 top tag disc. ' + str(events.FatJet_deepTag_TvsQCD[ijet])
