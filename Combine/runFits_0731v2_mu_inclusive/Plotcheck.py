import ROOT
f = ROOT.TFile("higgsCombine_bestfit_syst_r.MultiDimFit.mH125.root")
w = f.Get("w")
#w.Print("v")
n_bins = 80
binning = ROOT.RooFit.Binning(n_bins,100,180)

data_cat = w.data("data_obs").reduce("CMS_channel==CMS_channel::cat0_2223")
can = ROOT.TCanvas()
plot = w.var("CMS_hgg_mass").frame()
data_cat.plotOn( plot, binning )

# Load the S+B model
sb_model = w.pdf("model_s").getPdf("cat0_2223")

# Prefit
#sb_model.plotOn(plot, ROOT.RooFit.LineColor(2), ROOT.RooFit.Name("prefit") )

# Postfit
w.loadSnapshot("MultiDimFit")
sb_model.plotOn(plot, ROOT.RooFit.LineColor(4), ROOT.RooFit.Name("postfit") )
r_bestfit = w.var("r").getVal()



plot.Draw()

leg = ROOT.TLegend(0.55,0.6,0.85,0.85)
#leg.AddEntry("prefit", "Prefit S+B model (r=1.00)", "L")
leg.AddEntry("postfit", "Postfit S+B model (r=%.2f)"%r_bestfit, "L")
leg.Draw("Same")

can.Update()
can.SaveAs("sb_model.png")
