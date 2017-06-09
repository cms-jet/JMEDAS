from ROOT import *

gROOT.Macro("rootlogon.C")

f1 = TFile("qcd_short.root")
f2 = TFile("zprime3000_short.root")

h_msoftdropAK8_1   = f1.Get("h_msoftdropAK8")
h_msoftdropAK8_2   = f2.Get("h_msoftdropAK8")

h_msoftdropAK8_1    .SetLineColor(1)
h_msoftdropAK8_2    .SetLineColor(2)

leg = TLegend(0.5, 0.5, 0.8, 0.8)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_msoftdropAK8_1, "QCD", 'l')
leg.AddEntry( h_msoftdropAK8_2, "Z'", 'l')

h_msoftdropAK8_1.Sumw2()
h_msoftdropAK8_1.Scale( 1.0 / h_msoftdropAK8_1.Integral() )
h_msoftdropAK8_2.Sumw2()
h_msoftdropAK8_2.Scale( 1.0 / h_msoftdropAK8_2.Integral() )

c = TCanvas('c', 'c') 
h_msoftdropAK8_1    .Draw("hist")
h_msoftdropAK8_2    .Draw("same hist")
h_mAK8.GetXaxis().SetRangeUser(0, 200)


leg.Draw()

c.Print('plots5.png', 'png')
c.Print('plots5.pdf', 'pdf')
