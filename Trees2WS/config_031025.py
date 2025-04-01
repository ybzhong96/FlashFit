# Input config file for running trees2ws

trees2wsCfg = {

  # Name of RooDirectory storing input tree
  'inputTreeDir':'',
  
  'mainVars':["CMS_hgg_mass","eventWeight"],#"dZ","weight_*"], # Var for the nominal RooDataSets
  ### ^^^^ IF YOU CHANGE THE EVENT WEIGHT VAR NAME HERE, ALSO CHANGE IN TREE2WS.PY ^^^^^
  
  'dataVars':["CMS_hgg_mass","weight"], # Vars to be added for data
  'stxsVar':'',
  'systematicsVars':["CMS_hgg_mass","weight"], # Variables to add to sytematic RooDataHists
  'theoryWeightContainers':{},

  # List of systematics: use string YEAR for year-dependent systematics
  'systematics':'',#["Scale","Smearing"],

  # Analysis categories: python list of cats or use 'auto' to extract from input tree
  'cats': ['cat0', 'cat1', 'cat2', 'cat3']

}
