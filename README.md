# Jet CMS DAS Exercise

## Introduction
This Hands on Tutorial Session (HATS) is intended to provide you with basic familiarity with jet energy corrections (JEC) as they relate to CMS. Pretty much all analyses which use jets will need to make use of JECs in some way. Additionally, analyes will probably use the systematic uncertainties for those corrections as well as the jet energy resolution (JER) scale factors and their uncertainties. A general description of the JEC and JER will be provided, as well as several example of how to apply these corrections/scale factors.

More details about pileup and its removal from jets will be given as pileup presents a large issue for current and future analyses. There are several ways to mitigate the effects of pileup and this tutorial will cover the most common of those methods.

## CMS DAS 2020 at CERN
This tutorial uses Jupyer Notebooks as a browser-based development environment at [CERN-SWAN](https://swan.cern.ch). The content of these notebooks is the same as the one at the LPC, it is just a different set up.

### Getting Started (Setup)

Go to (https://swan.cern.ch)[https://swan.cern.ch] and log in with your CERN password. After that you need to configure your environment, please use these settings:

<img src="images/SWAN_configenv.png" width="600px" />

The most important configuration is the software stack, which has to be `97a Python2`. After that click on start the session.

Once you are in `My Projects`, create a new project by clicking on the plus icon on the right part of `My Projects`. Enter the project name you like, for this example we will use `CMSDAS_jetExercise`.

### Checkout the code
Open up a terminal by clicking on the icon:

<img src="images/SWAN_terminal.png" width="600px" />

Once there, you are in your cernbox home area, and you can follow these steps:

```
cd SWAN_projects/CMSDAS_jetExercise/
wget https://raw.githubusercontent.com/cms-jet/JMEDAS/DAS2020/setup-libraries_SWAN.sh
source setup-libraries_SWAN.sh 
```
This will take a while, but basically you are setting your CMSSW environment, cloning some packages, and creating the kernel used in this exercises. If the compilation is succesful, you should see something similar to this at the end of the messages:
```
Loaded CMSSW_10_6_6 into hats-jec!
```

Note: If you'd like to set this code up to be used without Jupyter, follow the directions below. This is not necessary for the DAS or HATS exercises.

<details>
<summary>Standalone directions without Jupyter</summary>
  
  ```bash
  export SCRAM_ARCH=slc7_amd64_gcc700
  cmsrel CMSSW_10_6_6
  cd CMSSW_10_6_6/src
  cmsenv
  git clone https://github.com/cms-jet/JMEDAS.git Analysis/JMEDAS -b DAS2020
  git clone https://github.com/cms-jet/JetToolbox Analysis/JetToolbox -b jetToolbox_102X_v3
  cd Analysis/JMEDAS
  scram b -j 4
  cd test
  voms-proxy-init
  ```
</details>



## CMS DAS 2020 at the LPC
<summary>Directions for CMS DAS 2020</summary>
(also used for the LPC HATS)
  
### Getting Started (Setup)
This tutorial uses Jupyter Notebooks as a browser-based development environment at Vanderbilt. These Jupyter-based tutorials use a pre-configured Jupyter service usable by all CMS members.

#### Connect to Jupyter 
To log in, access the [login](https://jupyter.accre.vanderbilt.edu/) page and login using your CERN credentials. Once you successfully connect, you should see the following front page

<img src="jupyter-login.png" width="600px" />

The two most important buttons are
  * The `new` button, which lets you open a terminal or start a new Jupyter notebook.
  * The `control panel` button, which lets you shut down your notebook once you're done. It's helpful to do this to free up resources for other users.

#### Upload Grid Certificates
We will copy your grid certificates from the LPC cluster, to do this, open the front page (shown above), and click the `New` box at the top right, then the `Terminal` option.

This will open a new tab with a bash terminal. Execute the following commands (following the appropriate prompts) to copy your certificate from the LPC to Jupyter (**note**: replace `username` with your `FNAL` username!)

The following command will prompt you for your FNAL password
```bash
kinit username@FNAL.GOV
rsync -rLv username@cmslpc-sl7.fnal.gov:.globus/ ~/.globus/
chmod 755 ~/.globus
chmod 600 ~/.globus/*
kdestroy
```

#### Initialize Your Proxy at every Login!
If you have a password on your grid certificate, you'll need to remember to execute the following in a terminal *each time you log in to Jupyter*. Similar to the LPC cluster, you will get a new host at each logon, and the new host won't have your old credentials.

Each time you log in, open a terminal and execute:
```bash
voms-proxy-init -voms cms -valid 192:00
```

#### Checkout the code
Open up a terminal and run the following command from your home area:
```
wget https://raw.githubusercontent.com/cms-jet/JMEDAS/DAS2020/setup-libraries.ipynb
```

Go back to your Jupyter browser (Home) page and open/run(double-click) the newly downloaded notebook  (setup-libraries.ipynb - downloaded just recently - only one cell to run). This will checkout the code and setup your environment for future use. After running setup-libraries.ipynb, choose "File... Close and Halt". Then you can continue on to the Tutorial section (below).


Note: If you'd like to set this code up to be used without Jupyter, follow the directions below. This is not necessary for the DAS or HATS exercises.
<details>
<summary>Standalone directions without Jupyter</summary>
  
  ```bash
  export SCRAM_ARCH=slc7_amd64_gcc700
  cmsrel CMSSW_10_6_6
  cd CMSSW_10_6_6/src
  cmsenv
  git clone https://github.com/cms-jet/JMEDAS.git Analysis/JMEDAS -b DAS2020
  git clone https://github.com/cms-jet/JetToolbox Analysis/JetToolbox -b jetToolbox_102X_v3
  cd Analysis/JMEDAS
  scram b -j 4
  cd test
  voms-proxy-init
  ```
</details>
  
### Tutorial
Once you've completed the setup instructions, change to the directory `~/CMSSW_10_6_6/src/Analysis/JMEDAS`. Information on the separate tutorial can be found in the "notebooks" subdirectory.

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
