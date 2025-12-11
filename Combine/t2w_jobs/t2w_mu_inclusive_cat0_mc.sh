#!/bin/bash

cd /uscms/home/yzhong/nobackup/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_cat0_mc.txt -o Datacard_cat0_mc_mu_inclusive.root -m 125 higgsMassRange=122,128 