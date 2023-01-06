import ROOT

#############################
# Plotting for Exercise: 2  #
#############################

f = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets.root")

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
c_pt.Draw('plot6.pdf','pdf')

################################################
# Plotting for Exercise: Before and after JECs #
################################################

f_corr = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets_corr.root")

h_ptAK4_corr = f_corr.Get("h_ptAK4")
h_ptAK4Gen_corr = f_corr.Get("h_ptAK4Gen")

h_ptAK4Gen_corr.SetLineStyle(2) 
h_ptAK4Gen_corr.SetLineColor(2) 
c_corr = ROOT.TCanvas('c_corr', 'c', 800, 400)
c_corr.Divide(2,1)
c_corr.cd(1)
ROOT.gPad.SetLogy()
h_ptAK4_corr.Draw()
h_ptAK4_corr.SetTitle("AK4 Jet p_{T} (corrected)")
h_ptAK4Gen_corr.Draw("same")
h_ptAK4_corr.GetXaxis().SetRangeUser(0, 1000)
leg_corr = ROOT.TLegend(0.6, 0.6, 0.8, 0.8)
leg_corr.AddEntry(h_ptAK4, "RECO", "l")
leg_corr.AddEntry(h_ptAK4Gen, "GEN", "l")
leg_corr.SetFillColor(0)
leg_corr.SetLineColor(0)
leg_corr.Draw("same")

c_corr.cd(2)
ROOT.gPad.SetLogy()
h_ptAK4.Draw()
h_ptAK4.SetTitle("AK4 Jet p_{T} (uncorrected)")
h_ptAK4Gen.Draw("same")
h_ptAK4.GetXaxis().SetRangeUser(0, 1000)
leg = ROOT.TLegend(0.6, 0.6, 0.8, 0.8)
leg.AddEntry(h_ptAK4, "RECO", "l")
leg.AddEntry(h_ptAK4Gen, "GEN", "l")
leg.SetFillColor(0)
leg.SetLineColor(0)
leg.Draw("same")

c_corr.Draw()
c_corr.Print('plot7.pdf','pdf')

c_compare = ROOT.TCanvas("c_compare", "c_compare", 400, 400)
c_compare.SetLogy()
h_ptAK4_norm = h_ptAK4.Clone()
h_ptAK4_norm.Scale(1. / h_ptAK4_norm.Integral())
h_ptAK4_norm.SetLineStyle(2)
h_ptAK4_norm.SetLineColor(ROOT.kRed)
h_ptAK4_norm.SetTitle("Corrected vs. Uncorrected")
h_ptAK4_norm.Draw("hist")

h_ptAK4_corr_norm = h_ptAK4_corr.Clone()
h_ptAK4_corr_norm.Scale(1. / h_ptAK4_corr_norm.Integral())
h_ptAK4_corr_norm.SetLineStyle(1)
h_ptAK4_corr_norm.SetLineColor(ROOT.kBlack)
h_ptAK4_corr_norm.Draw("hist same")
l_compare = ROOT.TLegend(0.55, 0.5, 0.88, 0.8)
l_compare.SetFillColor(0)
l_compare.SetBorderSize(0)
l_compare.AddEntry(h_ptAK4_norm, "Uncorrected AK4PFJets", "l")
l_compare.AddEntry(h_ptAK4_corr_norm, "Corrected AK4PFJets", "l")
l_compare.Draw()
c_compare.Draw()
c_compare.Print('plot8.pdf','pdf')

#############################################
# Plotting for Exercise: JEC Uncertainties  #
#############################################
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
c_JECunc.Print('plot9.pdf','pdf')

