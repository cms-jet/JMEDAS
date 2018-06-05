# JME POG CMS Data Analysis School (CMSDAS) exercise
(also used for HATs@LPC)

## DAS
<details>
<summary>Directions for CMSDAS 2018</summary>
  
  ```bash
  cmsrel CMSSW_8_0_25
  cd CMSSW_8_0_25/src
  git clone https://github.com/cms-jet/JMEDAS.git Analysis/JMEDAS
  git clone https://github.com/cms-jet/JetToolbox Analysis/JetToolbox -b jetToolbox_80X
  cd Analysis/JMEDAS
  scram b -j 10
  cd test
  voms-proxy-init
  python jmedas_fwlite.py --files qcdflat.txt  --outname qcdflat.root
  ```
  
  Later in the exercise we will do:

  ```bash
  cr ClusterWithToolboxAndMakeHistos.py
  ```
</details>

## Pileup & Jet Energy Correction HATS@LPC
### Introduction
This Hands on Tutorial Session (HATS) is intended to provide you with basic familiarity with jet energy corrections (JEC) as they relate to CMS. Pretty much all analyses which use jets will need to make use of JECs in some way. Additionally, analyes will probably use the systematic uncertainties for those corrections as well as the jet energy resolution (JER) scale factors and their uncertainties. A general description of the JEC and JER will be provided, as well as several example of how to apply these corrections/scale factors.

More details about pileup and its removal from jets will be given as pileup presents a large issue for current and future analyses. There are several ways to mitigate the effects of pileup and this tutorial will cover the most common of those methods.

### Getting Started
The setup/configuration of this HATS tutorial is documented at the [HATSatLPCSetup TWiki](https://twiki.cern.ch/twiki/bin/view/CMS/HATSatLPCSetup2018#JupyterSetup). This tutorial's repository is https://github.com/cms-jet/JMEDAS.git

Note: If you'd like to set this code up to be used without Jupyter, follow the directions below. This is not necessary for the HATS exercises.
<details>
<summary>Standalone directions without Jupyter</summary>
  
  ```bash
  cmsrel CMSSW_9_4_8
  cd CMSSW_9_4_8/src
  git clone https://github.com/cms-jet/JMEDAS.git Analysis/JMEDAS
  git clone https://github.com/cms-jet/JetToolbox Analysis/JetToolbox -b jetToolbox_94X
  cd Analysis/JMEDAS
  scram b -j 4
  cd test
  voms-proxy-init
  ```
  
</details>

### Tutorial
Once you've completed the setup instructions, information on the separate tutorial can be found in the `test` subdirectory.
