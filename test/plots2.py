from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("ttjets_short.root")

h_ptAK4   = f.Get("h_ptAK4")
h_etaAK4  = f.Get("h_etaAK4")
h_phiAK4  = f.Get("h_phiAK4")
h_mAK4    = f.Get("h_mAK4")

h_ptAK4Gen   = f.Get("h_ptAK4Gen")
h_etaAK4Gen  = f.Get("h_etaAK4Gen")
h_phiAK4Gen  = f.Get("h_phiAK4Gen")
h_mAK4Gen    = f.Get("h_mAK4Gen")

h_ptAK4Gen   .SetLineStyle(2) 
h_etaAK4Gen  .SetLineStyle(2) 
h_phiAK4Gen  .SetLineStyle(2) 
h_mAK4Gen    .SetLineStyle(2) 

h_ptAK4Gen   .SetLineColor(2) 
h_etaAK4Gen  .SetLineColor(2) 
h_phiAK4Gen  .SetLineColor(2) 
h_mAK4Gen    .SetLineColor(2)

c = TCanvas('c', 'c', 600, 800)

c.Divide(2,2)
c.cd(1)
gPad.SetLogy()
h_ptAK4.Draw()
h_ptAK4Gen.Draw("same")
h_ptAK4.GetXaxis().SetRangeUser(0, 1000)
c.cd(2)
h_etaAK4.Draw()
h_etaAK4Gen.Draw("same")
c.cd(3)
h_phiAK4.Draw()
h_phiAK4Gen.Draw("same")
h_phiAK4.SetMinimum(0)
c.cd(4)
h_mAK4.Draw()
h_mAK4Gen.Draw("same")
h_mAK4.GetXaxis().SetRangeUser(0, 200)
gPad.SetLogy()

c.Print('plots2.png', 'png')
c.Print('plots2.pdf', 'pdf')
