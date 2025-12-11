import ROOT

def print_dataset_contents(root_file, workspace_name, dataset_name):
    # 打开 ROOT 文件
    f = ROOT.TFile.Open(root_file)
    if not f or f.IsZombie():
        print("Error: Cannot open ROOT file!")
        return

    # 获取 RooWorkspace
    ws = f.Get(workspace_name)
    if not ws:
        print(f"Error: RooWorkspace '{workspace_name}' not found!")
        return

    # 获取 RooDataSet
    dataset = ws.data(dataset_name)
    if not dataset:
        print(f"Error: RooDataSet '{dataset_name}' not found!")
        return

    # 获取变量集
    vars = dataset.get()
    var_iter = vars.createIterator()

    # 打印变量名
    print("Variables in RooDataSet:")
    var_names = []
    var = var_iter.Next()
    while var:
        print(var.GetName(), end="\t")
        var_names.append(var.GetName())
        var = var_iter.Next()
    print("\n" + "-"*40)

    # 遍历事件
    for i in range(dataset.numEntries()):
        row = dataset.get(i)
        print(f"Entry {i}: ", end="")
        row_iter = row.createIterator()
        var_in_row = row_iter.Next()
        while var_in_row:
            print(f"{var_in_row.GetName()}={var_in_row.getVal():.6f}", end="\t")
            var_in_row = row_iter.Next()
        print()

    # 关闭文件
    f.Close()

if __name__ == "__main__":
    # 修改成你的文件名、workspace名和dataset名
    root_file = "CMS-HGG_multipdf_bbgg_cat4_2022+2023.root"
    workspace_name = "multipdf"
    dataset_name = "roodataset_data_mass_cat4"

    print_dataset_contents(root_file, workspace_name, dataset_name)

