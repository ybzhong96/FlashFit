#!/bin/bash
ulimit -s unlimited
set -e
cd /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src
export SCRAM_ARCH=el9_amd64_gcc12
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background
export PYTHONPATH=$PYTHONPATH:/eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/tools:/eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background/tools

python3 /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background/scripts/packageBackground.py --cat cat4 --outputExt packaged --massPoints 125 --fitType mgg --exts tth,vh,ggh --mergeYears
