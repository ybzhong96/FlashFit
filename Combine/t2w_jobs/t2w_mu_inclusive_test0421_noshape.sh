#!/bin/bash

cd /uscms/home/yzhong/nobackup/CMSSW_14_1_0_pre4/src/flashggFinalFit/Combine

eval `scramv1 runtime -sh`

text2workspace.py Datacard_test0421_noshape.txt -o Datacard_test0421_noshape_mu_inclusive.root -m 125 higgsMassRange=122,128 