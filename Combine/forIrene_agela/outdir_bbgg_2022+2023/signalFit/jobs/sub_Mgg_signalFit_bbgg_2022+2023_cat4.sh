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
python3 /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Signal/scripts/signalFit.py --xvar mass --inputWSDir /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/bbgg/ws_GGHH_kl-1p00_kt-1p00_c2-0p00 --ext bbgg_2022+2023 --proc GGHH_kl-1p00_kt-1p00_c2-0p00 --cat cat4 --year 2022+2023 --analysis bbgg --massPoints 125 --scales 'FNUF,Material,ScaleEB2GIJazZ,ScaleEE2GIJazZ,jecsyst' --scalesCorr '' --scalesGlobal '' --smears 'Smearing2GIJazZ,jersyst' --weightName weight_tot --doPlots --replacementThreshold 0 --template DCB --mggLow 100 --mggHigh 180 --mggBinWidth 2

