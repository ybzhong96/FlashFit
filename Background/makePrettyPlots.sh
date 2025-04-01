#!/bin/bash
pushd ../Plots
for cat in {cat0,cat1,cat2}; do python3 makeMultipdfPlot.py --inputWSFile ../Background/outdir_testV_231024_2022/CMS-HGG_multipdf_${cat}_2022.root --cat ${cat} --ext testV_231024_2022 --mass 125.38 --inputSignalWSFile ../Signal/outdir_testV_231024_2022_nGaus/signalFit/output/CMS-HGG_sigfit_testV_231024_2022_nGaus_GG2HH_2022_${cat}.root; done  
popd
