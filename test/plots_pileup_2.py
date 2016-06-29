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
parser.add_option('--algsize', type='string', action='store', default='AK4', dest='algsize'
		  help="The algorithm and size of the jet collections to get from the ntuple.")
(options, args) = parser.parse_args()

# Set the ROOT style
gROOT.Macro("rootlogon.C")
setTDRStyle()

#Settings for each of the pads in the canvas
settingsTMP = {'response' : (1,0.0,2.0,0.0,0.12,"Response (p_{T}^{RECO}/p_{T}^{GEN})","a.u.",False),
			   'pt'       : (2,10.0,200.0,0.0,0.21,"p_{T}^{RECO}","a.u.",True),
			   'eta' 	  : (3,-5,5,0.0,0.1,"#eta","a.u.",False),
			   'phi' 	  : (4,-3.14159,3.14159,0.0,0.04,"#phi","a.u.",False)
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
	if settings[s][6] :
		frames[f].GetXaxis().SetMoreLogLabels()
		frames[f].GetXaxis().SetNoExponent()
c = tdrCanvasMultipad("c",frames,14,11,2,2)

# Open the ROOT file with the ntuple
f = TFile(options.ifilename)

# Histogram settings
alg_size = options.algsize
jetTypes = OrderedDict([("PF" , kBlack),("PFchs" , kRed),("PFPuppi" , kGreen)])
corrections = OrderedDict([("Uncorrected" , kDotted),("L1" , kDashed),("L1L2L3" , kSolid)])
hsettingsTMP = {'response' : (1,80,0,2),
			    'pt'       : (2,200,0,1000),
			    'eta' 	   : (3,50,-5,5),
			    'phi' 	   : (4,50,-3.14159,3.14159),
			    }
hsettings = OrderedDict(sorted(hsettingsTMP.items(), key=lambda x:x[1], reverse=False))
nsigma = 1.0

histograms = {}
fits = {}
lines = {}
legends = {}
for hs in hsettings:
	print "Doing the",hs,"pad ... "

	legname = "leg_"+hs
	legends[legname] = tdrLeg(0.65,0.50,0.9,0.9)
	legends[legname].SetTextSize(0.035)

	for jt in jetTypes:
		if not options.doPUPPI and jt == "PFPuppi":
			continue
		if not f.GetDirectory(alg_size+jt.upper()+"L1L2L3"):
			continue

		tree = f.Get(alg_size+jt.upper()+"L1L2L3/t")

		for cor in corrections:	
			# Create the histograms
			hname = "h"+alg_size+jt+"_"+cor+"_"+hs

			print "\tDoing the histogram",hname,"..."

			histograms[hname] = TH1D(hname,hname,hsettingsTMP[hs][1],hsettingsTMP[hs][2],hsettingsTMP[hs][3])

			# Fill the histograms
			for event in tree:
				for jet, pt_from_tree in enumerate(event.jtpt):
					if cor == "Uncorrected":
						pt_updated = (pt_from_tree/event.jtjec[jet][0].second)
					elif cor == "L1":
						pt_updated = (pt_from_tree/event.jtjec[jet][1].second)
					else:
						pt_updated = pt_from_tree

					if event.refpt[jet]==0:
						continue
					rsp = pt_updated/event.refpt[jet]
					#print "JEC Level: "+str(event.jtjec[jet][0].first)+"\tJEC Factor: "+str(event.jtjec[jet][0].second)+"\tOriginal pT: "+str(pt_from_tree)+"\tUncorrected pT: "+str(pt_from_tree/event.jtjec[jet][0].second)+"\tRef pT: "+str(event.refpt[jet])
					if rsp<2.0 and rsp>0.0 and abs(event.jteta[jet])<1.3:
						if hs == "response":
							histograms[hname].Fill(rsp)
						elif hs == "pt":
							histograms[hname].Fill(pt_updated)
						elif hs == "eta":
							histograms[hname].Fill(event.jteta[jet])
						elif hs == "phi":
							histograms[hname].Fill(event.jtphi[jet])

			# Normalize the histograms
			histograms[hname].Scale(1.0/histograms[hname].Integral())

			if hs == "response":
				# Fit a Gaussian to the response curves
				fname = "f"+alg_size+jt+"_"+cor+"_"+hs
				fits[fname] = TF1(fname,"gaus",histograms[hname].GetMean()-(nsigma*histograms[hname].GetRMS()),histograms[hname].GetMean()+(nsigma*histograms[hname].GetRMS()))
				fits[fname].SetParNames("N","#mu","#sigma")
				fits[fname].SetLineColor(jetTypes[jt])
				fits[fname].SetLineStyle(corrections[cor])
				histograms[hname].Fit(fits[fname],"RQ0")
	
				# Create lines based on the fits
				lname = "l"+alg_size+jt+"_"+cor+"_"+hs
				lines[lname] = TLine(fits[fname].GetParameter(1),settings["response"][3],fits[fname].GetParameter(1),settings["response"][4])
				lines[lname].SetLineColor(jetTypes[jt])
				lines[lname].SetLineStyle(corrections[cor])

			# Add entries to the legend		
			legends[legname].AddEntry(histograms[hname],str(alg_size+jt+cor).replace("Uncorrected",""),"l")

			c.cd(hsettingsTMP[hs][0])
			tdrDraw(histograms[hname],"HIST",kNone,jetTypes[jt],corrections[cor],-1,0,0)

			if hs == "response":
				# Draw the fits
				if options.drawFits:
					c.cd(hsettingsTMP[hs][0])
					fits[fname].Draw("same")

				# Draw the lines
				if options.drawLines:
					c.cd(hsettingsTMP[hs][0])
					lines[lname].Draw("same")
			elif hs == "pt":
				gPad.SetLogx()

	#Draw the legend
	c.cd(hsettingsTMP[hs][0])
	legends[legname].Draw("same")	
c.Update()
c.Draw()


# Save the canvases
c.Print('plots_pileup_2.png', 'png')
