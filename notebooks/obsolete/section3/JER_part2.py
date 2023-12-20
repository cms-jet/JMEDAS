import ROOT

################################################
# Plotting for Exercise: Jet Energy Resolution #
################################################

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)

###################################################################
# Plotting for Exercise: Comparing jet areas between AK4 and AK8  #
###################################################################
f_nominal = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/rsgluon_qq_3000GeV.root")
h_nominal = f_nominal.Get("h_dijet_mass")
h_nominal.SetName("h_dijet_mass_nominal")
h_nominal.SetDirectory(0)
h_gen = f_nominal.Get("h_dijet_genmass")
h_gen.SetDirectory(0)
f_nominal.Close()

f_corr = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/rsgluon_qq_3000GeV_corr.root")
h_corr = f_corr.Get("h_dijet_mass")
h_corr.SetName("h_dijet_mass_corr")
h_corr.SetDirectory(0)
f_corr.Close()

f_smear = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/rsgluon_qq_3000GeV_smear.root")
h_smear = f_smear.Get("h_dijet_mass")
h_smear.SetName("h_dijet_mass_smear")
h_smear.SetDirectory(0)
f_smear.Close()

f_corr_smear = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/rsgluon_qq_3000GeV_corr_smear.root")
h_corr_smear = f_corr_smear.Get("h_dijet_mass")
h_corr_smear.SetName("h_dijet_mass_corr_smear")
h_corr_smear.SetDirectory(0)
f_corr_smear.Close()

rebin = 4

c_dijet = ROOT.TCanvas("c_dijet", "Dijet mass (#Delta#eta<1.2)", 800, 600)
h_gen.SetLineColor(ROOT.kBlack)
h_gen.Rebin(rebin)
h_gen.Draw("hist")

h_nominal.SetLineColor(ROOT.kRed-1)
h_nominal.SetLineStyle(3)
h_nominal.Rebin(rebin)
h_nominal.Draw("hist same")

h_corr.SetLineColor(ROOT.kBlue+2)
h_corr.SetLineStyle(4)
h_corr.Rebin(rebin)
h_corr.Draw("hist same")

h_smear.SetLineColor(ROOT.kGreen-1)
h_smear.SetLineStyle(5)
h_smear.Rebin(rebin)
h_smear.Draw("hist same")

h_corr_smear.SetLineColor(ROOT.kMagenta)
h_corr_smear.SetLineStyle(2)
h_corr_smear.Rebin(rebin)
h_corr_smear.Draw("hist same")

l_dijet = ROOT.TLegend(0.22, 0.5, 0.4, 0.8)
l_dijet.SetFillColor(0)
l_dijet.SetFillStyle(0)
l_dijet.SetBorderSize(0)
l_dijet.AddEntry(h_gen, "Gen jets", "l")
l_dijet.AddEntry(h_nominal, "Uncorrected", "pl")
l_dijet.AddEntry(h_corr, "Corrected", "pl")
l_dijet.AddEntry(h_smear, "Smeared", "pl")
l_dijet.AddEntry(h_corr_smear, "Corr+smear", "pl")
l_dijet.Draw()

c_dijet.Draw()
c_dijet.Print('JER_part2.pdf','pdf')

