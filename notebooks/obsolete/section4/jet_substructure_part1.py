import ROOT

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)

ROOT.gStyle.SetOptStat(0)
ROOT.gStyle.SetOptTitle(0)
f = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/rsgluon_ttbar_3000GeV.root")

h_mAK8   = f.Get("h_mAK8")
h_msoftdropAK8 = f.Get("h_msoftdropAK8")
h_mprunedAK8   = f.Get("h_mprunedAK8")
h_mpuppiAK8 = f.Get("h_mpuppiAK8")
h_mSDpuppiAK8 = f.Get("h_mSDpuppiAK8")

h_mAK8.SetLineColor(ROOT.kBlack)
h_mAK8.SetLineWidth(1)
h_msoftdropAK8.SetLineColor(ROOT.kRed-4)
h_msoftdropAK8.SetLineStyle(3)
h_msoftdropAK8.SetLineWidth(1)
h_mprunedAK8.SetLineColor(ROOT.kMagenta-4) 
h_mprunedAK8.SetLineStyle(4) 
h_mpuppiAK8.SetLineColor(ROOT.kGreen)
h_mpuppiAK8.SetLineStyle(3)
h_mpuppiAK8.SetLineWidth(1)
h_mSDpuppiAK8.SetLineColor(ROOT.kAzure)
h_mSDpuppiAK8.SetLineStyle(2)
h_mSDpuppiAK8.SetLineWidth(3)

legend = ROOT.TLegend(0.6, 0.6, 0.88, 0.88)
legend.SetFillColor(0)
legend.SetBorderSize(0)
legend.AddEntry(h_mAK8, "Ungroomed", 'l')
legend.AddEntry(h_msoftdropAK8, "Soft Drop", 'l')
legend.AddEntry(h_mprunedAK8, "Pruned", 'l')
legend.AddEntry(h_mpuppiAK8, "PUPPI", 'l')
legend.AddEntry(h_mSDpuppiAK8, "PUPPI+SD", 'l')

c_mass = ROOT.TCanvas('c_mass', 'c_mass', 800, 600)
#h_mprunedAK8.SetMaximum(500)
h_mprunedAK8.GetXaxis().SetRangeUser(0., 400.)
h_mprunedAK8.DrawNormalized()
#h_mprunedAK8.GetXaxis().SetRangeUser(0, 400)
#h_mprunedAK8.GetYaxis().SetRangeUser(0, 500)
h_msoftdropAK8.DrawNormalized("same") 
h_mAK8.DrawNormalized("same") 
h_mpuppiAK8.DrawNormalized("same")
h_mSDpuppiAK8.DrawNormalized("same")
h_mprunedAK8.DrawNormalized("axis same")
#h_mprunedAK8.SetMaximum(h_msoftdropAK8.GetMaximum()*1.2)

legend.Draw()
c_mass.Print("jet_substructure_part1.pdf","pdf")