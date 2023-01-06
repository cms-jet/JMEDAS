# Jet CMS DAS Exercise

## CMS DAS January  2023
  
### Introduction
This tutorial is intended to provide you with the basic you need in order to deal with jets in your analysis. We start with the basics of what is a jet, how are they reconstructed, what algorithms are used, etc. Then we give examples with scripts on how to access jets and use them in your analysis frameworks, including corrections and systematics. In the second part of the exercise, we examine jet substructure algorithms, which have many uses including identification of hadronic decays of heavy SM particles like top quarks, W, Z, and H bosons, as well as mitigation of pileup and others.

We recommend two ways of following this tutorial: in cmslpc or in SWAN. You do not need to follow both recipes below, use the one that you like the most.

## Run exercises in cmslpc

Open a terminal/console, connect to cmslpc-sl7 and prepare your working area (instructios are in a bash shell syntax):

```
kinit username@FNAL.GOV
ssh -Y username@cmslpc-sl7.fnal.gov
mkdir JMEDAS2023
cd JMEDAS2023

export SCRAM_ARCH=slc7_amd64_gcc700
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_10_6_18
cd CMSSW_10_6_18/src
cmsenv

git clone https://github.com/juska/JMEDAS.git Analysis/JMEDAS
git clone https://github.com/cms-jet/JetToolbox Analysis/JetToolbox -b jetToolbox_102X_v3
cd Analysis/JMEDAS
scram b -j 4
```

For some exercises we also need to access files in remote servers, so activate your grid certificate:


## Grid certificate

To access data stored remotely in different places, you need to set your grid certificate. 

 *For *cmslpc*, you only need to run (to get a valid certificate):
```bash
voms-proxy-init -voms cms -valid 192:00
```
## Jet Basics

This preliminary exercise will illustrate some of the basic properties of jets in CMS. Let's start by running the histogram-making code on some MC. While the script is running, take a look at the script and make sure you understand what it's doing.

```
# In bash shell
python $CMSSW_BASE/src/Analysis/JMEDAS/scripts/jmedas_make_histograms.py --files=$CMSSW_BASE/src/Analysis/JMEDAS/data/MiniAODs/RunIIFall17MiniAODv2/ttjets2023.txt --outname=$CMSSW_BASE/src/Analysis/JMEDAS/notebooks/files/ttjets.root --maxevents=2000 --maxjets=6 --maxFiles 5
```

Now let's plot the resulting histograms:

```
python basics.py
```

Open the produced plot:

```
evince plots1.pdf
```

The first run included only 2000 events. Increase this to 10000 or more and redo the plot and see how it looks like now.

The first set of plots shows only AK4 jets. Modify the basics.py code to include also AK8 jets -- the needed histograms are already available in ttjets.root.
Add the AK8 histograms to the same canvases, they are already filled and available (draw option 'same', line color 'ROOT.kRed').

How are the AK8 histograms different and why?

## Tutorial
Once you've completed the setup instructions, change to the directory `~/SWAN_projects/CMSDAS_jetExercise/DAS/` in SWAN. Information on the separate tutorial can be found in the "notebooks" subdirectory.

## Additional Information & Resources

  - [JERC Subgroup Twiki Page](https://twiki.cern.ch/twiki/bin/view/CMS/JetEnergyScale)
    - [JEC and JER Reference Sample Page](https://twiki.cern.ch/twiki/bin/view/CMS/JERCReference)
    - [WorkBook Page on Jet Energy Corrections](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyCorrections?redirectedfrom=CMS.WorkBookJetEnergyCorrections)
    - [WorkBook Page on Jet Energy Resolution](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookJetEnergyResolution)
  - [JetMET/JERC/JMAR Weekly Meetings](https://indico.cern.ch/categoryDisplay.py?categId=1308)
  - [Run2 Weekly Discussion Group](https://indico.cern.ch/category/7082/)
    - Every other week there is a meeting on jets and pileup
  - SQLite files, text files, and tarballs
    - [JEC Database](https://github.com/cms-jet/JECDatabase)
    - [JER Database](https://github.com/cms-jet/JRDatabase)
  - [JetToolbox Twiki Page](https://twiki.cern.ch/twiki/bin/view/CMS/JetToolbox)
  - [2017 MiniAOD Twiki Page](https://twiki.cern.ch/twiki/bin/view/CMSPublic/WorkBookMiniAOD2017)
