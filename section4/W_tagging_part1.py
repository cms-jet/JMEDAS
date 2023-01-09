import ROOT

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)

f1 = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets.root")
f2 = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/QCD_Pt_300to470.root")

h_tau21AK8_1 = f1.Get("h_tau21AK8")
h_tau21AK8_2 = f2.Get("h_tau21AK8")

h_tau21AK8_1.SetLineColor(1)
h_tau21AK8_2.SetLineColor(2)

leg = ROOT.TLegend(0.12, 0.65, 0.32, 0.85)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry(h_tau21AK8_1, "t#bar{t}", 'l')
leg.AddEntry(h_tau21AK8_2, "QCD", 'l')

h_tau21AK8_1.Sumw2()
h_tau21AK8_1.Scale( 1.0 / h_tau21AK8_1.Integral() )
h_tau21AK8_2.Sumw2()
h_tau21AK8_2.Scale( 1.0 / h_tau21AK8_2.Integral() )

c_tau21 = ROOT.TCanvas('c_tau21', 'c_tau21') 
h_tau21AK8_1.GetYaxis().SetRangeUser(0., max([h_tau21AK8_1.GetMaximum(), h_tau21AK8_2.GetMaximum()]) * 1.05)
h_tau21AK8_1.Draw("hist")
h_tau21AK8_2.Draw("same hist")
leg.Draw()
c_tau21.Print("W_tagging_part1.pdf","pdf")


