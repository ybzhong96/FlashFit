import pandas as pd
import pickle as pkl
with open("cat0.pkl", "rb") as fpkl:
    data = pkl.load(fpkl)
print(data.columns)
print(data.iloc[0])
print("===================================================================")
#with open("cat1.pkl", "rb") as fpkl:
#    data = pkl.load(fpkl)
#print(data.iloc[0])
#print("===================================================================")
#with open("cat2.pkl", "rb") as fpkl:
#    data = pkl.load(fpkl)
#print(data.iloc[0])


