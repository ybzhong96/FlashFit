# Python file to store systematics: for STXS analysis

# Comment out all nuisances that you do not want to include

# THEORY SYSTEMATICS:

# For type:constant
#  1) specify same value for all processes
#  2) define process map json in ./theory_uncertainties (add process names where necessary!)

# For type:factory
# Tier system: adds different uncertainties to dataframe
#   1) shape: absolute yield of process kept constant, shape effects i.e. calc migrations across cats
#   2) ishape: as (1) but absolute yield for proc x cat is allowed to vary
#   3) norm: absolute yield of production mode (s0) kept constant but migrations across sub-processes e.g. STXS bins.Same value in each category.
#   4) inorm: as (3) but absolute yield of production mode (s0) can vary
#   5) inc: variations in production mode (s0), same value for each subprocess in each category
# Relations: shape = ishape/inorm
#            norm  = inorm/inc
# Specify as list in dict: e.g. 'tiers'=['inc','inorm','norm','ishape','shape']

theory_systematics = [
                # Normalisation uncertainties: enter interpretations
                {'name':'BR_hgg','title':'BR_hgg', 'proc': 'all','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"0.9791/1.0205"},
                {'name':'BR_hbb','title':'BR_hbb', 'proc': 'split','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':{'GG2HH':'0.9874/1.0124', 'VBFHH':'0.9874/1.0124'}},
                {'name':'QCDscale_ggH','title':'QCDscale_ggH', 'proc':'GG2H', 'type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'1.039'},
                {'name':'QCDscale_qqH','title':'QCDscale_qqH', 'proc':'VBFH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'0.997/1.004'},
                {'name':'QCDscale_VH','title':'QCDscale_VH', 'proc':'VH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'0.984/1.0179'},
                {'name':'QCDscale_ttH','title':'QCDscale_ttH','proc':'TTH', 'type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'0.908/1.058'},
                {'name':'QCDscale_bbH','title':'QCDscale_bbH','proc':'BBH', 'type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'0.761/1.201'},
                {'name':'QCDscale_qqHH','title':'QCDscale_qqHH','proc':'VBFHH', 'type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'0.9996/1.0003'},
                {'name':'pdf_Higgs_ggHH','title':'pdf_Higgs_ggHH','proc':'GG2HH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'1.03'},
                {'name':'pdf_Higgs_qqHH','title':'pdf_Higgs_qqHH','proc':'VBFHH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'1.021'},
                {'name':'pdf_Higgs_ttH','title':'pdf_Higgs_ttH','proc':'TTH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'1.03'},
                {'name':'pdf_Higgs_qqbar','title':'pdf_Higgs_qqbar','proc':'split','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':{'VBFH':'1.021','VH':'1.0154'}},
                {'name':'pdf_Higgs_gg','title':'pdf_Higgs_gg','proc':'GG2H','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'1.019'},
                {'name':'alpha_s','title':'alpha_s', 'proc':'split', 'type':'constant','prior':'lnN','correlateAcrossYears':1, 'value': {'GG2H':'1.026', 'VBFH':'1.005', 'VH':'1.009', 'TTH':'1.02'}},
                {'name': 'THU_HH','title':'THU_HH','proc':'GG2HH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'0.77/1.06'},
                {'name': 'bbH_norm_ggH','title':'bbH_norm_ggH','proc':'GG2H','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'1.5'},
                {'name': 'bbH_norm_qqH','title':'bbH_norm_qqH','proc':'VBFH','type':'constant','prior':'lnN','correlateAcrossYears':1,'value':'1.5'}
             #   {'name':'weight_LHEScale_0','title':'CMS_LHEScale','type':'factory','prior':'lnN','correlateAcrossYears':1}, 
             #   {'name':'weight_LHEScale_1','title':'CMS_hgg_scaleWeight_1','type':'factory','prior':'lnN','correlateAcrossYears':1},
             #   {'name':'weight_LHEScale_2','title':'CMS_hgg_scaleWeight_2','type':'factory','prior':'lnN','correlateAcrossYears':1}, #Unphysical
             #   {'name':'weight_LHEScale_3','title':'CMS_hgg_scaleWeight_3','type':'factory','prior':'lnN','correlateAcrossYears':1},
             #   {'name':'weight_LHEScale_4','title':'CMS_hgg_scaleWeight_4','type':'factory','prior':'lnN','correlateAcrossYears':1}, # nominal weight
             #   {'name':'weight_LHEScale_5','title':'CMS_hgg_scaleWeight_5','type':'factory','prior':'lnN','correlateAcrossYears':1}, 
             #   {'name':'weight_LHEScale_6','title':'CMS_hgg_scaleWeight_6','type':'factory','prior':'lnN','correlateAcrossYears':1}, #Unphysical
             #   {'name':'weight_LHEScale_7','title':'CMS_hgg_scaleWeight_7','type':'factory','prior':'lnN','correlateAcrossYears':1},
             #   {'name':'weight_LHEScale_8','title':'CMS_hgg_scaleWeight_8','type':'factory','prior':'lnN','correlateAcrossYears':1}
                # Shape uncertainties: enter direct XS measurements
                # Shape uncertainties: enter direct XS measurements
                # Scale weights grouping is defined in makeDatacard.py
                # For some reason, the name is saved only as `Scal`, not `Scale`, do not ask me why
                # Comment out the nominal weight here as it does not contain any `tiers`, so it would fail in `makeDatacard.py``
                # The scheme below is valid for v13, you need to explicitly check the nanoAOD documentation to validate your setup

              
                ]
# PDF weight
#for i in range(1,101): theory_systematics.append( {'name':'weight_LHEPdf_%g'%i, 'title':'CMS_hgg_pdfWeight_%g'%i, 'type':'factory','prior':'lnN','correlateAcrossYears':1} )

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# EXPERIMENTAL SYSTEMATICS
# correlateAcrossYears = 0 : no correlation
# correlateAcrossYears = 1 : fully correlated
# correlateAcrossYears = -1 : partially correlated

experimental_systematics = [
               {'name':'lumi_13p6TeV_2223','title':'lumi_13p6TeV_2223','proc':'all', 'type':'constant','prior':'lnN','correlateAcrossYears':1,'value':"1.014"},
               # weight_*
               {'name':'bTagSF_sys_cferr2','title':'CMS_btag_cferr2','type':'factory','prior':'lnN','correlateAcrossYears':1},
            #   {'name':'bTagSF_sys_jes','title':'CMS_btag_jes','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'bTagSF_sys_hf','title':'CMS_btag_HF','type':'factory','prior':'lnN','correlateAcrossYears':1},
           
               {'name':'TriggerSF','title':'CMS_hgg_TriggerWeight','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'ElectronVetoSF','title':'CMS_hgg_electronVetoSF','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'bTagSF_sys_lfstats2', 'title':'CMS_btag_lfstats2','type':'factory','prior':'lnN','correlateAcrossYears':1},
                
               {'name':'bTagSF_sys_hfstats1', 'title':'CMS_btag_hfstats1','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'PreselSF', 'title':'CMS_hgg_PreselSF','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'Pileup', 'title':'CMS_pileup','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'bTagSF_sys_lfstats1', 'title':'CMS_btag_lfstats1','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'bTagSF_sys_hfstats2', 'title':'CMS_btag_hfstats2','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'bTagSF_sys_cferr1', 'title':'CMS_btag_cferr1','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name':'bTagSF_sys_lf', 'title':'CMS_btag_LF','type':'factory','prior':'lnN','correlateAcrossYears':1},
              # hist
               {'name': 'JEC22', 'title':'CMS_scale_j_2022','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name': 'JER22', 'title':'CMS_res_j_2022','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name': 'JEC23', 'title':'CMS_scale_j_2023','type':'factory','prior':'lnN','correlateAcrossYears':1},
               {'name': 'JER23', 'title':'CMS_res_j_2023','type':'factory','prior':'lnN','correlateAcrossYears':1}
              # {'name': 'FNUF', 'title':'CMS_FNUF','type':'factory','prior':'lnN','correlateAcrossYears':1},
              # {'name': 'Material', 'title':'CMS_Materials','type':'factory','prior':'lnN','correlateAcrossYears':1},
             #  {'name': 'LHEScale', 'title':'CMS_QCD_scaleWeight','type':'factory','prior':'lnN','correlateAcrossYears':1},
             #  {'name': 'LHEPdf', 'title':'CMS_QCD_pdf','type':'factory','prior':'lnN','correlateAcrossYears':1}
               ]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Shape nuisances: effect encoded in signal model
# mode = (other,scalesGlobal,scales,scalesCorr,smears): match the definition in the signal models

signal_shape_systematics = [
                {'name':'EBScale','title':'EBScale','type':'signal_shape','mode':'scales','mean':'0.0','sigma':'1.0'},  
                {'name':'EEScale','title':'EEScale','type':'signal_shape','mode':'scales','mean':'0.0','sigma':'1.0'},
                {'name':'Smearing','title':'Smearing','type':'signal_shape','mode':'smears','mean':'0.0','sigma':'1.0'},
                {'name':'FNUF', 'title':'CMS_FNUF','type':'signal_shape','mode':'scales','mean':'0.0','sigma':'1.0'},
                {'name':'Material', 'title':'CMS_Materials','type':'signal_shape','mode':'scales','mean':'0.0','sigma':'1.0'}
                #{'name':'NonLinearity','title':'NonLinearity','type':'signal_shape','mode':'scalesGlobal','mean':'0.0','sigma':'0.002'},
                #{'name':'Geant4','title':'Geant4','type':'signal_shape','mode':'scalesGlobal','mean':'0.0','sigma':'0.0005'}
              ]
