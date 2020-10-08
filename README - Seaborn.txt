Starting with the brief intro of Seaborn, Its an open source Python library used for data visualization. It has a vast pool of different graphs from bar chart to heatmaps.

I'll try to cover most commonly used charts.

Install Seaborn package by writing following command on your Anaconda interface

pip install seaborn

OR
conda install seaborn

Then We need to import necessary libraries.

import numpy as np import pandas as pd import seaborn as sns import matplotlib.pyplot as plt

Then we will read our dataset using pandas. The dataset which I am using is a time series IMF dataset that can be found on their official web https://data.imf.org/

data = pd.Read_csv('imf_data.csv') data.head()

In the next few files I will be sharing basic graphs made by seaborn library.