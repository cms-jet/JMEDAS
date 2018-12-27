from ROOT import *
from collections import OrderedDict
from Analysis.JMEDAS.tdrstyle_mod14 import *

# Set the ROOT style
gROOT.Macro("rootlogon.C")
setTDRStyle()

#Settings for each of the pads in the canvas
settingsTMP = {'npv'  : (1,0.0,50.0,0.0,1000.0,"N_{PV}","events"),
	       'npv'  : (2,0.0,50.0,0.0,1000.0,"N_{PV}","events")}
settings = OrderedDict(sorted(settingsTMP.items(), key=lambda x:x[1], reverse=False))

# Create and draw the canvas
frames = []
for f, s in enumerate(settings) :
	frame = TH1D()
	frames.append(frame)
	frames[f].GetXaxis().SetLimits(settings[s][1],settings[s][2])
	frames[f].GetYaxis().SetRangeUser(settings[s][3],settings[s][4])
	frames[f].GetXaxis().SetTitle(settings[s][5])
	frames[f].GetYaxis().SetTitle(settings[s][6])
c = tdrCanvasMultipad("c",frames,14,10,1,2)

# Open the ROOT file with the ntuple
f_data = TFile("JECNtuple_data.root","READ")
f_mc = TFile("JECNtuple_mc.root","READ")

# Access and store the necessary trees
tAK4PFchs_data   = f_mc.Get("AK4PFCHSL1L2L3/t")
tAK4PFchs_mc   = f_mc.Get("AK4PFCHSL1L2L3/t")

# Crease some histograms
hAK4PFchs_data = TH1D("hAK4PFchs_data","hAK4PFchs_data",50,0,50)
hAK4PFchs_mc_before = TH1D("hAK4PFchs_mc_before","hAK4PFchs_mc_before",50,0,50)
hAK4PFchs_mc_after  = TH1D("hAK4PFchs_mc_after","hAK4PFchs_mc_after",50,0,50)

# Fill the histograms
for event in tAK4PFchs_data:
	hAK4PFchs_data.Fill(event.npv)

for event in tAK4PFchs_mc:
	hAK4PFchs_mc_before.Fill(event.npv)
	hAK4PFchs_mc_after.Fill(event.npv,weight)

#Scale the histograms to be the same height
hAK4PFchs_data.Scale(1.0/hAK4PFchs_data.Integral())
hAK4PFchs_mc_before.Scale(1.0/hAK4PFchs_mc_before.Integral())
hAK4PFchs_mc_after.Scale(1.0/hAK4PFchs_mc_after.Integral())

#Draw the histograms
c.cd(1)
tdrDraw(hAK4PFchs_mc_before,"HIST",kNone,kNone,kSolid,kAzure,kSolid,kAzure)
tdrDraw(hAK4PFchs_data,"ep",kFullCircle,kBlack)
l_before = tdrLeg(0.8,0.65,0.9,0.9)
l_before.AddEntry(hAK4PFchs_data,"Data","ep")
l_before.AddEntry(hAK4PFchs_mc_before,"MC","l")
l_before.Draw("same")

c.cd(2)
tdrDraw(hAK4PFchs_mc_after,"HIST",kNone,kNone,kSolid,kAzure,kSolid,kAzure)
tdrDraw(hAK4PFchs_data,"ep",kFullCircle,kBlack)
l_after = tdrLeg(0.8,0.65,0.9,0.9)
l_after.AddEntry(hAK4PFchs_data,"Data","ep")
l_after.AddEntry(hAK4PFchs_mc_after,"MC","l")
l_after.Draw("same")

c.Update()
c.Draw()

# Save the Canvas
c.SaveAs('plots_pileup_1.png')
