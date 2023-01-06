# Loads the ROOT environment and style
import ROOT as r
from collections import OrderedDict
from Analysis.JMEDAS.tdrstyle_mod14 import *

# Set the ROOT style
r.gROOT.Macro("rootlogon.C")
setTDRStyle()
#r.enableJSVis()

#Settings for each of the pads in the canvas
settingsTMP = {'X'         : (4,0.0,60.0,0.0,0.04,"X","a.u."),
               'RhoVsNpv'  : (2,0.0,60.0,0.0,60.0,"N_{PV}","#rho"),
               'NpvVsTnpu' : (1,0.0,60.0,0.0,60.0,"#mu","N_{PV}"),
               'RhoVsTnpu' : (3,0.0,60.0,0.0,60.0,"#mu","#rho")
               }
settings = OrderedDict(sorted(settingsTMP.items(), key=lambda x:x[1], reverse=False))

# Create and draw the canvas
frames = []
for f, s in enumerate(settings) :
    frame = r.TH1D()
    frames.append(frame)
    frames[f].GetXaxis().SetLimits(settings[s][1],settings[s][2])
    frames[f].GetYaxis().SetRangeUser(settings[s][3],settings[s][4])
    frames[f].GetXaxis().SetTitle(settings[s][5])
    frames[f].GetYaxis().SetTitle(settings[s][6])
c = tdrCanvasMultipad("c",frames,14,10,2,2)

# Open the ROOT file with the ntuple
f = r.TFile.Open("root://cmseos.fnal.gov//store/user/hats/2020/JEC/JECNtuple_MiniAOD.root")

# Access and store the necessary trees
tAK4PFchs   = f.Get("AK4PFCHSL1L2L3/t")

# Crease some histograms
hAK4PFchs_npv        = r.TH1D("hAK4PFchs_npv","hAK4PFchs_npv",60,0,60)
hAK4PFchs_rho        = r.TH1D("hAK4PFchs_rho","hAK4PFchs_rho",60,0,60)
hAK4PFchs_npu        = r.TH1D("hAK4PFchs_npu","hAK4PFchs_npu",60,0,60)
hAK4PFchs_tnpu       = r.TH1D("hAK4PFchs_tnpu","hAK4PFchs_tnpu",60,0,60)
hAK4PFchs_rhovsnpv   = r.TH2F("hAK4PFchs_rhovsnpv","hAK4PFchs_rhovsnpv",60,0,60,60,0,60)
hAK4PFchs_npvvsnpu   = r.TH2F("hAK4PFchs_npvvsnpu","hAK4PFchs_npvvsnpu",60,0,60,60,0,60)
hAK4PFchs_rhovsnpu   = r.TH2F("hAK4PFchs_rhovsnpu","hAK4PFchs_rhovsnpu",60,0,60,60,0,60)

# Fill the histograms
tAK4PFchs.Draw("npv:tnpus[12]>>hAK4PFchs_npvvsnpu","","goff")
tAK4PFchs.Draw("rho:npv>>hAK4PFchs_rhovsnpv","","goff")
tAK4PFchs.Draw("rho:tnpus[12]>>hAK4PFchs_rhovsnpu","","goff")

tAK4PFchs.Draw("npv>>hAK4PFchs_npv","","goff")
tAK4PFchs.Draw("rho>>hAK4PFchs_rho","","goff")
tAK4PFchs.Draw("npus[12]>>hAK4PFchs_npu","","goff")
tAK4PFchs.Draw("tnpus[12]>>hAK4PFchs_tnpu","","goff")

#Scale the histograms to be the same height
hAK4PFchs_npv.Scale(1.0/hAK4PFchs_npv.Integral())
hAK4PFchs_rho.Scale(1.0/hAK4PFchs_rho.Integral())
hAK4PFchs_npu.Scale(1.0/hAK4PFchs_npu.Integral())
hAK4PFchs_tnpu.Scale(1.0/hAK4PFchs_tnpu.Integral())

#Draw the histograms
c.cd(1)
tdrDraw(hAK4PFchs_npvvsnpu,"colz")
c.cd(2)
tdrDraw(hAK4PFchs_rhovsnpv,"colz")
c.cd(3)
tdrDraw(hAK4PFchs_rhovsnpu,"colz")
c.cd(4)
tdrDraw(hAK4PFchs_npv,"HIST",r.kNone,r.kBlack,r.kSolid,-1,0,0)
c.cd(4)
tdrDraw(hAK4PFchs_rho,"HIST",r.kNone,r.kRed,r.kSolid,-1,0,0)
c.cd(4)
tdrDraw(hAK4PFchs_npu,"HIST",r.kNone,r.kGreen,r.kSolid,-1,0,0)
c.cd(4)
tdrDraw(hAK4PFchs_tnpu,"HIST",r.kNone,r.kBlue,r.kSolid,-1,0,0)

# Add entries to the legend and draw it
c.cd(4)
l_X = tdrLeg(0.8,0.65,0.9,0.9)
l_X.AddEntry(hAK4PFchs_npv,"N_{PV}","l")
l_X.AddEntry(hAK4PFchs_rho,"#rho","l")
l_X.AddEntry(hAK4PFchs_npu,"N_{PU}","l")
l_X.AddEntry(hAK4PFchs_tnpu,"#mu","l")
l_X.Draw("same")

c.Update()
c.Draw()
c.Print('plot4.pdf','pdf')
