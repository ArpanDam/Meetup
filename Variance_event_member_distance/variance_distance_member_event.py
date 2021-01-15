# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 17:41:03 2020

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

egroup=pickle.load(open("egroup","rb"))

etime=pickle.load(open("etime","rb"))

groupjoin=pickle.load(open("groupjoin","rb"))

memjoin=pickle.load(open("memjoin","rb"))  

mlat=pickle.load(open("mlat","rb"))

mlon=pickle.load(open("mlon","rb"))


elat=pickle.load(open("elat","rb"))

elon=pickle.load(open("elon","rb"))

#ersvp

ersvp=pickle.load(open("ersvp","rb"))

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
    
def variance(data):
    # Number of observations
    n = len(data)
    # Mean of the data
    if(n > 0):
        mean = sum(data) / n
     # Square deviations
        deviations = [(x - mean) ** 2 for x in data]
     # Variance
        variance = sum(deviations) / n
        return variance    

dict_to_store_variance_member_event_distance={}

for key in ersvp:
    member_list_lat=[]
    member_list_lon=[]
    #dis_sum=0
    dist=[]
    for i in range(len(ersvp[key])):
        
        try:
            event_lat=elat[key]  # latitude of event
            event_lon=elon[key]  # longitude of event 
            
            member_lat=mlat[ersvp[key][i][0]] # latitude of member
            member_lon=mlon[ersvp[key][i][0]]  # # longitude of member
            member_list_lat.append(member_lat)
            member_list_lon.append(member_lon)
            
            
        except:
            print("No event or member found")
    k=0
    for k in range(len(member_list_lat)):
        dis=distance(event_lat, member_list_lat[k], event_lon, member_list_lon[k])
        dist.append(dis)
        #dis_sum=dis_sum+dis
    if(len(member_list_lat)!=0):        
        #avg_dis=dis_sum/len(member_list_lat)
        dict_to_store_variance_member_event_distance[key]=variance(dist)  # key is event_id and value is the average distance between event and its members
        
        
pickle.dump( dict_to_store_variance_member_event_distance, open( "member_event_variance_dis_groupwise", "wb" ) )        
        
            
            
#sfile = open("etime",'rb')