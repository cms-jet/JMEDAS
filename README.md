JMEDAS
======

JME POG CMS Data Analysis School (CMSDAS) exercise



`cmsrel CMSSW_8_0_25`

`cd CMSSW_8_0_25/src`

`git clone https://github.com/cms-jet/JMEDAS.git Analysis/JMEDAS`

`git clone https://github.com/cms-jet/JetToolbox Analysis/JetToolbox -b jetToolbox_80X`

`cd Analysis/JMEDAS`

`scram b -j 10`

`cd test`

`voms-proxy-init`

`python jmedas_fwlite.py --files qcdflat.txt  --outname qcdflat.root`

Later in the exercise we will do:

`cr ClusterWithToolboxAndMakeHistos.py`
