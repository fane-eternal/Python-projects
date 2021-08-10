#inline flag will use the appropriate backend to make
#figures appear inline in the notebook
import pandas as pd
import numpy as np

# 'plt' is an alias for the 'matplotlib.pyplot' module
import matplotlib.pyplot as plt

#import seaborn library (wrapper of matplotlib)
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/datasets/covid-19/main/data/countries-aggregated.csv', parse_dates = ['Date'])
df['Total Cases'] = df[['Confirmed', 'Recovered', 'Deaths']].sum(axis = 1)
print(df.head())
print(df.info())
