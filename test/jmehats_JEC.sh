#! /bin/bash

echo "Starting to run a series of cmsRun commands ... "
nohup cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD.root maxEvents=100000 > JECNtuple_MiniAOD.log &
nohup cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JESUncertaintyUp.root JESUncertainty=up maxEvents=100000 > JECNtuple_MiniAOD_JESUncertaintyUp.log &
nohup cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JESUncertaintyDown.root JESUncertainty=down maxEvents=100000 > JECNtuple_MiniAOD_JESUncertaintyDown.log &
nohup cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JER.root JERUncertainty=nominal maxEvents=100000 > JECNtuple_MiniAOD_JER.log &
nohup cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JERUncertaintyUp.root JERUncertainty=up maxEvents=100000 > JECNtuple_MiniAOD_JERUncertaintyUp.log &
nohup cmsRun jmehats_JEC.py print ofilename=JECNtuple_MiniAOD_JERUncertaintyDown.root JERUncertainty=down maxEvents=100000 > JECNtuple_MiniAOD_JERUncertaintyDown.log &
echo "All ntuples created successfully!"