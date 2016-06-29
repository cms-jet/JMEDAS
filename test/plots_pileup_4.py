from ROOT import *
from Analysis.JMEDAS.tdrstyle_mod14 import *
from collections import OrderedDict
from optparse import OptionParser

parser = OptionParser()
parser.add_option('--doPUPPI', action='store_true', default=False, dest='doPUPPI',
                  help='Plot the PFPuppi algorithm as well (if it exists in the ntuple')
parser.add_option('--drawFits', action='store_true', default=False, dest='drawFits',
                  help='Flag to draw, or not, the Gaussian fits to the response curves')
parser.add_option('--drawLines', action='store_false', default=True, dest='drawLines',
                  help='Flag to draw, or not, the lines at the mean of the Gaussian fit')
parser.add_option('--ifilename', type='string', action='store', default='pileupNtuple.root',
                  dest='ifilename', help='The name of the input ROOT file.')
parser.add_option('--jetcollection', type='string', action='store', default='AK4PFCHSL1L2L3',
                  dest='jetcollection', help="The jet collections to get from the ntuple.")
parser.add_option('--nsigma', type='int', action='store', default=1.0, dest='nsigma',
                  help="The number of sigma from the histogram mean which is used to determine the fit range.")
(options, args) = parser.parse_args()

# Set the ROOT style
gROOT.Macro("rootlogon.C")
setTDRStyle()

# Filename suffixes
ifilenames = OrderedDict([("",kBlack),("_JESUncertaintyUp",kBlack),("_JESUncertaintyDown",kBlack),("_JER",kRed),("_JERUncertaintyUp",kRed),("_JERUncertaintyDown",kRed)])

# Create and draw the canvas
frame = TH1D()
frame.GetXaxis().SetLimits(0.0,2.0)
frame.GetYaxis().SetRangeUser(0.0,0.12)
frame.GetXaxis().SetTitle("Response (p_{T}^{RECO}/p_{T}^{GEN})")
frame.GetYaxis().SetTitle("a.u.")
c = tdrCanvas("c",frame,14,11,True)

leg = tdrLeg(0.65,0.50,0.9,0.9)
leg.SetTextSize(0.035)
histograms = {}
fits = {}
lines = {}
for ifilename_suffix in ifilenames:
    ifilename = "JECNtuple_MiniAOD"+ifilename_suffix+".root"
    print "Processing the file "+ifilename+" ... "

    f = TFile(ifilename,"READ")

    if not f.GetDirectory(options.jetcollection):
        print "ERROR::Cannot find the jet collection "+options.jetcollection+" in the input file "+ifilename
        exit(-1)

    tree = f.Get(options.jetcollection+"/t")

    # Create the histograms
    hname = "h"+options.jetcollection+ifilename_suffix

    print "\tDoing the histogram",hname,"..."

    histograms[hname] = TH1D(hname,hname,80,0,2)

    # Fill the histograms
    for event in tree:
        for jet, pt_from_tree in enumerate(event.jtpt):
            pt_updated = pt_from_tree
            if event.refpt[jet]==0:
                continue
            rsp = pt_updated/event.refpt[jet]
            if rsp<2.0 and rsp>0.0 and abs(event.jteta[jet])<1.3:
                histograms[hname].Fill(rsp)

    # Normalize the histograms
    histograms[hname].Scale(1.0/histograms[hname].Integral())

    if "Up" in ifilename_suffix:
        style = kDotted
    elif "Down" in ifilename_suffix:
        style = kDashed
    else:
        style = kSolid

    # Fit a Gaussian to the response curves
    fname = "f"+options.jetcollection+ifilename_suffix
    fits[fname] = TF1(fname,"gaus",histograms[hname].GetMean()-(options.nsigma*histograms[hname].GetRMS()),histograms[hname].GetMean()+(options.nsigma*histograms[hname].GetRMS()))
    fits[fname].SetParNames("N","#mu","#sigma")
    fits[fname].SetLineColor(ifilenames[ifilename_suffix])
    fits[fname].SetLineStyle(style)
    histograms[hname].Fit(fits[fname],"RQ0")
    
    # Create lines based on the fits
    lname = "l"+options.jetcollection+ifilename_suffix
    lines[lname] = TLine(fits[fname].GetParameter(1),0.0,fits[fname].GetParameter(1),0.12)
    lines[lname].SetLineColor(ifilenames[ifilename_suffix])
    lines[lname].SetLineStyle(style)

    # Add entries to the legend     
    leg.AddEntry(histograms[hname],ifilename_suffix.replace("_","") if ifilename_suffix!="" else str(options.jetcollection),"l")

    c.cd()
    tdrDraw(histograms[hname],"HIST",kNone,ifilenames[ifilename_suffix],style,-1,0,0)

    # Draw the fits
    if options.drawFits:
        fits[fname].Draw("same")

    # Draw the lines
    if options.drawLines:
        lines[lname].Draw("same")

#Draw the legend
leg.Draw("same")

c.Update()
c.Draw()

# Save the canvases
c.Print('plots_pileup_4.png', 'png')
