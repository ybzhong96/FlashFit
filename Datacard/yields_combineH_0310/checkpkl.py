import numpy as np
import pandas as pd
import pickle
with open('cat0.pkl', 'rb') as handle:
    test =  pd.read_pickle(handle)
print(test)
