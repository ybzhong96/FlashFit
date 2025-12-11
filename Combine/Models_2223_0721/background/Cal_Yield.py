import ROOT

# Open the ROOT file
file = ROOT.TFile.Open("CMS-HGG_multipdf_cat0_2223.root")  # Replace with your actual file name

# Load the workspace
ws = file.Get("multipdf")  # Replace with actual workspace name if different

# Check if workspace is loaded
if not ws:
    raise RuntimeError("Workspace not found in the file.")

# Get the lau1 PDF from the workspace
lau1_pdf = ws.pdf("env_pdf_0_2223_13TeV_lau1")

if not lau1_pdf:
    raise RuntimeError("lau1 PDF not found in the workspace.")

# Print info
print("lau1 PDF:", lau1_pdf)

# Extract components of the RooAddPdf
components = lau1_pdf.getComponents()
components.Print()

# Retrieve and print relevant parameters
params = [
    "env_pdf_0_2223_13TeV_lau1_l1",
    "env_pdf_0_2223_13TeV_lau1_recursive_fraction_env_pdf_0_2223_13TeV_lau1_powl1_2",
    "env_pdf_0_2223_13TeV_lau1_pow0",
    "env_pdf_0_2223_13TeV_lau1_powl1"
]

print("\nParameters of lau1:")
for pname in params:
    param = ws.var(pname)
    if not param:
        param = ws.function(pname)  # try as function
    if param:
        print(f"{pname} = {param.getVal()}")
    else:
        print(f"{pname} not found.")
