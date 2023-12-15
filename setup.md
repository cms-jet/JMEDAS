---
title: Setup
---

# Run exercises in cmslpc

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



{% include links.md %}
