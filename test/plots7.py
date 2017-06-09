from ROOT import *

gROOT.Macro("rootlogon.C")

f1 = TFile("ttjets_short.root")
f2 = TFile("zprime3000_short.root")

h_mSubjet0AK8_1   = f1.Get("h_mSubjet0AK8")
h_mSubjet0AK8_2   = f2.Get("h_mSubjet0AK8")

h_mSubjet0AK8_1    .SetLineColor(1)
h_mSubjet0AK8_2    .SetLineColor(2)

leg = TLegend(0.5, 0.5, 0.8, 0.8)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_mSubjet0AK8_1, "t#bar{t}", 'l')
leg.AddEntry( h_mSubjet0AK8_2, "RS KK Gluon", 'l')

h_mSubjet0AK8_1.Sumw2()
h_mSubjet0AK8_1.Scale( 1.0 / h_mSubjet0AK8_1.Integral() )
h_mSubjet0AK8_2.Sumw2()
h_mSubjet0AK8_2.Scale( 1.0 / h_mSubjet0AK8_2.Integral() )

c = TCanvas('c', 'c') 
h_mSubjet0AK8_1    .Draw("hist")
h_mSubjet0AK8_2    .Draw("same hist")


leg.Draw()

c.Print('plots7a.png', 'png')
c.Print('plots7a.pdf', 'pdf')



h_mSubjet1AK8_1   = f1.Get("h_mSubjet1AK8")
h_mSubjet1AK8_2   = f2.Get("h_mSubjet1AK8")

h_mSubjet1AK8_1    .SetLineColor(1)
h_mSubjet1AK8_2    .SetLineColor(2)

leg = TLegend(0.5, 0.5, 0.8, 0.8)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_mSubjet1AK8_1, "t#bar{t}", 'l')
leg.AddEntry( h_mSubjet1AK8_2, "RS KK Gluon", 'l')

h_mSubjet1AK8_1.Sumw2()
h_mSubjet1AK8_1.Scale( 1.0 / h_mSubjet1AK8_1.Integral() )
h_mSubjet1AK8_2.Sumw2()
h_mSubjet1AK8_2.Scale( 1.0 / h_mSubjet1AK8_2.Integral() )

c2 = TCanvas('c2', 'c2') 
h_mSubjet1AK8_1    .Draw("hist")
h_mSubjet1AK8_2    .Draw("same hist")


leg.Draw()

c2.Print('plots7b.png', 'png')
c2.Print('plots7b.pdf', 'pdf')
