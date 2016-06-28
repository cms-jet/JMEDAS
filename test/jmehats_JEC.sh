#! /bin/bash

echo "Starting to run a series of cmsRun commands ... "
cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD.root
cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JESUncertaintyUp.root JESUncertainty=up
cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JESUncertaintyDown.root JESUncertainty=down
cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JER.root JERUncertainty=nominal
cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JERUncertaintyUp.root JERUncertainty=up
cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JERUncertaintyDown.root JERUncertainty=down
echo "All ntuples created successfully!"