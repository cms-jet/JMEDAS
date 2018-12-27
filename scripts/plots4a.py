from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("qcd_highPt.root")

h_mAK8   = f.Get("h_mAK8")
h_msoftdropAK8   = f.Get("h_msoftdropAK8")
h_mfilteredAK8   = f.Get("h_mfilteredAK8")
h_mprunedAK8   = f.Get("h_mprunedAK8")
h_mtrimmedAK8   = f.Get("h_mtrimmedAK8")
h_mpuppiAK8 = f.Get("h_mpuppiAK8")
h_mSDpuppiAK8 = f.Get("h_mSDpuppiAK8")

h_msoftdropAK8   .SetLineColor(2)
h_mprunedAK8     .SetLineColor(4) 

h_msoftdropAK8   .SetLineColor(2)
h_mprunedAK8     .SetLineStyle(3) 

h_mpuppiAK8.SetLineColor(kGreen+3)
h_mSDpuppiAK8.SetLineColor(kOrange+3)


leg = TLegend(0.35, 0.68, 0.65, 0.99)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_mAK8, "Ungroomed", 'l')
leg.AddEntry( h_msoftdropAK8, "Soft Drop", 'l')
leg.AddEntry( h_mprunedAK8, "Pruned", 'l')
leg.AddEntry( h_mpuppiAK8, "PUPPI", 'l')
leg.AddEntry( h_mSDpuppiAK8, "PUPPI+SD", 'l')


c = TCanvas('c', 'c')
h_mprunedAK8.Draw()
h_mprunedAK8.GetXaxis().SetRangeUser(0, 250)
h_msoftdropAK8   .Draw("same") 
h_mAK8     .Draw("same") 
h_mpuppiAK8.Draw("same")
h_mSDpuppiAK8.Draw("same")
h_mprunedAK8.SetMaximum( h_msoftdropAK8.GetMaximum()*1.2 )

leg.Draw()

c.Print('plots4a.png', 'png')
c.Print('plots4a.pdf', 'pdf')
