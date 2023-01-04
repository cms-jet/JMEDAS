import os
import sys

# Loads the ROOT environment and style
import ROOT
from collections import OrderedDict

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)

# Imports for running locally
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/Analysis/JMEDAS/python"))

f = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets.root")

h_ptAK4   = f.Get("h_ptAK4")
h_etaAK4  = f.Get("h_etaAK4")
h_phiAK4  = f.Get("h_phiAK4")
h_mAK4    = f.Get("h_mAK4")

c = ROOT.TCanvas('c', 'c', 800, 600)

c.Divide(2,2)
c.cd(1)
ROOT.gPad.SetLogy()
h_ptAK4.Draw()
h_ptAK4.GetXaxis().SetRangeUser(0, 1000)
c.cd(2)
h_etaAK4.Draw()
c.cd(3)
h_phiAK4.Draw()
h_phiAK4.SetMinimum(0)
c.cd(4)
ROOT.gPad.SetLogy()
h_mAK4.Draw()
h_mAK4.GetXaxis().SetRangeUser(0, 200)
ROOT.gPad.SetLogy()

c.SaveAs('plots1.pdf', 'pdf')


