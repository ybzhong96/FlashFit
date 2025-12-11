#!/bin/bash
ulimit -s unlimited
set -e
cd /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src
export SCRAM_ARCH=el9_amd64_gcc12
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background
export PYTHONPATH=$PYTHONPATH:/eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/tools:/eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background/tools

/eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Background/runBackgroundScripts.sh -i /eos/home-b/bdanzi/EarlyRun3HHbbgg/2D/CMSSW_14_1_0_pre4/src/flashggFinalFit_fullexp/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/inputs/bbgg/ws_data/output_Data_13TeV_2022+2023_M125_GGHH.root -p GGHH -f cat4 --ext bbgg --catOffset 0 --fTestOnly --sigFile none --intLumi 61.457 --year 2022+2023 --isData --batch local --queue espresso --fitType mgg --massLow 100 --massHigh 180 --binWidth 2 --mggName mass --mjjName dijet_mass 
