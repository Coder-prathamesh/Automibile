import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot 
# Read the dataset from local computer
Cars = pd.read_csv('Automobile_data.csv')
Cars.info()

print(Cars.head())
Cars = Cars.drop(['symboling','normalized-losses','aspiration','wheel-base','width','height'],1)
print(Cars.head())
# Also the "price" column is showing object datatype. So I have changed it to float.
Cars['price']= pd.to_numeric(Cars['price'],errors='coerce')

#Data Visualization

Total = Cars.make.value_counts().to_frame()

fig,ax= plt.subplots(figsize=(12,6))
sns.barplot(x=Total.index, 
            y=Total.make,
            data= Cars)
ax.set_xticklabels(ax.get_xticklabels(),
                   rotation=45, 
                   horizontalalignment='right')
plt.show()

#Bar Plot using Pandas:

Cars_make= Cars['make'].value_counts()
Cars_make.plot(kind='bar',figsize=(12,6))

#To plot body style vs mpg (Box plot)

fig,ax= plt.subplots(figsize=(12,6))
sns.boxplot(x='body-style',y='highway-mpg',data=Cars)
#Additionally We can also specify any categorical feature for comparision
sns.boxplot(x='body-style',y='highway-mpg', hue='fuel-type',data=Cars)

# Heatmap: This graph demonstrates the the correlation between the parameters.

sns.heatmap(Cars.corr(),cmap='coolwarm')
plt.title('Correlation')
