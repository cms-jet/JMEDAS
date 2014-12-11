from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("ttjets_short.root")

h_areaAK4   = f.Get("h_areaAK4")
h_areaAK8   = f.Get("h_areaAK8")
h_areaAK8.SetLineStyle(4)
h_areaAK8.SetLineColor(4)

h_areaAK4.Scale( 1.0 / h_areaAK4.Integral() )
h_areaAK8.Scale( 1.0 / h_areaAK8.Integral() )

c = TCanvas('c', 'c')
h_areaAK4.Draw('hist')
h_areaAK8.Draw("hist same")

c.Print('plots3.png', 'png')
c.Print('plots3.pdf', 'pdf')
