from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("ttjets_short.root")

h_ptAK4   = f.Get("h_ptAK4")
h_ptAK4Up  = f.Get("h_ptJECUpAK4")
h_ptAK4Down  = f.Get("h_ptJECDownAK4")
h_ptAK4Up   .SetLineStyle(2)
h_ptAK4Up   .SetLineColor(2) 
h_ptAK4Down   .SetLineStyle(2)
h_ptAK4Down   .SetLineColor(2) 

c = TCanvas('c', 'c')

h_ptAK4.Draw()
h_ptAK4Up.Draw("same")
h_ptAK4Down.Draw("same")
h_ptAK4.GetXaxis().SetRangeUser(0, 400)

c.Print('plots_jec_2.png', 'png')
c.Print('plots_jec_2.pdf', 'pdf')
