# Jet CMS DAS Exercise

## CMS DAS January  2023
  
### Introduction
This tutorial is intended to provide you with the basic you need in order to deal with jets in your analysis. We start with the basics of what is a jet, how are they reconstructed, what algorithms are used, etc. Then we give examples with scripts on how to access jets and use them in your analysis frameworks, including corrections and systematics. In the second part of the exercise, we examine jet substructure algorithms, which have many uses including identification of hadronic decays of heavy SM particles like top quarks, W, Z, and H bosons, as well as mitigation of pileup and others.

The tutorial is designed to be executed at cmslpc and followed in the JMEDAS 2023 twiki page, where you find links to instructional slides and (read-only) notebooks that walk you through the exercises.

## Run exercises in cmslpc

Open a terminal/console, connect to cmslpc-sl7 and prepare your working area (instructions are in bash shell syntax):

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

In some exercises we also need to access files in remote servers, so activate your grid certificate:
```
voms-proxy-init -voms cms -valid 192:00
```

If you like seeing your working directory in the commandline, you can do also this by adding a line to ~/.bashrc and activating it with the 'source' command:

```
echo "PS1='\W\$ '" >> ~/.bashrc
source ~/.bashrc
```

Now you can go back to the TWiki page and start with the basics in Section 1.

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
