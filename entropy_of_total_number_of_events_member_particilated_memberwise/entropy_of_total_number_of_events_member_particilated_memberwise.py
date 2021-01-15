# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 21:18:15 2020

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


m6_number_of_events=pickle.load(open("m6_number_of_events","rb"))

def entropy3(labels, base=2):
  vc = pd.Series(labels).value_counts(normalize=True, sort=False)
  base = e if base is None else base
  return -(vc * np.log(vc)/np.log(base)).sum()


dict1={}
list1=[]
label=[]
for key in m6_number_of_events:
    list1=[]
    label=[]
    i=0
    for i in range(len(m6_number_of_events[key])):
        list1.append(m6_number_of_events[key][i])
    if(len(list1)>0):    
        min_time=min(list1)
        max_time=max(list1)
    # Deviding into 5 bins
        interval_size=(max_time-min_time)/5
        first_interval=min_time + interval_size
        second_interval=first_interval+ interval_size
        third_interval=second_interval+ interval_size
        fourth_interval=third_interval+ interval_size
        fifth_interval=fourth_interval+ interval_size
        #there will be 5 labels
        for j in range(len(list1)):
            if(list1[j]< first_interval):
                label.append(1)
            if(list1[j]> first_interval) and(list1[j]< second_interval):
                label.append(2)
            if(list1[j]> second_interval) and(list1[j]< third_interval):
                label.append(3)
            if(list1[j]> third_interval) and(list1[j]< fourth_interval):
                label.append(4)    
            if(list1[j]> fourth_interval) and(list1[j]< fifth_interval):
                label.append(5)
        dict1[key]=entropy3(label, base=2)        
            

pickle.dump( dict1, open( "m6_entropy", "wb" ), protocol=2 )

    

print(" ")
