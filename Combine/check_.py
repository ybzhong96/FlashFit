import ROOT

def check_pdf_norm(rootfile_path, workspace_name, pdf_name, observable_name, mass_range=(100, 180)):

    f = ROOT.TFile.Open(rootfile_path)
    if not f or f.IsZombie():
        raise IOError(f"Cannot open file {rootfile_path}")
    
    ws = f.Get(workspace_name)
    if not ws:
        raise KeyError(f"Workspace '{workspace_name}' not found in file.")
    

    pdf = ws.pdf(pdf_name)
    mass = ws.var(observable_name)
    norm_val0=pdf.getNorm()

    if not pdf or not mass:
        raise KeyError("PDF or observable not found in workspace.")


    mass.setRange("normRange", mass_range[0], mass_range[1])

    
    norm_val = pdf.getNorm(ROOT.RooArgSet(mass))
    integral_val = pdf.createIntegral(ROOT.RooArgSet(mass), ROOT.RooFit.NormSet(ROOT.RooArgSet(mass)),
                                      ROOT.RooFit.Range("normRange")).getVal()

    print(f"--- PDF: {pdf_name} ---")
    print(f"Normalization mass (getNorm): {norm_val:.6f}")
    print(f"Norm: {norm_val0: .6f} ")
    print(f"Integral over mass [{mass_range[0]}, {mass_range[1]}]: {integral_val:.6f}")
    print(f"Expected total (norm integral): {norm_val * integral_val:.6f}")
    print("-----------------------------------\n")
    
    f.Close()

check_pdf_norm(
    rootfile_path="./Models/signal/CMS-HGG_sigfit_GG2HH_cat0_2223.root",
    workspace_name="wsig_13p6TeV",
    pdf_name="hggpdfsmrel_GG2HH_2223_cat0_13p6TeV",
    observable_name="CMS_hgg_mass"
)

check_pdf_norm(
    rootfile_path="./Models/singleH_old/CMS-HGG_sigfit_H60_cat0_2022.root",
    workspace_name="wsig_13p6TeV",
    pdf_name="hggpdfsmrel_GG2HH_2022_cat0_13p6TeV",
    observable_name="CMS_hgg_mass"
)

