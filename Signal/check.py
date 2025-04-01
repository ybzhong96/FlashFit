import ROOT

# Open the ROOT file
file = ROOT.TFile("/uscms_data/d3/yzhong/ws_GG2HH/Signal_output_M125_GG2HH.root")
#file = ROOT.TFile("/uscms_data/d3/idutta/HHbbgg_Run3_fits/CMSSW_14_1_0_pre4/src/flashggFinalFit/Trees2WS/input_testV_231024/ws_GG2HH/Signal_output_M125_GG2HH.root")
# Access the TDirectoryFile
directory = file.Get("tagsDumper")
if not directory:
    print("tagsDumper not found in the file")
else:
    print("\n== List of keys in tagsDumper ==")
    directory.ls()

    # Access the RooWorkspace
    workspace = directory.Get("cms_hgg_13TeV")
    if workspace:
        print("\n== List of variables in cms_hgg_13TeV ==")
        vars = workspace.allVars()
        vars.Print("V")  # "V" prints detailed information about variables
    else:
        print("Workspace 'cms_hgg_13TeV' not found.")

# Close the file
file.Close()
