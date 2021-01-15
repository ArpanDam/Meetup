# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 12:18:23 2020

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
for key in new_grp_event:
    sum=0
    i=0
    key_found=0
    for i in range(len(new_grp_event[key])):
        try:
            event_id=new_grp_event[key][i][0]
            sum=sum+hcount[event_id]
            key_found=1
        except:
            print(" ")
    if(key_found==1):
        dict1[key]=sum/len(new_grp_event[key])


pickle.dump( dict1, open( "average_rsvp", "wb" ) )        
            

print(" ")