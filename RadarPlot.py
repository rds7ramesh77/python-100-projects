#Python program for Radar Plot 

""" A radar plot is also know as a spider plot or a star plot.

It is used to display multivariate data as a two-dimensional visualization of quantitative featues that are represented on axes coming from the centre.
"""

from matplotlib.pyplot import figure
import plotly.express as px  
import pandas as pd  

data=pd.DataFrame(dict(keys=[10,20,30,40,50],values=["Labor cost","Manu Cost","promotion cost","Selling cost","Next Cost"]))

figure=px.line_polar(data,r='keys',theta='values',line_close=True)
figure.update_traces(fill="toself")
figure.show()


#Remember Dash Plotly pip install dash