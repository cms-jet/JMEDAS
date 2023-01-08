import ROOT

def compareHistogram(variable, processes=["tt", "rsg", "wqq", "qcd"]):
    hist_files = {
        "tt": ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets.root"), 
        "rsg": ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/rsgluon_ttbar_3000GeV.root"), 
        "wqq": ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/WJetsToQQ_HT600to800.root"), 
        "qcd": ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/QCD_Pt_470to600.root")
    }
    hists = {}
    for iprocess, process in enumerate(processes):
        #print(process)
        hists[process] = hist_files[process].Get("h_{}".format(variable))
        if not hists[process]:
            print "ERROR : didn't find histogram {} in file {}".format("h_{}".format(variable), hist_files[process].GetPath())
        hists[process].SetDirectory(0)
        hists[process].SetLineColor(iprocess+1)
        hists[process].Rebin(2)
        if hists[process].Integral() > 0:
            hists[process].Scale(1. / hists[process].Integral())
    
    # Dummy histogram for drawing axes on TCanvas
    #hframe = ROOT.TH1F("hframe", "hframe", hists["tt"].GetNbinsX(), hists["tt"].GetXaxis().GetXmin(), hists["tt"].GetXaxis().GetXmax())
    #hframe.SetDirectory(0)
    #hframe.GetXaxis().SetTitle(variable)
    #hframe.SetMinimum(0.)
    #hframe.SetMaximum(1.2 * max([hists[process].GetMaximum() for process in ["tt", "rsg", "wqq"]]))

    if variable == "ak8_N2_beta1":
        hists[processes[0]].GetXaxis().SetRangeUser(0., 0.5)
    elif variable == "logrhoRatioAK8":
        for process in processes:
            hists[process].Rebin(5)

    hists[processes[0]].SetMaximum(1.2 * max([hists[process].GetMaximum() for process in processes]))

    legend = ROOT.TLegend(0.15, 0.65, 0.4, 0.85)
    legend.SetFillColor(0)
    legend.SetFillStyle(0)
    legend.SetBorderSize(0)
    
    legend_entries = {
        "tt": "t#bar{t}", 
        "rsg": "RS KK gluon",
        "wqq": "W(qq)", 
        "qcd": "QCD"
    }
    
    for process in processes:
        legend.AddEntry(hists[process], legend_entries[process], "l")
    
    canvas = ROOT.TCanvas(variable, variable, 700, 500) 

    #hframe.Draw()
    for iprocess, process in enumerate(processes):
        if iprocess == 0:
            draw_opts = "hist"
        else:
            draw_opts = "hist same"
        hists[process].Draw(draw_opts)
    
    legend.Draw()
    canvas.Draw()
    return canvas, legend, hists
