from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("ttjets_short.root")

h_ptAK4   = f.Get("h_ptAK4")
h_etaAK4  = f.Get("h_etaAK4")
h_phiAK4  = f.Get("h_phiAK4")
h_mAK4    = f.Get("h_mAK4")

h_ptAK8   = f.Get("h_ptAK8")
h_etaAK8  = f.Get("h_etaAK8")
h_phiAK8  = f.Get("h_phiAK8")
h_mAK8    = f.Get("h_mAK8")

h_ptAK8   .SetLineStyle(2) 
h_etaAK8  .SetLineStyle(2) 
h_phiAK8  .SetLineStyle(2) 
h_mAK8    .SetLineStyle(2) 

h_ptAK8   .SetLineColor(2) 
h_etaAK8  .SetLineColor(2) 
h_phiAK8  .SetLineColor(2) 
h_mAK8    .SetLineColor(2)

c = TCanvas('c', 'c', 600, 800)

c.Divide(2,2)
c.cd(1)
gPad.SetLogy()
h_ptAK4.Draw()
h_ptAK8.Draw("same")
h_ptAK4.GetXaxis().SetRangeUser(0, 1000)
c.cd(2)
h_etaAK4.Draw()
h_etaAK8.Draw("same")
c.cd(3)
h_phiAK4.Draw()
h_phiAK8.Draw("same")
h_phiAK4.SetMinimum(0)
c.cd(4)
h_mAK4.Draw()
h_mAK8.Draw("same")
h_mAK4.GetXaxis().SetRangeUser(0, 200)
gPad.SetLogy()

c.Print('plotAK4AK8.png', 'png')
c.Print('plotAK4AK8.pdf', 'pdf')
