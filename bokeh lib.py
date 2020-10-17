import numpy as np
from bokeh.plotting import figure, output_file, show
import pandas as pd

data = pd.read_csv('D:/Github/bokeh_sample.csv')
x = [str(x) for x in data['Year']]
y = [str(y) for y in data['Value']] 
chart = figure(title="First Line Plot", x_axis_label='x', y_axis_label='y')

#plot the line graph on the figure
chart.line(x, y, legend_label="Counts", line_width=2)
# show the results
show(chart)


#multiple lines plot

import numpy as np
from bokeh.plotting import figure, output_file, show
import pandas as pd
from bokeh.charts import Scatter

data = pd.read_csv('D:/Github/bokeh_sample.csv')
x = [str(x) for x in data['Year']]
y = [str(y) for y in data['Value']] 
y2 = [str(y2) for y2 in data['Value2']] 
chart = figure(title="Multiple Lines Plot", x_axis_label='x', y_axis_label='y')

#plot the line graph on the figure
chart.line(x, y, legend_label="Counts", line_width=4)
chart.line(x, y2, legend_label="Counts", line_color = 'purple',line_width=4)

# show the results
show(chart)


#scatter plot


import numpy as np
from bokeh.plotting import figure, output_file, show
import pandas as pd
#from bokeh.plotting import Scatter



data = pd.read_csv('D:/Github/bokeh_sample.csv')

x = [str(x) for x in data['Year']]
y = [str(y) for y in data['Value']] 
p = figure(plot_width=400, plot_height=400)
p.circle(x, y, size=20, color="navy", alpha=0.5)
show(p)


#Area Plot

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show

output_file("varea_stack.html")

source = ColumnDataSource(data=dict(
    x=[1, 2, 3, 4, 5],
    y1=[1, 2, 4, 3, 4],
    y2=[1, 4, 2, 2, 3],
))
p = figure(plot_width=400, plot_height=400)

p.varea_stack(['y1', 'y2'], x='x', color=("purple", "pink"), source=source)

show(p)


 #stacked bar graph

import numpy as np
from bokeh.plotting import figure, output_file, show
import pandas as pd
from bokeh.palettes import PiYG, Category20, PuBu
#from bokeh.plotting import Scatter
from bokeh.models import ColumnDataSource, Label, LabelSet



data = pd.read_csv('D:/Github/bokeh_sample.csv')

x = [str(x) for x in data['Year']]
y = [str(y) for y in round(data['Value'],2)] 

source = ColumnDataSource(data=dict(
    x=data['Year'],
    y=round(data['Value'])
))
p = figure(plot_width=800, plot_height=600)

output_file("stacked_bar.html")

labels = LabelSet( x= 'x' , y= 'y', text= 'y', level='glyph', source = source)

p.vbar(source = source,x = 'x', top = 'y' , width = 0.5,color=PuBu[7][2])

p.add_layout(labels)
show(p)