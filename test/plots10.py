from ROOT import *

gROOT.Macro("rootlogon.C")

f1 = TFile("ttjets_short.root")
f2 = TFile("rsgluon_ttbar_3TeV.root")

h_tau32AK8_1   = f1.Get("h_tau32AK8")
h_tau32AK8_2   = f2.Get("h_tau32AK8")

h_tau32AK8_1    .SetLineColor(1)
h_tau32AK8_2    .SetLineColor(2)

leg = TLegend(0.3, 0.5, 0.5, 0.8)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_tau32AK8_1, "t#bar{t}", 'l')
leg.AddEntry( h_tau32AK8_2, "RS KK Gluon", 'l')

h_tau32AK8_1.Sumw2()
h_tau32AK8_1.Scale( 1.0 / h_tau32AK8_1.Integral() )
h_tau32AK8_2.Sumw2()
h_tau32AK8_2.Scale( 1.0 / h_tau32AK8_2.Integral() )

c = TCanvas('c', 'c') 
h_tau32AK8_1    .Draw("hist")
h_tau32AK8_2    .Draw("same hist")


leg.Draw()

c.Print('plots10.png', 'png')
c.Print('plots10.pdf', 'pdf')
