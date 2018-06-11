from ROOT import *
import sys

gStyle.SetOptStat(0)

TMVA.Tools.Instance()

output = TFile.Open('TMVA.root', 'RECREATE')

factory = TMVA.Factory('TMVAClassification', output, '!V:!Silent:Color:DrawProgressBar:Transformations=D,G:AnalysisType=Classification')

signalF = TFile.Open('zprime3000_short.root', 'READ')
backgdF = TFile.Open('qcd_short.root', 'READ')

signalTree = signalF.Get('varTree')
backgdTree = backgdF.Get('varTree') 

dataloader = TMVA.DataLoader("dataset")

varString = ""
for var in sys.argv[1:]:
	dataloader.AddVariable(var)
	varString = varString+"_"+var

dataloader.AddSignalTree(signalTree, 1.0)
dataloader.AddBackgroundTree(backgdTree, 1.0)
dataloader.SetBackgroundWeightExpression("1")
dataloader.SetSignalWeightExpression("1")

dataloader.PrepareTrainingAndTestTree(TCut('1'),TCut('1'), 'nTrain_Signal=0:nTrain_Background=0:SplitMode=Random:NormMode=None:!V')

factory.BookMethod(dataloader, TMVA.Types.kCuts, 'Cuts', '!H:!V:FitMethod=MC:EffSel:SampleSize=200000:VarProp=FSmart')

factory.TrainAllMethods()
factory.TestAllMethods()
factory.EvaluateAllMethods()

output.cd()

rocHist = output.Get('dataset/Method_Cuts/Cuts/MVA_Cuts_effBvsS')
rocHist.SetTitle('ROC Curve')
rocHist.GetXaxis().SetTitle('Signal Efficiency')
rocHist.GetYaxis().SetTitle('Background Efficiency')
rocHist.SetMinimum(0.001)
rocHist.SetLineWidth(3)
rocHist.Draw()
gPad.SetLogy(1)
gPad.SetGrid()



legText = ''
for var in sys.argv[1:]:
	legText += str(var)
	legText += " + "

leg = TLegend(0.50, 0.14, 0.88, 0.33)
leg.AddEntry(rocHist, legText[:-3], 'l')
leg.SetFillStyle(0)
leg.SetLineWidth(0)
leg.Draw()


c1.SaveAs("computeROC{0}.png".format(varString))
