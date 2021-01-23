import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
fig= plt.figure()
ax=fig.add_axes([0,0,1,1])

# dataf=pd.DataFrame(dataf)
# print(dataf.tail(2))
# age=dataf["age"]
# m=np.std(age)
# print('the standerd deviation is %d'% m)
# sort=dataf.sort_values(by='player_height')
# sort=sort.reset_index(drop=True)
# print(sort)
# print(sort.mean())
# print(sort.describe())
# ax.bar(sort['player_name'],sort['age'])
# plt.show()
# sort.columns
# print(sort.columns)
# k=sort.loc[401:705,['player_height','player_weight']]

# print(k)
dataf= pd.read_csv('/run/media/swaraj/New Volume2/code/gui/pandas/all_seasons.csv')




"""i=0
dataf=pd.DataFrame(dataf)
k='aj'
groupped = dataf.groupby('player_name')
print(groupped)
print(groupped[['college','season']].sum() )
for keys,values in groupped:
    if keys!=k:
      print(keys,values['season'],"                        /n\n",i)
      i=i+1
    """
groupped = dataf.groupby('player_name')
player_seasons={}
player_colleges={}
for name ,df in groupped:
  season=[]
  college=[]
  weight=[]
  height=[]
  for i in range(len(df)):
    season.append(dataf.iloc[i].season)
    college.append(dataf.iloc[i].college)
    weight.append(dataf.iloc[i].player_weight)
    height.append(dataf.iloc[i].player_height)
  player_seasons[name]=season
  player_colleges[name]=college,season,height,weight
#print(player_seasons)
new_data= pd.DataFrame.from_dict(player_colleges,orient='index')
#new_data['colleges']=player_colleges
new_data.rename(columns = {'0':'colleges','1':'seasons','2':'weight','3':'height'}, inplace = True) 
new_data.columns = ['college', 'seasons', 'height','weight'] 
#new_data.to_csv('file1.csv') 
print(new_data)
