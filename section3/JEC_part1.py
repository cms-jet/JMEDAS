import ROOT


f = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets.root")

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)


h_ptAK4   = f.Get("h_ptAK4")
h_ptAK4Gen   = f.Get("h_ptAK4Gen")

h_ptAK4Gen.SetLineStyle(2) 
h_ptAK4Gen.SetLineColor(2) 
c_pt = ROOT.TCanvas('c_pt', 'c_pt', 600, 400)
ROOT.gPad.SetLogy()
h_ptAK4.Draw()
h_ptAK4Gen.Draw("same")
h_ptAK4.GetXaxis().SetRangeUser(0, 600)
leg = ROOT.TLegend(0.6, 0.6, 0.8, 0.8)
leg.AddEntry(h_ptAK4, "RECO", "l")
leg.AddEntry(h_ptAK4Gen, "GEN", "l")
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.Draw("same")
ROOT.enableJSVis()
c_pt.Draw()
c_pt.Draw('jec_part1.pdf','pdf')
