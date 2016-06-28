#
# Taken from https://github.com/kpedro88/TreeMaker/blob/upgrade2016/Production/test/pileupCorr.py
# Written by: Kevin Pedro
# Modified by: Alexx Perloff
#

import os, subprocess, array, time, math
from optparse import OptionParser
from Analysis.JMEDAS.tdrstyle_mod14 import *
from ROOT import *
import FWCore.ParameterSet.Config as cms

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

def DtoF(file,get):
    hD = file.Get(get)
    hF = TH1F()
    hD.Copy(hF)
    return hF

def hold_pointers_to_implicit_members( obj ):
  if not hasattr( obj, '_implicit_members' ):
    obj._implicit_members = []
  if hasattr( obj, 'GetListOfPrimitives' ):
    for prim in obj.GetListOfPrimitives():
      obj._implicit_members.append( prim )

'''
Interactive:
from Analysis.JMEDAS.pileupCorr import *
c = MakeCanvas(filename="../data/PileupHistograms.root")
c.Draw()
'''
def MakeCanvas(dataHists = [], MCHist = TH1F(), weightHists = [], filename = ""):
    if filename!='':
        f = TFile.Open(filename,"READ")
        dataHists.append(DtoF(f,"data_pu_central"))
        dataHists[-1].SetDirectory(None)
        dataHists.append(DtoF(f,"data_pu_up"))
        dataHists[-1].SetDirectory(None)
        dataHists.append(DtoF(f,"data_pu_down"))
        dataHists[-1].SetDirectory(None)
        MCHist = DtoF(f,"hMC25ns")
        MCHist.SetDirectory(None)
        weightHists.append(DtoF(f,"pu_weights_central"))
        weightHists[-1].SetDirectory(None)
        weightHists.append(DtoF(f,"pu_weights_up"))
        weightHists[-1].SetDirectory(None)
        weightHists.append(DtoF(f,"pu_weights_down"))
        weightHists[-1].SetDirectory(None)

    setTDRStyle()

    frame = TH1D()
    frame.GetXaxis().SetLimits(0,100)
    frame.GetYaxis().SetRangeUser(1e-11,1e4)
    frame.GetXaxis().SetTitle("#mu")
    frame.GetYaxis().SetTitle("Weights / a.u.")

    c = tdrCanvas("pileupCanvas",frame,14,11,True)
    c.cd()
    c.SetLogy()

    #Reweight the MC histogram
    MCHist_reweighted = MCHist.Clone("hMC25ns_reweighted")
    MCHist_reweighted.SetDirectory(None)
    for b in xrange(1,int(MCHist.GetNbinsX()+1)):
        MCHist_reweighted.SetBinContent(b,MCHist_reweighted.GetBinContent(b)*weightHists[0].GetBinContent(b))

    #Make TGraphAsymmErrors for the statistical+systematic error bands
    #First up is for the data histograms
    x       = array.array('f',[])
    y       = array.array('f',[])
    ex_up   = array.array('f',[])
    ex_down = array.array('f',[])
    ey_up   = array.array('f',[])
    ey_down = array.array('f',[])
    for b in xrange(1,int(dataHists[0].GetNbinsX()+1)):
        x.append(dataHists[0].GetBinCenter(b))
        y.append(dataHists[0].GetBinContent(b))
        ex_up.append(0.5)
        ex_down.append(0.5)
        if dataHists[1].GetBinContent(b) > dataHists[0].GetBinContent(b):
            ey_up.append(math.sqrt((dataHists[1].GetBinContent(b)-dataHists[0].GetBinContent(b))**2+(dataHists[0].GetBinError(b))**2))
            ey_down.append(math.sqrt((dataHists[0].GetBinContent(b)-dataHists[2].GetBinContent(b))**2+(dataHists[0].GetBinError(b))**2))
        else:
            ey_up.append(math.sqrt((dataHists[2].GetBinContent(b)-dataHists[0].GetBinContent(b))**2+(dataHists[0].GetBinError(b))**2))
            ey_down.append(math.sqrt((dataHists[0].GetBinContent(b)-dataHists[1].GetBinContent(b))**2+(dataHists[0].GetBinError(b))**2))
    errorBandData = TGraphAsymmErrors(len(x)-1,x,y,ex_down,ex_up,ey_down,ey_up)

    #Then we do the weight histograms
    x       = array.array('f',[])
    y       = array.array('f',[])
    ex_up   = array.array('f',[])
    ex_down = array.array('f',[])
    ey_up   = array.array('f',[])
    ey_down = array.array('f',[])
    for b in xrange(1,int(weightHists[0].GetNbinsX()+1)):
        x.append(weightHists[0].GetBinCenter(b))
        y.append(weightHists[0].GetBinContent(b))
        ex_up.append(0.5)
        ex_down.append(0.5)
        if weightHists[1].GetBinContent(b) > weightHists[0].GetBinContent(b):
            ey_up.append(math.sqrt((weightHists[1].GetBinContent(b)-weightHists[0].GetBinContent(b))**2+(weightHists[0].GetBinError(b))**2))
            ey_down.append(math.sqrt((weightHists[0].GetBinContent(b)-weightHists[2].GetBinContent(b))**2+(weightHists[0].GetBinError(b))**2))
        else:
            ey_up.append(math.sqrt((weightHists[2].GetBinContent(b)-weightHists[0].GetBinContent(b))**2+(weightHists[0].GetBinError(b))**2))
            ey_down.append(math.sqrt((weightHists[0].GetBinContent(b)-weightHists[1].GetBinContent(b))**2+(weightHists[0].GetBinError(b))**2))
    errorBandWeight = TGraphAsymmErrors(len(x)-1,x,y,ex_down,ex_up,ey_down,ey_up)

    #Draw all histograms and graphs
    tdrDraw(errorBandData,"4",kNone,kNone,kNone,kNone,3144,kGray)
    tdrDraw(dataHists[0],"e1",kFullCircle,kBlack)
    tdrDraw(MCHist,"e1p",kFullCircle,kGreen,kNone,kGreen,kNone,kNone)
    tdrDraw(MCHist_reweighted,"e1p",kOpenCircle,kGreen,kNone,kGreen,kNone,kNone)
    tdrDraw(errorBandWeight,"4",kNone,kNone,kNone,kNone,3144,kRed+2)
    tdrDraw(weightHists[0],"e1",kFullTriangleUp,kRed)

    #Draw a legend
    leg = tdrLeg(0.5, 0.65, 0.88, 0.88)
    leg.AddEntry(dataHists[0],"Data","ep")
    leg.AddEntry(errorBandData,"Data Stat+Sys","f")
    leg.AddEntry(MCHist,"MC","ep")
    leg.AddEntry(MCHist_reweighted,"MC (Reweighted)","ep")
    leg.AddEntry(weightHists[0],"Weights","ep")
    leg.AddEntry(errorBandWeight,"Weight Stat+Sys","f")
    leg.Draw("same")

    #Set the canvas to own the histograms and graphs which are drawn
    hold_pointers_to_implicit_members(c)

    print "Canvas Successfully Made!"
    return c

# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------

'''
Example:
python ../python/pileupCorr.py -j Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt -l pileup_latest.txt -b 100
'''
if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-o", "--outname", dest="outname", default="PileupHistograms.root", help="output filename for PU histos (default = %default)")
    parser.add_option("-j", "--json", dest="json", default="data/Cert_271036-275125_13TeV_PromptReco_Collisions16_JSON.txt", help="golden JSON for data (default = %default)")
    parser.add_option("-l", "--latest", dest="latest", default="data/pileup_latest.txt", help="latest pileup file (default = %default)")
    parser.add_option("-s", "--scenario", dest="scenario", default="SimGeneral.MixingModule.mix_2016_25ns_SpringMC_PUScenarioV1_PoissonOOTPU_cfi", help="CMSSW python file for pileup scenario (default = %default)")
    parser.add_option("-m", "--minbias", dest="minbias", default=71300, help="minbias xsec in mb (default = %default)")
    parser.add_option("-u", "--uncertainty", dest="uncertainty", default=0.0485, help="minbias xsec uncertainty (default = %default)")
    parser.add_option("-b", "--nbins", dest="nbins", default=50, help="max number of bins for histos (default = %default)")
    (options, args) = parser.parse_args()
    
    # get scenario
    mix = getattr(__import__(options.scenario,fromlist=["mix"]),"mix")
    probvalue = mix.input.nbPileupEvents.probValue
    
    # generate pileup histograms in data
    os.system("pileupCalc.py -i "+options.json+" --inputLumiJSON "+options.latest+" --calcMode true --minBiasXsec "+str(options.minbias)+" --maxPileupBin "+str(options.nbins)+" --numPileupBins "+str(options.nbins)+" CentralPileupHistogram.root")
    os.system("pileupCalc.py -i "+options.json+" --inputLumiJSON "+options.latest+" --calcMode true --minBiasXsec "+str(options.minbias*(1+options.uncertainty))+" --maxPileupBin "+str(options.nbins)+" --numPileupBins "+str(options.nbins)+" UpPileupHistogram.root")
    os.system("pileupCalc.py -i "+options.json+" --inputLumiJSON "+options.latest+" --calcMode true --minBiasXsec "+str(options.minbias*(1-options.uncertainty))+" --maxPileupBin "+str(options.nbins)+" --numPileupBins "+str(options.nbins)+" DownPileupHistogram.root")
    
    # open files
    fc = TFile.Open("CentralPileupHistogram.root","read")
    fup = TFile.Open("UpPileupHistogram.root","read")
    fdown = TFile.Open("DownPileupHistogram.root","read")
    fout = TFile.Open(options.outname,"RECREATE")
    
    # get histos
    hdata_central = DtoF(fc,"pileup")
    hdata_up = DtoF(fup,"pileup")
    hdata_down = DtoF(fdown,"pileup")

    # scale histos
    hdata_central.Scale(1/hdata_central.Integral(1,int(options.nbins)))
    hdata_up.Scale(1/hdata_up.Integral(1,int(options.nbins)))
    hdata_down.Scale(1/hdata_down.Integral(1,int(options.nbins)))

    # save histos
    hdata_central.SetName("data_pu_central")
    hdata_up.SetName("data_pu_up")
    hdata_down.SetName("data_pu_down")
    hdata_central.Write()
    hdata_up.Write()
    hdata_down.Write()

    # MC histo
    hMC25ns = TH1F("hMC25ns", "", int(options.nbins), 0, int(options.nbins))
    for b in xrange(0,int(options.nbins)):
        hMC25ns.SetBinContent(b+1,probvalue[b] if b < len(probvalue) else 0)
        hMC25ns.SetBinError(b+1,0)
    hMC25ns.Scale(1/hMC25ns.Integral(1,int(options.nbins)))
    hMC25ns.Write()
    
    # divide histos
    hPUWeightsCentral = hMC25ns.Clone("pu_weights_central")
    hPUWeightsUp = hMC25ns.Clone("pu_weights_up")
    hPUWeightsDown = hMC25ns.Clone("pu_weights_down")
    hPUWeightsCentral.Divide(hdata_central, hMC25ns, 1., 1.)
    hPUWeightsUp.Divide(hdata_up, hMC25ns, 1., 1.)
    hPUWeightsDown.Divide(hdata_down, hMC25ns, 1., 1.)
    hPUWeightsCentral.Write()
    hPUWeightsUp.Write()
    hPUWeightsDown.Write()

    dataHists = [hdata_central, hdata_up, hdata_down]
    weightHists = [hPUWeightsCentral, hPUWeightsUp, hPUWeightsDown]
    c = MakeCanvas(dataHists,hMC25ns,weightHists)
    c.Write()

    fout.Close()