#!/bin/bash
ulimit -s unlimited
set -e
source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=el9_amd64_gcc12
cd /uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src
eval `scramv1 runtime -sh`
cd /uscms_data/d3/yzhong/CMSSW_14_1_0_pre4/src/flashggFinalFit/Plots/SplusBModelstest_postfit/toys

itoy=$1

#Generate command
combine /uscms/home/yzhong/nobackup/CMSSW_14_1_0_pre4/src/flashggFinalFit/Plots/../Combine/runFits_0806_mu_inclusive/higgsCombine_bestfit_syst_r.MultiDimFit.mH125.root -m 125.000 -M GenerateOnly --saveWorkspace --toysFrequentist --bypassFrequentistFit -t 1 --setParameters r=-1.094 -s -1 -n _${itoy}_gen_step --snapshotName MultiDimFit

#Fit command
mv higgsCombine_${itoy}_gen_step*.root gen_${itoy}.root
combine gen_${itoy}.root -m 125.000 -M MultiDimFit -P r --floatOtherPOIs=1 --saveWorkspace --toysFrequentist --bypassFrequentistFit -t 1 --setParameters r=-1.094 -s -1 -n _${itoy}_fit_step --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_freezeDisassociatedParams --X-rtd MINIMIZER_multiMin_hideConstants --X-rtd MINIMIZER_multiMin_maskConstraints --X-rtd MINIMIZER_multiMin_maskChannels=2

#Throw command
mv higgsCombine_${itoy}_fit_step*.root fit_${itoy}.root
combine fit_${itoy}.root -m 125.000 --snapshotName MultiDimFit -M GenerateOnly --saveToys --toysFrequentist --bypassFrequentistFit -t -1 -n _${itoy}_throw_step --setParameters r=0

mv higgsCombine_${itoy}_throw_step*.root toy_${itoy}.root
rm gen_${itoy}.root fit_${itoy}.root
