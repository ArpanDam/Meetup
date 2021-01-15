# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 20:34:14 2020

@author: HP
"""


import pickle
import math
import numpy as np
import json 
import numpy as np
from scipy.stats import entropy
from math import log, e
import pandas as pd
from math import radians, cos, sin, asin, sqrt

elat=pickle.load(open("elat","rb"))

elon=pickle.load(open("elon","rb"))

groupjoin=pickle.load(open("groupjoin","rb"))

egroup=pickle.load(open("egroup","rb"))

group_event=pickle.load(open("new_grp_event","rb"))


dict_to_store_groupidwith_average_event_distance={}

def distance(lat1, lat2, lon1, lon2): 
      
    # The math module contains a function named 
    # radians which converts from degrees to radians. 
    lon1 = radians(lon1) 
    lon2 = radians(lon2) 
    lat1 = radians(lat1) 
    lat2 = radians(lat2) 
       
    # Haversine formula  
    dlon = lon2 - lon1  
    dlat = lat2 - lat1 
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
  
    c = 2 * asin(sqrt(a))  
     
    # Radius of earth in kilometers. Use 3956 for miles 
    r = 6371
       
    # calculate the result 
    return(c * r) 


for key in group_event:
    list1=[]
    for i in range(len(group_event[key])):
        list1.append(group_event[key][i][0])
    k=0
    list_lat=[]
    list_lon=[]
    
    for k in range(len(list1)):
        try:
            list_lat.append(elat[list1[k]])
            list_lon.append(elon[list1[k]])
        except:
            print("No even found")
    m=0
    dis_sum=0
    for m in range(len(list_lat)-1):
        n=m+1
        for n in range(len(list_lat)):
            dis=distance(list_lat[m], list_lat[n], list_lon[m], list_lon[m])
            dis_sum=dis_sum+dis
    if(len(list_lat)!=0):        
        avg_dis=dis_sum/len(list_lat)
        dict_to_store_groupidwith_average_event_distance[key]=avg_dis    
        
        
pickle.dump( dict_to_store_groupidwith_average_event_distance, open( "avg_dis_groupwise", "wb" ) )

print("")