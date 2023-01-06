# Loads the ROOT environment and style
import ROOT as r
from Analysis.JMEDAS.pileupCorr import *

inf = r.TFile("PileupHistograms.root","READ")
c = MakeCanvas(filename="PileupHistograms.root")
c.Draw()
c.Print('plot5.pdf','pdf')
