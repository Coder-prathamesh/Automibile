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

