#!/bin/sh
ulimit -s unlimited
set -e
cd /uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src
export SCRAM_ARCH=el9_amd64_gcc12
source /cvmfs/cms.cern.ch/cmsset_default.sh
eval `scramv1 runtime -sh`
cd /uscms/home/yzhong/nobackup/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/runFits_0708_bare_mu_inclusive

if [ $1 -eq 0 ]; then
  combine --floatOtherPOIs 1 --expectSignal 1 -t -1 -P r --saveWorkspace --saveSpecifiedNuis all --freezeParameters MH --saveSpecifiedIndex pdfindex_cat0_2223_13TeV,pdfindex_cat1_2223_13TeV,pdfindex_cat2_2223_13TeV,pdfindex_cat3_2223_13TeV --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2 -M MultiDimFit -m 125 -d /uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine/Datacard_0708_bare_mu_inclusive.root --setParameterRanges r=0,3 -n _bestfit_syst_r
fi

