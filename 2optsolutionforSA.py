# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:22:53 2019

@author: buse
"""
import math
import numpy as np
import pandas as pd
def objFunc(p):
    N = len(x)
    cost = 0
    for i in range(0,N-1):
        xd = x[p[i]] - x[p[i+1]]
        yd = y[p[i]] - y[p[i+1]]
        dxy = math.sqrt(xd * xd + yd *yd)
        cost = cost + dxy
    return cost
def data(p,x,y):
    sehirler=[]
    with open("E:\DERSLER\Yüksek Lisans\Optimization\gr137.tsp") as b:
        locations = b.read()
        for location in locations.split("NODE_COORD_SECTION")[1:]:
            sehirler=(location.splitlines()[1:-1])
    p=[0]
    x=[]
    y=[]
    for i in sehirler:
        p.append(int(i.split(" ")[0]))
        x.append(float(i.split(" ")[1]))
        y.append(float(i.split(" ")[2]))
    return p[:-1],x,y
def city(cities):
    cities=[]
    with open("E:\DERSLER\Yüksek Lisans\Optimization\gr137.tsp") as b:
        locations = b.read()
        for location in locations.split("NODE_COORD_SECTION")[1:]:
            cities=(location.splitlines()[1:-1])
    return cities

def two_opt_python():
   
    min_change = 0
    num_cities = len(tour)
    # Find the best move
    for i in range(num_cities - 2):
        for j in range(i + 2, num_cities - 1):
            change = dist(i, j) + dist(i+1, j+1) - dist(i, i+1) - dist(j, j+1)
            
            if change < min_change:
                min_change = change
                min_i, min_j = i, j
                
                
    print(min_change)           
    # Update tour with best move
    if min_change < 0:
        tour[min_i+1:min_j+1] = tour[min_i+1:min_j+1][::-1]   
    print('Gidilen yol:',tour)   



def dist(a, b):
    """Return the euclidean distance between cities tour[a] and tour[b]."""
    return np.hypot(coords[tour[a], 0] - coords[tour[b], 0],
                    coords[tour[a], 1] - coords[tour[b], 1])

x=[]
y=[]
p=[]
sehirler=[]
sehirler=city(sehirler)
p,x,y=data(p,x,y)
#
tour= np.asarray(p)
x_array=np.asarray(x)
y_array=np.asarray(y)
#dataframe oluştur
data={'x':x_array,'y':y_array}
coords = pd.DataFrame(data)
coords=coords.to_numpy()

two_opt_python()
first_path=objFunc(p)
change_path=objFunc(tour)
print(first_path)
print(change_path)
