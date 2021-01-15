# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 21:17:10 2021

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

mem_event_1=pickle.load(open("mem_event_1","rb"))

hcount=pickle.load(open("hcount","rb"))


dict1={}
for key in mem_event_1:
    i=0
    list1=[]
    for i in range(len(mem_event_1[key])):
        group_id=mem_event_1[key][i]
        list1.append(group_id)
    j=0
    list2=[]
    for j in range(len(list1)):
        try:
            list2.append(hcount[list1[j]])
        except:
            print("")
    dict1[key]=list2        
    
    
pickle.dump( dict1, open( "m10_attendance_distribution_of_members_protocol_2", "wb" ), protocol=2)    