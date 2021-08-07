#inline flag will use the appropriate backend to make
#figures appear inline in the notebook
import pandas as pd
import numpy as np

# 'plt' is an alias for the 'matplotlib.pyplot' module
import matplotlib.pyplot as plt

#import seaborn library (wrapper of matplotlib)
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/fane-eternal/test-csv/main/Database_sample.csv', sep=r'\s*,\s*',
header=0, error_bad_lines=False, engine='python')
print(df.head())
print(df.info())
rating = df.loc[:, 'rating'].values
gross_revenue = df.loc[:, 'Gross Revenue'].values
duration = df.loc[:, 'Duration (min)'].values
plt.plot(rating, duration)
