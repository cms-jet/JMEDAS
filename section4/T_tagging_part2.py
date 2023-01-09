import ROOT

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)

f1 = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/rsgluon_ttbar_3TeV.root")
f2 = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/QCD_Pt_300to470.root")

h_ak8_N3_beta1_1 = f1.Get("h_ak8_N3_beta1")
h_ak8_N3_beta1_2 = f2.Get("h_ak8_N3_beta1")

h_ak8_N3_beta1_1.SetLineColor(1)
h_ak8_N3_beta1_2.SetLineColor(2)

leg = ROOT.TLegend(0.15, 0.5, 0.35, 0.7)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_ak8_N3_beta1_1, "RS KK Gluon", 'l')
leg.AddEntry( h_ak8_N3_beta1_2, "QCD", 'l')

h_ak8_N3_beta1_1.Sumw2()
h_ak8_N3_beta1_1.Scale(1.0 / h_ak8_N3_beta1_1.Integral())
h_ak8_N3_beta1_2.Sumw2()
h_ak8_N3_beta1_2.Scale(1.0 / h_ak8_N3_beta1_2.Integral())

c_n3 = ROOT.TCanvas('c_n3', 'c_n3') 
h_ak8_N3_beta1_1.GetYaxis().SetRangeUser(0., max([h_ak8_N3_beta1_1.GetMaximum(), h_ak8_N3_beta1_2.GetMaximum()]) * 1.05)
h_ak8_N3_beta1_1.Draw("hist")
h_ak8_N3_beta1_2.Draw("same hist")
leg.Draw()
c_n3.Print("T_tagging_part2.pdf","pdf")
