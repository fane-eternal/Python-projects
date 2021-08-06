#inline flag will use the appropriate backend to make
#figures appear inline in the notebook
import pandas as pd
import numpy as np

# 'plt' is an alias for the 'matplotlib.pyplot' module
import matplotlib.pyplot as plt

#import seaborn library (wrapper of matplotlib)
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/fane-eternal/test-csv/main/Database_sample.csv')
print(df.head())
print(df.info())
