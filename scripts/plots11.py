from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("rsgluon_ttbar_3TeV.root")

h_massAK8_1   = f.Get("h_mAK8")
h_massAK8_2   = f.Get("h_msoftdropAK8")
h_massAK8_3   = f.Get("h_mpuppiAK8")

h_massAK8_1    .SetLineColor(1)
h_massAK8_2    .SetLineColor(2)
h_massAK8_3    .SetLineColor(3)

leg = TLegend(0.5, 0.5, 0.7, 0.8)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_massAK8_1, "", "")
leg.AddEntry( h_massAK8_1, "CHS", 'l')
leg.AddEntry( h_massAK8_2, "Soft Drop", 'l')
leg.AddEntry( h_massAK8_3, "PUPPI", 'l')

h_massAK8_1.Sumw2()
h_massAK8_1.Scale( 1.0 / h_massAK8_1.Integral() )
h_massAK8_2.Sumw2()
h_massAK8_2.Scale( 1.0 / h_massAK8_2.Integral() )
h_massAK8_3.Sumw2()
h_massAK8_3.Scale( 1.0 / h_massAK8_3.Integral() )

c = TCanvas('c', 'c') 
h_massAK8_1    .Draw("hist")
h_massAK8_2    .Draw("same hist")
h_massAK8_3    .Draw("same hist")


leg.Draw()

c.Print('plots11.png', 'png')
c.Print('plots11.pdf', 'pdf')
