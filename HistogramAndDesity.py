#python program for histogram and Density plot

""" Histogram and Density plots are a good way to analyze continous variables."""


#Histogram Program

import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd
from pyparsing import alphas
import seaborn as sns 
sns.set()

data=np.random.multivariate_normal([0,0],[[5,2],[2,2]],size=2000)
data=pd.DataFrame(data,columns=['x','y'])
plt.hist(data['x'],alpha=0.5)
plt.hist(data['y'],alpha=0.5)
plt.show()


#Density Program

sns.kdeplot(data['x'],shade=True)
sns.kdeplot(data['y'],shade=True)
plt.show()