import pandas as pd 
import numpy as np
i=0
f=pd.read_csv('/run/media/swaraj/New Volume2/code/gui/pandas/all_seasons.csv')
print(f)
f=f.groupby('college')
print(type(f))
print(f['player_name'])
