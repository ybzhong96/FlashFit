#!/bin/bash
ulimit -s unlimited
set -e
cd /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src
export SCRAM_ARCH=el9_amd64_gcc12
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal
export PYTHONPATH=$PYTHONPATH:/eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/tools:/eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/tools

export CMSSW_BASE=/eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4
python3 /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/scripts/fTest.py --xvar mass --cat cat4 --procs GGHH_kl-1p00_kt-1p00_c2-0p00 --ext bbgg_2022+2023 --inputWSDir /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/bbgg/ws_GGHH_kl-1p00_kt-1p00_c2-0p00 --weightName weight_tot --doPlots --template NGauss --nGaussMax 5 --mggBinWidth 2
