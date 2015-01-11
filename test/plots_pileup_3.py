from ROOT import *
from Analysis.JMEDAS.tdrstyle_mod14 import *

# Set the ROOT style
gROOT.Macro("rootlogon.C")
setTDRStyle()

#Settings for each of the pads in the canvas
settings = {'isolation': (0.0,1.6,1.0,4000,"Isolation","Number of Muons",False), #1
			'pt'       : (10.0,100.0,0.0,200,"p_{T}^{RECO}","Number of Muons",True), #4
			'eta' 	   : (-2.4,2.4,0.0,300,"#eta","Number of Muons",False), #3
			'phi' 	   : (-3.14159,3.14159,0.0,250,"#phi","Number of Muons",False) #2
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
f = TFile("pileupNtuple.root")

# Access and store the necessary trees
tAK4PFchs   = f.Get("AK4PFchs/t")

# Crease some histograms
hmuon_isolationSTAND = TH1D("hmuon_isolationSTAND","hmuon_isolationSTAND",1000,-10,10)
hmuon_isolationPUPPI = TH1D("hmuon_isolationPUPPI","hmuon_isolationPUPPI",1000,-10,10)
hmuon_pt   			 = TH1D("hmuon_pt","hmuon_pt",1000,0,1000)
hmuon_eta   		 = TH1D("hmuon_eta","hmuon_eta",50,-5,5)
hmuon_phi   		 = TH1D("hmuon_phi","hmuon_phi",30,-3.14159,3.14159)

# Fill the histograms
tAK4PFchs.Draw("muIsoSTAND>>hmuon_isolationSTAND","","goff")
tAK4PFchs.Draw("muIsoPUPPI>>hmuon_isolationPUPPI","","goff")
tAK4PFchs.Draw("mupt>>hmuon_pt","","goff")
tAK4PFchs.Draw("mueta>>hmuon_eta","","goff")
tAK4PFchs.Draw("muphi>>hmuon_phi","","goff")

#Draw the histograms
c.cd(1)
gPad.SetLogy()
tdrDraw(hmuon_isolationSTAND,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hmuon_isolationPUPPI,"HIST",kNone,kRed,kSolid,-1,0,0)
c.cd(2)
tdrDraw(hmuon_phi,"HIST",kNone,kBlack,kSolid,-1,0,0)
c.cd(3)
tdrDraw(hmuon_eta,"HIST",kNone,kBlack,kSolid,-1,0,0)
c.cd(4)
tdrDraw(hmuon_pt,"HIST",kNone,kBlack,kSolid,-1,0,0)

# Add entries to the legend and draw it
c.cd(1)
l_isolation = tdrLeg(0.65,0.65,0.9,0.9)
l_isolation.AddEntry(hmuon_isolationSTAND,"#Delta#Beta","l")
l_isolation.AddEntry(hmuon_isolationPUPPI,"iPUPPI","l")
l_isolation.Draw("same")

# Save the canvases
c.Print('plots_pileup_3.png', 'png')
c.Print('plots_pileup_3.pdf', 'pdf')

