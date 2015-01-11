from ROOT import *
from Analysis.JMEDAS.tdrstyle_mod14 import *

# Set the ROOT style
gROOT.Macro("rootlogon.C")
setTDRStyle()

#Settings for each of the pads in the canvas
settings = {'X'         : (0.0,40.0,0.0,1500,"X","Number of Jets"),
			'RhoVsNpv'  : (0.0,40.0,0.0,40.0,"N_{PV}","#rho"),
			'NpvVsTnpu' : (0.0,40.0,0.0,40.0,"#mu","N_{PV}"),
			'RhoVsTnpu'	: (0.0,40.0,0.0,40.0,"#mu","#rho")
			}

# Create and draw the canvas
frames = []
for f, s in enumerate(settings) :
	frame = TH1D()
	frames.append(frame)
	frames[f].GetXaxis().SetLimits(settings[s][0],settings[s][1])
	frames[f].GetYaxis().SetRangeUser(settings[s][2],settings[s][3])
	frames[f].GetXaxis().SetTitle(settings[s][4])
	frames[f].GetYaxis().SetTitle(settings[s][5])
c = tdrCanvasMultipad("c",frames,2,0,2,2)

# Open the ROOT file with the ntuple
f = TFile("pileupNtuple.root")

# Access and store the necessary trees
tAK4PFchs   = f.Get("AK4PFchs/t")
tAK4PFchsl1 = f.Get("AK4PFchsl1/t")
tAK4PUPPI   = f.Get("AK4PUPPI/t")

# Crease some histograms
hAK4PFchs_npv   	 = TH1D("hAK4PFchs_npv","hAK4PFchs_npv",60,0,60)
hAK4PFchs_rho 		 = TH1D("hAK4PFchs_rho","hAK4PFchs_rho",60,0,60)
hAK4PFCHS_npu   	 = TH1D("hAK4PFchs_npu","hAK4PFchs_npu",60,0,60)
hAK4PFchs_tnpu  	 = TH1D("hAK4PFchs_tnpu","hAK4PFchs_tnpu",60,0,60)
hAK4PFchs_rhovsnpv   = TH2F("hAK4PFchs_rhovsnpv","hAK4PFchs_rhovsnpv",60,0,600,60,0,60)
hAK4PFchs_npvvsnpu	 = TH2F("hAK4PFchs_npvvsnpu","hAK4PFchs_npvvsnpu",60,0,60,60,0,60)
hAK4PFchs_rhovsnpu   = TH2F("hAK4PFchs_rhovsnpu","hAK4PFchs_rhovsnpu",60,0,60,60,0,60)

# Fill the histograms
tAK4PFchs.Draw("npv>>hAK4PFchs_npv","","goff")
tAK4PFchs.Draw("rho>>hAK4PFchs_rho","","goff")
tAK4PFchs.Draw("npus[12]>>hAK4PFchs_npu","","goff")
tAK4PFchs.Draw("tnpus[12]>>hAK4PFchs_tnpu","","goff")
c.cd(1)
tAK4PFchs.Draw("rho:npv","","colz")
c.cd(4)
tAK4PFchs.Draw("npv:npus[12]","","colz")
c.cd(3)
tAK4PFchs.Draw("rho:npus[12]","","colz")

#Draw the histograms
c.cd(2)
tdrDraw(hAK4PFchs_npv,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hAK4PFchs_rho,"HIST",kNone,kRed,kSolid,-1,0,0)
tdrDraw(hAK4PFchs_npu,"HIST",kNone,kGreen,kSolid,-1,0,0)
tdrDraw(hAK4PFchs_tnpu,"HIST",kNone,kBlue,kSolid,-1,0,0)

# Add entries to the legend and draw it
c.cd(2)
l_X = tdrLeg(0.8,0.65,0.9,0.9)
l_X.AddEntry(hAK4PFchs_npv,"N_{PV}","l")
l_X.AddEntry(hAK4PFchs_rho,"#rho","l")
l_X.AddEntry(hAK4PFchs_npu,"N_{PU}","l")
l_X.AddEntry(hAK4PFchs_tnpu,"#mu","l")
l_X.Draw("same")

# Save the canvases
c.Print('plots_pileup_1.png', 'png')
c.Print('plots_pileup_1.pdf', 'pdf')

