##### BARPLOT:

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


##### BARPLOT with annotations
data = pd.read_csv('C:/Users/Hassan hasan/Downloads/imf_data.csv')

data = data.sort_values(['year'], ascending = 0)
g = data.head(5)

#Resizing frame for plotting
fig_size = plt.rcParams["figure.figsize"]
fig_size[0] = 10
fig_size[1] = 8
plt.rcParams["figure.figsize"] = fig_size

groupedvalues = data.groupby(('CountryName'), as_index = 0).sum().sort_values(['year'], ascending = 0)
g=groupedvalues.head(5)

pt = sns.barplot(x=g['CountryName'].head(5),y=g['year'],data=g)
pt.set(xlabel='Country Name', ylabel='Unemployment Rate')

for p in pt.patches:
    pt.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, 9), 
                   textcoords = 'offset points')


######################### Anotations alignment (labels inside the bar) #################################


pt = sns.barplot(x=g['CountryName'].head(5),y=g['year'],data=g)
pt.set(xlabel='Country Name', ylabel='Unemployment Rate')

for p in pt.patches:
    pt.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, -12), 
                   textcoords = 'offset points')
    

######################## Changing Colour Palett to Pastel Colours ###############################


pt = sns.barplot(x=g['CountryName'].head(5),y=g['year'],data=g,palette=("Set2"))
pt.set(xlabel='Country Name', ylabel='Unemployment Rate')

for p in pt.patches:
    pt.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, -12), 
                   textcoords = 'offset points')



######################## Changing Colour Palett of bars and labels ###############################




pt = sns.barplot(x=g['CountryName'].head(5),y=g['year'],data=g, palette =("rocket"))

pt.set(xlabel='Country Name', ylabel='Unemployment Rate')

for p in pt.patches:
    pt.annotate(format(p.get_height(), '.1f'), 
                   (p.get_x() + p.get_width() / 2., p.get_height()), 
                   ha = 'center', va = 'center', 
                   xytext = (0, -12), 
                   textcoords = 'offset points', color = "#FFFFFF", fontsize=15)