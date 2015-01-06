from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("ttjets_short.root")

h_ptAK4   = f.Get("h_ptAK4")
h_ptAK4Up  = f.Get("h_ptJECUpAK4")
h_ptAK4Down  = f.Get("h_ptJECDownAK4")
h_ptAK4Up   .SetLineStyle(2)
h_ptAK4Up   .SetLineColor(kGreen+1) 
h_ptAK4Down   .SetLineStyle(2)
h_ptAK4Down   .SetLineColor(kRed) 
h_ptAK4Up     .SetLineWidth(2)
h_ptAK4Down   .SetLineWidth(2)
h_ptAK4       .SetLineWidth(2)

c = TCanvas('c', 'c')

h_ptAK4.Draw()
h_ptAK4Up.Draw("same")
h_ptAK4Down.Draw("same")
h_ptAK4.GetXaxis().SetRangeUser(0, 400)

leg = TLegend(0.45, 0.55, 0.75, 0.8)
leg.AddEntry(h_ptAK4, "Nominal JEC", "l")
leg.AddEntry(h_ptAK4Up, "JEC +1 #sigma", "l")
leg.AddEntry(h_ptAK4Down, "JEC -1 #sigma", "l")
leg.SetLineWidth(0)
leg.SetFillColor(0)
leg.SetShadowColor(0)
leg.Draw()


c.Print('plots_jec_2.png', 'png')
c.Print('plots_jec_2.pdf', 'pdf')
