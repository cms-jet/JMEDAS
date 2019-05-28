def computeROC(varlist):

    import ROOT

    ROOT.gStyle.SetOptStat(0)

    ROOT.TMVA.Tools.Instance()

    output = ROOT.TFile.Open('TMVA.root', 'RECREATE')

    factory = ROOT.TMVA.Factory('TMVAClassification', output, '!V:!Silent:Color:DrawProgressBar:Transformations=D,G:AnalysisType=Classification')

    signalF = ROOT.TFile.Open('files/rsgluon_ttbar_3TeV.root', 'READ')
    backgdF = ROOT.TFile.Open('files/qcd.root', 'READ')

    signalTree = signalF.Get('varTree')
    backgdTree = backgdF.Get('varTree') 

    dataloader = ROOT.TMVA.DataLoader("dataset")

    varString = ""
    for var in varlist:
        dataloader.AddVariable(var)
        varString = varString+"_"+var

    dataloader.AddSignalTree(signalTree, 1.0)
    dataloader.AddBackgroundTree(backgdTree, 1.0)
    dataloader.SetBackgroundWeightExpression("1")
    dataloader.SetSignalWeightExpression("1")

    dataloader.PrepareTrainingAndTestTree(ROOT.TCut('1'),ROOT.TCut('1'), 'nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=None:!V')

    factory.BookMethod(dataloader, ROOT.TMVA.Types.kCuts, 'Cuts', '!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart')

    factory.TrainAllMethods()
    factory.TestAllMethods()
    factory.EvaluateAllMethods()

    output.cd()

    c1 = ROOT.TCanvas('c1', 'c1') 
    
    rocHist = output.Get('dataset/Method_Cuts/Cuts/MVA_Cuts_effBvsS')
    rocHist.SetTitle('ROC Curve')
    rocHist.GetXaxis().SetTitle('Signal Efficiency')
    rocHist.GetYaxis().SetTitle('Background Efficiency')
    rocHist.SetMinimum(0.001)
    rocHist.SetLineWidth(3)
    rocHist.Draw()
    ROOT.gPad.SetLogy(1)
    ROOT.gPad.SetGrid()

    legText = " + ".join(varlist)

    leg = ROOT.TLegend(0.50, 0.14, 0.88, 0.33)
    leg.AddEntry(rocHist, legText[:-3], 'l')
    leg.SetFillStyle(0)
    leg.SetLineWidth(0)
    leg.Draw()
    
    c1.Draw()
    
    return c1
