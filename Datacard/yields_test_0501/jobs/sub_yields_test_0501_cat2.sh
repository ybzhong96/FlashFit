#!/bin/bash
ulimit -s unlimited
set -e
cd /uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src
export SCRAM_ARCH=el9_amd64_gcc12
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src/flashggFinalFit/Datacard
export PYTHONPATH=$PYTHONPATH:/uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src/flashggFinalFit/tools:/uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src/flashggFinalFit/Datacard/tools

python3 /uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src/flashggFinalFit/Datacard/makeYields.py --cat cat2 --procs auto --ext test_0501 --mass 125 --inputWSDirMap 2022=/uscms/home/yzhong/nobackup/2223_0424_sample/ws_GG2HH/ --sigModelWSDir ./Models/signal --sigModelExt packaged --bkgModelWSDir ./Models/background --bkgModelExt multipdf  --skipCOWCorr --systWeightScheme accEff --doSystematics
