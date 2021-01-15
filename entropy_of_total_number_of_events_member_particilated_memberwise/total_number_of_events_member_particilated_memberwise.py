# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 21:34:32 2020

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


memjoin=pickle.load(open("memjoin","rb"))

new_grp_event=pickle.load(open("new_grp_event","rb"))  

dict1={}
for key in memjoin:
    member=key
    i=0
    group_id_list=[]
    for i in range(len(memjoin[key])):
        group_id_list.append(memjoin[key][i][0])
    k=0
    number_of_event=[]
    for k in range(len(group_id_list)):
        try:
            number_of_event.append(len(new_grp_event[group_id_list[k]]))
        except:
            print()    
        dict1[key]=number_of_event
        
        
pickle.dump( dict1, open( "m6_number_of_events", "wb" ), protocol=2 )         
        
        
        

