from ROOT import *
from collections import OrderedDict
from Analysis.JMEDAS.tdrstyle_mod14 import *

# Set the ROOT style
gROOT.Macro("rootlogon.C")
setTDRStyle()

#Settings for each of the pads in the canvas
settingsTMP = {'mupt'        : (1,10.0,100.0,0.0,0.025,"p_{T}^{#mu}","a.u.",True),
			   'muisolation' : (2,0.0,1.6,1.0,1,"#mu Isolation","a.u.",False),
			   'METpt' 	  	 : (3,10.0,200,0.0,0.045,"MET","a.u.",False),
			   'METphi'		 : (4,-3.14159,3.14159,0.0,0.065,"MET #phi","a.u.",False)
			   }
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
	if settings[s][7] :
		frames[f].GetXaxis().SetMoreLogLabels()
		frames[f].GetXaxis().SetNoExponent()
c = tdrCanvasMultipad("c",frames,14,11,2,2)

# Open the ROOT file with the ntuple
f = TFile("pileupNtuple.root")

# Access and store the necessary trees
tAK4PFPuppi   = f.Get("AK4PFPuppiL1L2L3/t")

# Crease some histograms
hmuon_pt   			  = TH1D("hmuon_pt","hmuon_pt",1000,0,1000)
hmuon_PuppiCombined   = TH1D("hmuon_PuppiCombined","hmuon_PuppiCombined",1000,-10,10)
hmuon_PuppiWithLep    = TH1D("hmuon_PuppiWithLep","hmuon_PuppiWithLep",1000,-10,10)
hmuon_PuppiWithoutLep = TH1D("hmuon_PuppiWithoutLep","hmuon_PuppiWithoutLep",1000,-10,10)
hmet_pt   			  = TH1D("hmet_pt","hmet_pt",1000,0,1000)
hmetNoHF_pt  		  = TH1D("hmetNoHF_pt","hmetNoHF_pt",1000,0,1000)
hmetPUPPI_pt 		  = TH1D("hmetPUPPI_pt","hmetPUPPI_pt",1000,0,1000)
hmet_phi   			  = TH1D("hmet_phi","hmet_phi",30,-3.14159,3.14159)
hmetNoHF_phi   		  = TH1D("hmetNoHF_phi","hmetNoHF_phi",30,-3.14159,3.14159)
hmetPUPPI_phi   	  = TH1D("hmetPUPPI_phi","hmetPUPPI_phi",30,-3.14159,3.14159)

#Fill the histograms
tAK4PFPuppi.Draw("mupt>>hmuon_pt","","goff")
tAK4PFPuppi.Draw("muIso_PuppiCombined>>hmuon_PuppiCombined","","goff")
tAK4PFPuppi.Draw("muIso_PuppiWithLep>>hmuon_PuppiWithLep","","goff")
tAK4PFPuppi.Draw("muIso_PuppiWithoutLep>>hmuon_PuppiWithoutLep","","goff")
tAK4PFPuppi.Draw("metpt>>hmet_pt","","goff")
tAK4PFPuppi.Draw("metNoHFpt>>hmetNoHF_pt","","goff")
tAK4PFPuppi.Draw("metPUPPIpt>>hmetPUPPI_pt","","goff")
tAK4PFPuppi.Draw("metphi>>hmet_phi","","goff")
tAK4PFPuppi.Draw("metNoHFphi>>hmetNoHF_phi","","goff")
tAK4PFPuppi.Draw("metPUPPIphi>>hmetPUPPI_phi","","goff")

#Normalized the histograms
hmuon_pt.Scale(1.0/hmuon_pt.Integral())
hmuon_PuppiCombined.Scale(1.0/hmuon_PuppiCombined.Integral())
hmuon_PuppiWithLep.Scale(1.0/hmuon_PuppiWithLep.Integral())
hmuon_PuppiWithoutLep.Scale(1.0/hmuon_PuppiWithoutLep.Integral())
hmet_pt.Scale(1.0/hmet_pt.Integral())
hmetNoHF_pt.Scale(1.0/hmetNoHF_pt.Integral())
hmetPUPPI_pt.Scale(1.0/hmetPUPPI_pt.Integral())
hmet_phi.Scale(1.0/hmet_phi.Integral())
hmetNoHF_phi.Scale(1.0/hmetNoHF_phi.Integral())
hmetPUPPI_phi.Scale(1.0/hmetPUPPI_phi.Integral())

#Draw the histograms
c.cd(1)
tdrDraw(hmuon_pt,"HIST",kNone,kBlack,kSolid,-1,0,0)
c.cd(2)
gPad.SetLogy()
tdrDraw(hmuon_PuppiCombined,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hmuon_PuppiWithLep,"HIST",kNone,kRed,kSolid,-1,0,0)
tdrDraw(hmuon_PuppiWithoutLep,"HIST",kNone,kGreen,kSolid,-1,0,0)
c.cd(3)
tdrDraw(hmet_pt,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hmetNoHF_pt,"HIST",kNone,kRed,kSolid,-1,0,0)
tdrDraw(hmetPUPPI_pt,"HIST",kNone,kGreen,kSolid,-1,0,0)
c.cd(4)
tdrDraw(hmet_phi,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hmetNoHF_phi,"HIST",kNone,kRed,kSolid,-1,0,0)
tdrDraw(hmetPUPPI_phi,"HIST",kNone,kGreen,kSolid,-1,0,0)

# Add entries to the legend and draw it
c.cd(2)
l_isolation = tdrLeg(0.55,0.65,0.9,0.9)
l_isolation.SetTextSize(0.035)
l_isolation.AddEntry(hmuon_PuppiCombined,"iPUPPI (Combined)","l")
l_isolation.AddEntry(hmuon_PuppiWithLep,"iPUPPI (w/Lep)","l")
l_isolation.AddEntry(hmuon_PuppiWithoutLep,"iPUPPI (w/o Lep)","l")
l_isolation.Draw("same")
c.cd(3)
l_metpt = tdrLeg(0.65,0.65,0.9,0.9)
l_metpt.SetTextSize(0.035)
l_metpt.AddEntry(hmet_pt,"MET","l")
l_metpt.AddEntry(hmetNoHF_pt,"MET NoHF","l")
l_metpt.AddEntry(hmetPUPPI_pt,"PUPPET","l")
l_metpt.Draw("same")
c.cd(4)
l_metphi = tdrLeg(0.65,0.65,0.9,0.9)
l_metphi.SetTextSize(0.035)
l_metphi.AddEntry(hmet_phi,"MET","l")
l_metphi.AddEntry(hmetNoHF_phi,"MET NoHF","l")
l_metphi.AddEntry(hmetPUPPI_phi,"PUPPET","l")
l_metphi.Draw("same")


# Save the canvases
# Causes an issue with the CMS text in the current window after the operation
# However, the saved files do not show this problem
#c.Print('plots_pileup_3.png', 'png')
#c.Print('plots_pileup_3.pdf', 'pdf')

