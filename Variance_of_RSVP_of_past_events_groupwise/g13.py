# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:00:21 2020

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


hcount=pickle.load(open("hcount","rb"))

new_grp_event=pickle.load(open("new_grp_event","rb"))

dict1={}


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
    
    
for key in new_grp_event:
    #sum=0
    i=0
    key_found=0
    list=[]
    for i in range(len(new_grp_event[key])):
        try:
            event_id=new_grp_event[key][i][0]
            list.append(hcount[event_id])
            key_found=1
        except:
            print(" ")
    if(key_found==1):
        dict1[key]=variance(list)


pickle.dump( dict1, open( "variance_rsvp", "wb" ) )        
            

print(" ")