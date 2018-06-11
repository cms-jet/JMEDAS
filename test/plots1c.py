from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("zprime_ttbar_3000.root")

h_ptAK4   = f.Get("h_ptAK4")
h_etaAK4  = f.Get("h_etaAK4")
h_phiAK4  = f.Get("h_phiAK4")
h_mAK4    = f.Get("h_mAK4")

c = TCanvas('c', 'c', 600, 800)

c.Divide(2,2)
c.cd(1)
gPad.SetLogy()
h_ptAK4.Draw()
h_ptAK4.GetXaxis().SetRangeUser(0, 2000)
c.cd(2)
h_etaAK4.Draw()
c.cd(3)
h_phiAK4.Draw()
h_phiAK4.SetMinimum(0)
c.cd(4)
h_mAK4.Draw()
h_mAK4.GetXaxis().SetRangeUser(0, 200)
gPad.SetLogy()

c.Print('plots1c.png', 'png')
c.Print('plots1c.pdf', 'pdf')
