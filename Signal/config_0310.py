# Config file: options for signal fitting

_year = '2224'

signalScriptCfg = {
  # Setup
  'inputWSDir': '/uscms_data/d3/yzhong/2224_0925/ws_SingleH/',
  'procs':'auto', # if auto: inferred automatically from filenames
  'cats':'cat0,cat1,cat2', # if auto: inferred automatically from (0) workspace
  'ext':'H_0925_%s'%_year,#_%s_nGaus'%_year,
  'analysis':'0310', # To specify which replacement dataset mapping (defined in ./python/replacementMap.py)
  'year':'%s'%_year, # Use 'combined' if merging all years: not recommended
  'massPoints':'125',
  'xvar':'CMS_hgg_mass',
 # 'skipVertexSplit': '--skipVertexScenarioSplit', #For HH searches, skip this if you are forming single Hgg with split vertex
    #Photon shape systematics  
  'scales':'EBScale,EEScale,FNUF,Material', # separate nuisance per year
  'scalesCorr':'', # correlated across years
  'scalesGlobal':'', # affect all processes equally, correlated across years
  'smears':'Smearing', # separate nuisance per year

  # Job submission options
  'batch':'local', # ['condor','SGE','IC','local']
  'queue':'espresso'

}
