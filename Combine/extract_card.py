def extract_category_datacard(input_card, output_card, target_cat):
    with open(input_card) as f:
        lines = f.readlines()

    header = []
    shapes = []
    obs_bin_line = None
    obs_val_line = None
    proc_bin_line = None
    proc_lines = []  # two process lines
    rate_line = None
    syst_lines = []

    section = None

    for line in lines:
        if line.startswith("imax") or line.startswith("jmax") or line.startswith("kmax"):
            # header lines
            header.append(line)
        elif line.startswith("shapes"):
            # keep only target_cat shapes
            if target_cat in line:
                shapes.append(line)
        elif line.startswith("bin") and obs_bin_line is None:
            # first bin line belongs to observation
            obs_bin_line = line
        elif line.startswith("observation") and obs_val_line is None:
            obs_val_line = line
        elif line.startswith("bin") and obs_bin_line is not None and proc_bin_line is None:
            # second bin line belongs to process/rate section
            proc_bin_line = line
            section = "proc"
        elif line.startswith("process") and section == "proc":
            proc_lines.append(line)
        elif line.startswith("rate"):
            rate_line = line
            section = None
        else:
            # systematics and anything else
            syst_lines.append(line)

    # ---- Parse observation ----
    obs_bins = obs_bin_line.strip().split()[1:]
    obs_vals = obs_val_line.strip().split()[1:]
    keep_idx = [i for i, b in enumerate(obs_bins) if target_cat in b]

    new_obs_bins = [obs_bins[i] for i in keep_idx]
    new_obs_vals = [obs_vals[i] for i in keep_idx]

    new_obs = "bin " + " ".join(new_obs_bins) + "\n"
    new_obs += "observation " + " ".join(new_obs_vals) + "\n"

    # ---- Parse process/rate ----
    proc_bins = proc_bin_line.strip().split()[1:]
    proc_procs = proc_lines[0].strip().split()[1:]
    proc_ids   = proc_lines[1].strip().split()[1:]
    rates      = rate_line.strip().split()[1:]

    keep_proc_idx = [i for i, b in enumerate(proc_bins) if target_cat in b]

    new_bin_line = "bin " + " ".join([proc_bins[i] for i in keep_proc_idx]) + "\n"
    new_proc1 = "process " + " ".join([proc_procs[i] for i in keep_proc_idx]) + "\n"
    new_proc2 = "process " + " ".join([proc_ids[i]   for i in keep_proc_idx]) + "\n"
    new_rate  = "rate "    + " ".join([rates[i]      for i in keep_proc_idx]) + "\n"

    # ---- Parse systematics ----
    new_syst = []
    for line in syst_lines:
        parts = line.strip().split()
        if len(parts) < 2:
            new_syst.append(line)
            continue
        if parts[1] in ["lnN", "shape", "lnU", "gmN"]:
            syst_name = parts[0]
            syst_type = parts[1]
            vals = parts[2:]
            new_vals = [vals[i] for i in keep_proc_idx]
            new_syst.append(f"{syst_name:<40} {syst_type:<10} {' '.join(new_vals)}\n")
        else:
            new_syst.append(line)

    # ---- Update header ----
    new_header = [
        f"imax 1  number of bins\n",
        f"jmax {len(set([proc_procs[i] for i in keep_proc_idx]))-1}  number of processes minus 1\n",
        f"kmax *  number of nuisance parameters\n"
    ]

    # ---- Write new datacard ----
    with open(output_card, "w") as f:
        f.writelines(new_header)
        f.writelines(shapes)
        f.write("\n")
        f.write(new_obs)
        f.write("\n")
        f.write(new_bin_line)
        f.write(new_proc1)
        f.write(new_proc2)
        f.write(new_rate)
        f.write("\n")
        f.writelines(new_syst)

    print(f"✅ Wrote single-category datacard: {output_card}")


# Usage example:
# extract_category_datacard("datacard.txt", "datacard_cat0.txt", "cat0_2223")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 4:
        print("Usage: python extract_card.py <input_datacard> <output_datacard> <target_category>")
    else:
        extract_category_datacard(sys.argv[1], sys.argv[2], sys.argv[3])

