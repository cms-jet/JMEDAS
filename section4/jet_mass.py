import ROOT

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)

f1 = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/rsgluon_ttbar_3TeV.root")
f2 = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/QCD_Pt_300to470.root")

h_massAK8_1 = f1.Get("h_mAK8")
h_massAK8_2 = f2.Get("h_mAK8")
h_massAK8_3 = f1.Get("h_mSDpuppiAK8")
h_massAK8_4 = f2.Get("h_mSDpuppiAK8")

h_massAK8_1.SetLineColor(1)
h_massAK8_2.SetLineColor(2)
h_massAK8_3.SetLineColor(3)
h_massAK8_4.SetLineColor(4)

leg = ROOT.TLegend(0.5, 0.5, 0.7, 0.8)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_massAK8_1, "", "")
leg.AddEntry( h_massAK8_1, "RS KK Gluon CHS", 'l')
leg.AddEntry( h_massAK8_2, "QCD CHS", 'l')
leg.AddEntry( h_massAK8_3, "RS KK Gluon SD+PUPPI", 'l')
leg.AddEntry( h_massAK8_4, "QCD SD+PUPPI", 'l')

h_massAK8_1.Sumw2()
h_massAK8_1.Scale( 1.0 / h_massAK8_1.Integral() )
h_massAK8_2.Sumw2()
h_massAK8_2.Scale( 1.0 / h_massAK8_2.Integral() )
h_massAK8_3.Sumw2()
h_massAK8_3.Scale( 1.0 / h_massAK8_3.Integral() )
h_massAK8_4.Sumw2()
h_massAK8_4.Scale( 1.0 / h_massAK8_4.Integral() )

c_puppimass = ROOT.TCanvas('c_puppimass', 'c_puppimass') 
h_massAK8_1.GetXaxis().SetRangeUser(0., 400.)
h_massAK8_1.GetYaxis().SetRangeUser(0., max([h_massAK8_1.GetMaximum(), h_massAK8_2.GetMaximum(), h_massAK8_3.GetMaximum(), h_massAK8_4.GetMaximum()]) * 1.05)
h_massAK8_1.Draw("hist")
h_massAK8_2.Draw("same hist")
h_massAK8_3.Draw("same hist")
h_massAK8_4.Draw("same hist")


leg.Draw()
c_puppimass.Print("jet_mass.pdf","pdf")
