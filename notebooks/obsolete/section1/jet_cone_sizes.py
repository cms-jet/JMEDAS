import ROOT
import math

ROOT.gROOT.SetBatch(True)


###################################################################
# Plotting for Exercise: Comparing jet areas between AK4 and AK8  #
###################################################################

f = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/qcd_470to600.root")

h_areaAK4 = f.Get("h_areaAK4")
h_areaAK8 = f.Get("h_areaAK8")
h_areaAK8.SetLineStyle(4)
h_areaAK8.SetLineColor(4)

h_areaAK4.Scale( 1.0 / h_areaAK4.Integral() )
h_areaAK8.Scale( 1.0 / h_areaAK8.Integral() )

c_area = ROOT.TCanvas('c_area', 'c_area')
frame = h_areaAK4.Clone()
frame.Reset()
frame.SetTitle("Jet Areas")
frame.SetMaximum(h_areaAK4.GetMaximum() * 1.2)
frame.Draw('axis')
h_areaAK4.Draw('hist same')
h_areaAK8.Draw("hist same")

l = ROOT.TLegend(0.6, 0.7, 0.8, 0.8)
l.SetFillColor(0)
l.SetBorderSize(0)
l.AddEntry(h_areaAK4, "AK4", "l")
l.AddEntry(h_areaAK8, "AK8", "l")
l.Draw()

c_area.Draw()
c_area.Print('jet_cone_sizes.pdf','pdf')
