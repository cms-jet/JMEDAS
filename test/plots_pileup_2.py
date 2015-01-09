from ROOT import *
from Analysis.JMEDAS.tdrstyle_mod14 import *

gROOT.Macro("rootlogon.C")

setTDRStyle()

f = TFile("pileupNtuple.root")

tAK4PFchs   = f.Get("AK4PFchs/t")
tAK4PFchsl1 = f.Get("AK4PFchsl1/t")
tAK4PUPPI   = f.Get("AK4PUPPI/t")

hAK4PFchs_response   = TH1D("hAK4PFchs_response","hAK4PFchs_response",80,0,2)
hAK4PFchsl1_response = TH1D("hAK4PFchsl1_response","hAK4PFchsl1_response",80,0,2)
hAK4PUPPI_response   = TH1D("hAK4PUPPI_response","hAK4PUPPI_response",80,0,2)
tAK4PFchs.Draw("jtpt/refpt>>hAK4PFchs_response","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>10 && jteta<1.3","geoff")
tAK4PFchsl1.Draw("jtpt/refpt>>hAK4PFchsl1_response","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>10 && jteta<1.3","geoff")
tAK4PUPPI.Draw("jtpt/refpt>>hAK4PUPPI_response","jtpt/refpt<2 && jtpt/refpt>0 && jtpt>10 && jteta<1.3","geoff")

frame = TH1D()
frame.GetXaxis().SetLimits(0.0,2.0)
#frame.GetXaxis().SetMoreLogLabels()
#frame.GetXaxis().SetNoExponent()
frame.GetYaxis().SetRangeUser(0.0,1700)
frame.GetXaxis().SetTitle("Response (p_{T}^{RECO}/p_{T}^{GEN})")
frame.GetYaxis().SetTitle("Number of Jets")
c = tdrCanvas("c",frame,2,11,true)
l = tdrLeg(0.6,0.6,0.9,0.9)

tdrDraw(hAK4PFchs_response,"HIST",kNone,kBlack,kSolid,-1,0,0)
tdrDraw(hAK4PFchsl1_response,"HIST",kNone,kRed,kSolid,-1,0,0)
tdrDraw(hAK4PUPPI_response,"HIST",kNone,kGreen,kSolid,-1,0,0)

l.AddEntry(hAK4PFchs_response,"AK4PFchs","l")
l.AddEntry(hAK4PFchsl1_response,"AK4PFchsl1","l")
l.AddEntry(hAK4PUPPI_response,"AK4PUPPI","l")

l.Draw("same")

c.Print('plots_pileup_2.png', 'png')
c.Print('plots_pileup_2.pdf', 'pdf')

