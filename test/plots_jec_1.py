from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("ttjets_short.root")

h_ptAK4   = f.Get("h_ptAK4")
h_ptAK4Uncorr   = f.Get("h_ptUncorrAK4")
h_ptAK4Uncorr   .SetLineStyle(2) 
h_ptAK4Uncorr   .SetLineColor(2) 

c = TCanvas('c', 'c')

h_ptAK4.Draw()
h_ptAK4Uncorr.Draw("same")
h_ptAK4.GetXaxis().SetRangeUser(0, 1000)

c.Print('plots_jec_1.png', 'png')
c.Print('plots_jec_1.pdf', 'pdf')
