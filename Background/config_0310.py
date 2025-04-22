#Config file: options for bkg fitting
_year ='2022'
backgroundScriptCfg = {
  # Setup
  'inputWS': '/uscms_data/d3/yzhong/2223_0417_sample/ws/Data_output_M125.root',
  'cats':'cat0,cat1,cat2', # if auto: inferred automatically from (0) workspace
  'ext':'test_0417_%s'%_year,
  'catOffset':0,
  'year':'2022',   # Use 'combined' if merging all years: not recommended    
  # Job submission options
  'batch':'local',  # ['condor','SGE','IC','local']
  'queue':'espresso'
}
