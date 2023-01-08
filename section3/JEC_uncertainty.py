import ROOT

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)

f_corr = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets_corr.root")

h_ptAK4_corr   = f_corr.Get("h_ptAK4")
h_ptAK4_corrUp  = f_corr.Get("h_ptUpAK4")
h_ptAK4_corrDown  = f_corr.Get("h_ptDownAK4")

h_ptAK4_corr.SetLineWidth(2)
h_ptAK4_corrUp.SetLineStyle(2)
h_ptAK4_corrUp.SetLineColor(ROOT.kGreen+1) 
h_ptAK4_corrDown.SetLineStyle(2)
h_ptAK4_corrDown.SetLineColor(ROOT.kRed) 
h_ptAK4_corrUp.SetLineWidth(2)
h_ptAK4_corrDown.SetLineWidth(2)

c_JECunc = ROOT.TCanvas('c', 'c')

h_ptAK4_corr.Draw()
h_ptAK4_corrUp.Draw("same")
h_ptAK4_corrDown.Draw("same")
h_ptAK4_corr.GetXaxis().SetRangeUser(0, 400)

leg_corr = ROOT.TLegend(0.45, 0.55, 0.75, 0.8)
leg_corr.AddEntry(h_ptAK4_corr, "Nominal JEC", "l")
leg_corr.AddEntry(h_ptAK4_corrUp, "JEC +1 #sigma", "l")
leg_corr.AddEntry(h_ptAK4_corrDown, "JEC -1 #sigma", "l")
leg_corr.SetLineWidth(0)
leg_corr.SetFillColor(0)
leg_corr.SetShadowColor(0)
leg_corr.Draw()

c_JECunc.Draw()
c_JECunc.Print('JEC_uncertainty.pdf','pdf')


