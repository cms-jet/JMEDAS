from ROOT import *

gROOT.Macro("rootlogon.C")

f1 = TFile("qcd_highPt.root")
f2 = TFile("zprime_ttbar_3000.root")

h_tau21AK8_1   = f1.Get("h_tau21AK8")
h_tau21AK8_2   = f2.Get("h_tau21AK8")

h_tau21AK8_1    .SetLineColor(1)
h_tau21AK8_2    .SetLineColor(2)

leg = TLegend(0.15, 0.5, 0.35, 0.8)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_tau21AK8_1, "QCD", 'l')
leg.AddEntry( h_tau21AK8_2, "Z'#rightarrow t#bar{t}", 'l')

h_tau21AK8_1.Sumw2()
h_tau21AK8_1.Scale( 1.0 / h_tau21AK8_1.Integral() )
h_tau21AK8_2.Sumw2()
h_tau21AK8_2.Scale( 1.0 / h_tau21AK8_2.Integral() )

c = TCanvas('c', 'c') 
h_tau21AK8_1    .Draw("hist")
h_tau21AK8_2    .Draw("same hist")


leg.Draw()

c.Print('plots9.png', 'png')
c.Print('plots9.pdf', 'pdf')
