from ROOT import *
from Analysis.JMEDAS.tdrstyle_mod14 import *

# Flag to turn PUPPI jets on or off
doPUPPI = False

# Set the ROOT style
gROOT.Macro("rootlogon.C")
setTDRStyle()

#Settings for each of the pads in the canvas
settings = {'response' : (0.0,2.0,0.0,0.12,"Response (p_{T}^{RECO}/p_{T}^{GEN})","a.u.",False),
			'pt'       : (30.0,200.0,0.0,0.26,"p_{T}^{RECO}","a.u.",True),
			'eta' 	   : (-5,5,0.0,0.07,"#eta","a.u.",False),
			'phi' 	   : (-3.14159,3.14159,0.0,0.04,"#phi","a.u.",False)
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
	if settings[s][6] :
		frames[f].GetXaxis().SetMoreLogLabels()
		frames[f].GetXaxis().SetNoExponent()
c = tdrCanvasMultipad("c",frames,2,11,2,2)

# Open the ROOT file with the ntuple
f = TFile("JECNtuple.root")

# Access and store the necessary trees
tAK4PF   = f.Get("AK4PF/t")
tAK4PFchs = f.Get("AK4PFCHS/t")
tAK4PUPPI   = f.Get("AK4PUPPI/t")

# Crease some histograms
hAK4PF_response    = TH1D("hAK4PF_response","hAK4PF_response",80,0,2)
hAK4PFchs_response = TH1D("hAK4PFchs_response","hAK4PFchs_response",80,0,2)
hAK4PUPPI_response = TH1D("hAK4PUPPI_response","hAK4PUPPI_response",80,0,2)
hAK4PF_pt   	   = TH1D("hAK4PF_pt","hAK4PF_pt",200,0,1000)
hAK4PFchs_pt 	   = TH1D("hAK4PFchs_pt","hAK4PFchs_pt",200,0,1000)
hAK4PUPPI_pt   	   = TH1D("hAK4PUPPI_pt","hAK4PUPPI_pt",200,0,1000)
hAK4PF_eta   	   = TH1D("hAK4PF_eta","hAK4PF_eta",50,-5,5)
hAK4PFchs_eta 	   = TH1D("hAK4PFchs_eta","hAK4PFchs_eta",50,-5,5)
hAK4PUPPI_eta  	   = TH1D("hAK4PUPPI_eta","hAK4PUPPI_eta",50,-5,5)
hAK4PF_phi   	   = TH1D("hAK4PF_phi","hAK4PF_phi",50,-3.14159,3.14159)
hAK4PFchs_phi 	   = TH1D("hAK4PFchs_phi","hAK4PFchs_phi",50,-3.14159,3.14159)
hAK4PUPPI_phi  	   = TH1D("hAK4PUPPI_phi","hAK4PUPPI_phi",50,-3.14159,3.14159)

# Fill the histograms
tAK4PF.Draw("jtpt/refpt>>hAK4PF_response","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")
tAK4PF.Draw("jtpt>>hAK4PF_pt","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")
tAK4PF.Draw("jteta>>hAK4PF_eta","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30","goff")
tAK4PF.Draw("jtphi>>hAK4PF_phi","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")
tAK4PFchs.Draw("jtpt/refpt>>hAK4PFchs_response","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")
tAK4PFchs.Draw("jtpt>>hAK4PFchs_pt","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")
tAK4PFchs.Draw("jteta>>hAK4PFchs_eta","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30","goff")
tAK4PFchs.Draw("jtphi>>hAK4PFchs_phi","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")
if doPUPPI:
	tAK4PUPPI.Draw("jtpt/refpt>>hAK4PUPPI_response","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")
	tAK4PUPPI.Draw("jtpt>>hAK4PUPPI_pt","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")
	tAK4PUPPI.Draw("jteta>>hAK4PUPPI_eta","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30","goff")
	tAK4PUPPI.Draw("jtphi>>hAK4PUPPI_phi","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>30 && jteta<1.3","goff")

#Normalize the histograms
hAK4PF_response.Scale(1.0/hAK4PF_response.Integral())
hAK4PF_pt.Scale(1.0/hAK4PF_pt.Integral())
hAK4PF_eta.Scale(1.0/hAK4PF_eta.Integral())
hAK4PF_phi.Scale(1.0/hAK4PF_phi.Integral())
hAK4PFchs_response.Scale(1.0/hAK4PFchs_response.Integral())
hAK4PFchs_pt.Scale(1.0/hAK4PFchs_pt.Integral())
hAK4PFchs_eta.Scale(1.0/hAK4PFchs_eta.Integral())
hAK4PFchs_phi.Scale(1.0/hAK4PFchs_phi.Integral())
if doPUPPI:
	hAK4PUPPI_response.Scale(1.0/hAK4PUPPI_response.Integral())
	hAK4PUPPI_pt.Scale(1.0/hAK4PUPPI_pt.Integral())
	hAK4PUPPI_eta.Scale(1.0/hAK4PUPPI_eta.Integral())
	hAK4PUPPI_phi.Scale(1.0/hAK4PUPPI_phi.Integral())

#Draw the histograms
c.cd(1)
tdrDraw(hAK4PF_phi,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hAK4PFchs_phi,"HIST",kNone,kRed,kSolid,-1,0,0)
if doPUPPI :
	tdrDraw(hAK4PUPPI_phi,"HIST",kNone,kGreen,kSolid,-1,0,0)
c.cd(2)
tdrDraw(hAK4PF_eta,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hAK4PFchs_eta,"HIST",kNone,kRed,kSolid,-1,0,0)
if doPUPPI :
	tdrDraw(hAK4PUPPI_eta,"HIST",kNone,kGreen,kSolid,-1,0,0)
c.cd(3)
tdrDraw(hAK4PF_response,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hAK4PFchs_response,"HIST",kNone,kRed,kSolid,-1,0,0)
if doPUPPI :
	tdrDraw(hAK4PUPPI_response,"HIST",kNone,kGreen,kSolid,-1,0,0)
c.cd(4)
gPad.SetLogx()
tdrDraw(hAK4PF_pt,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hAK4PFchs_pt,"HIST",kNone,kRed,kSolid,-1,0,0)
if doPUPPI :
	tdrDraw(hAK4PUPPI_pt,"HIST",kNone,kGreen,kSolid,-1,0,0)

# Add entries to the legend and draw it
l_response = tdrLeg(0.65,0.65,0.9,0.9)
l_pt  	   = tdrLeg(0.65,0.65,0.9,0.9)
l_eta 	   = tdrLeg(0.65,0.65,0.9,0.9)
l_phi 	   = tdrLeg(0.65,0.65,0.9,0.9)
l_response.AddEntry(hAK4PF_response,"AK4PF","l")
l_response.AddEntry(hAK4PFchs_response,"AK4PFchs","l")
l_pt.AddEntry(hAK4PF_pt,"AK4PF","l")
l_pt.AddEntry(hAK4PFchs_pt,"AK4PFchs","l")
l_eta.AddEntry(hAK4PF_eta,"AK4PF","l")
l_eta.AddEntry(hAK4PFchs_eta,"AK4PFchs","l")
l_phi.AddEntry(hAK4PF_phi,"AK4PF","l")
l_phi.AddEntry(hAK4PFchs_phi,"AK4PFchs","l")
if doPUPPI :
	l_response.AddEntry(hAK4PUPPI_response,"AK4PUPPI","l")
	l_pt.AddEntry(hAK4PUPPI_pt,"AK4PUPPI","l")
	l_eta.AddEntry(hAK4PUPPI_eta,"AK4PUPPI","l")
	l_phi.AddEntry(hAK4PUPPI_phi,"AK4PUPPI","l")
c.cd(1)
l_phi.Draw("same")
c.cd(2)
l_eta.Draw("same")
c.cd(3)
l_response.Draw("same")
c.cd(4)
l_pt.Draw("same")

# Save the canvases
c.Print('plots_jec_hats_1.png', 'png')
c.Print('plots_jec_hats_1.pdf', 'pdf')

