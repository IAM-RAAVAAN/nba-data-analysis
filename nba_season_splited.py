import csv
import numpy as np
import pandas as pd
with open('/run/media/swaraj/New Volume/code/gui/pandas/all_seasons.csv','r') as all_seasons:
    seasons= csv.DictReader(all_seasons)
    k=pd.DataFrame(seasons)
    print(k)
    l={}
    j=[]
    group= k.groupby('player_name')
    for line , info in group:
        p=info['season'].sum()
        p=str(p)
        #print(line)
        for i in range(0,len(p),7):
            j.append(p[i:i+7])
        j=str(j)
        j=j.replace(','," ")
        l[line]=j
        j=[]
        #print(l.values())

    new_frame=pd.DataFrame(l,index=range(0,11145))
    print(new_frame)

    with open("nba_season.csv",'w') as new:
        fil=csv.writer(new)
        for line,info in l.items():
            fil.writerow([line,info])