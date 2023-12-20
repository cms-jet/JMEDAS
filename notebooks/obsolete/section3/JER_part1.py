import ROOT

################################################
# Plotting for Exercise: Jet Energy Resolution #
################################################

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)


f = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets_corr_smear.root")
h_ptAK4   = f.Get("h_ptAK4")
h_ptAK4Up  = f.Get("h_ptUpAK4")
h_ptAK4Down  = f.Get("h_ptDownAK4")
h_ptAK4Up.SetLineStyle(2)
h_ptAK4Up.SetLineColor(ROOT.kGreen+1) 
h_ptAK4Down.SetLineStyle(2)
h_ptAK4Down.SetLineColor(ROOT.kRed) 
h_ptAK4Up.SetLineWidth(2)
h_ptAK4Down.SetLineWidth(2)
h_ptAK4.SetLineWidth(2)

c = ROOT.TCanvas('c', 'c')

h_ptAK4.Draw()
h_ptAK4Up.Draw("same")
h_ptAK4Down.Draw("same")
h_ptAK4.GetXaxis().SetRangeUser(0, 400)

leg = ROOT.TLegend(0.45, 0.55, 0.75, 0.8)
leg.AddEntry(h_ptAK4, "Nominal JER", "l")
leg.AddEntry(h_ptAK4Up, "JER +1 #sigma", "l")
leg.AddEntry(h_ptAK4Down, "JER -1 #sigma", "l")
leg.SetLineWidth(0)
leg.SetFillColor(0)
leg.SetShadowColor(0)
leg.Draw()

c.Draw()
c.Print('JER_part1.pdf','pdf')
