from ROOT import *

gROOT.Macro("rootlogon.C")

f = TFile("ttjets_short.root")

h_mAK8   = f.Get("h_mAK8")
h_mfilteredAK8   = f.Get("h_mfilteredAK8")
h_mprunedAK8   = f.Get("h_mprunedAK8")
h_mtrimmedAK8   = f.Get("h_mtrimmedAK8")

h_mfilteredAK8   .SetLineColor(2) 
h_mprunedAK8     .SetLineColor(4) 
h_mtrimmedAK8    .SetLineColor(6) 

h_mfilteredAK8   .SetLineStyle(2) 
h_mprunedAK8     .SetLineStyle(3) 
h_mtrimmedAK8    .SetLineStyle(4) 


leg = TLegend(0.5, 0.5, 0.8, 0.8)
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.AddEntry( h_mAK8, "Ungroomed", 'l')
leg.AddEntry( h_mfilteredAK8, "Filtered", 'l')
leg.AddEntry( h_mtrimmedAK8, "Trimmed", 'l')
leg.AddEntry( h_mprunedAK8, "Pruned", 'l')

c = TCanvas('c', 'c')
h_mAK8.Draw()
h_mfilteredAK8   .Draw("same") 
h_mprunedAK8     .Draw("same") 
h_mtrimmedAK8    .Draw("same")
h_mAK8.GetXaxis().SetRangeUser(0, 200)
h_mAK8.SetMaximum( 200 )

leg.Draw()

c.Print('plots4.png', 'png')
c.Print('plots4.pdf', 'pdf')
