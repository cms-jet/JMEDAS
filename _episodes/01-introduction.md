---
title: "Jets 101"
teaching: 0
exercises: 0
questions:
- "What is a jet?"
objectives:
- "Learn about jets, their different origin, types and reclustering algorithms."
keypoints:
- "First key point. Brief Answer to questions. (FIXME)"
---

In your cmslpc ssh session that was opened in the preliminary step in the README instructions, navigate to directory section1 and follow the instructions in the below notebooks.
Please note that the code shown in the notebooks is just for you to understand what each python script is doing and there's minor differences in the actual scripts that you will execute and sometimes modify in your ssh session. 


## Jet Basics

This preliminary exercise will illustrate some of the basic properties of jets in CMS. Let's start by running the histogram-making code on some MC. While the script is running, take a look at the script and make sure you understand what it's doing.

~~~
python $CMSSW_BASE/src/Analysis/JMEDAS/scripts/jmedas_make_histograms.py --files=$CMSSW_BASE/src/Analysis/JMEDAS/data/MiniAODs/RunIIFall17MiniAODv2/ttjets2023.txt --outname=$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets.root --maxevents=2000 --maxjets=6 --maxFiles 2
~~~
{: .language-bash}

Now let's plot the resulting histograms. Take a look at the simple plotting script below and execute it with

~~~
python basics.py
~~~
{: .language-bash}

~~~
import os
import sys

# Loads the ROOT environment and style
import ROOT
from collections import OrderedDict

# Imports for running locally
sys.path.append(os.path.expandvars("$CMSSW_BASE/src/Analysis/JMEDAS/python"))

# Disable pop-up windows for smoother running over ssh
ROOT.gROOT.SetBatch(True)

f = ROOT.TFile("$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets.root")

h_ptAK4   = f.Get("h_ptAK4")
h_etaAK4  = f.Get("h_etaAK4")
h_phiAK4  = f.Get("h_phiAK4")
h_mAK4    = f.Get("h_mAK4")

c = ROOT.TCanvas('c', 'c', 800, 600)

c.Divide(2,2)
c.cd(1)
ROOT.gPad.SetLogy()
h_ptAK4.Draw()
h_ptAK4.GetXaxis().SetRangeUser(0, 1000)
c.cd(2)
h_etaAK4.Draw()
c.cd(3)
h_phiAK4.Draw()
h_phiAK4.SetMinimum(0)
c.cd(4)
ROOT.gPad.SetLogy()
h_mAK4.Draw()
h_mAK4.GetXaxis().SetRangeUser(0, 200)
ROOT.gPad.SetLogy()

c.Draw()
c.SaveAs('plots1.pdf', 'pdf')
~~~
{: .language-python}

{% include links.md %}

