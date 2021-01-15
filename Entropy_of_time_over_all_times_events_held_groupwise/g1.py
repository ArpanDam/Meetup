# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 19:57:37 2021

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


new_grp_event=pickle.load(open("new_grp_event","rb"))

print("")

def entropy3(labels, base=2):
  vc = pd.Series(labels).value_counts(normalize=True, sort=False)
  base = e if base is None else base
  return -(vc * np.log(vc)/np.log(base)).sum()

dict1={}
list1=[]
for key in new_grp_event:
    i=0
    for i in range(len(new_grp_event[key])):
       list1.append(new_grp_event[key][i][1]) 
    
    
    
min_time=min(list1)
max_time=max(list1)

interval_size=(max_time-min_time)/5
first_interval=min_time + interval_size
second_interval=first_interval+ interval_size
third_interval=second_interval+ interval_size
fourth_interval=third_interval+ interval_size
fifth_interval=fourth_interval+ interval_size

for key in new_grp_event:
    i=0
    list2=[]
    label=[]
    for i in range(len(new_grp_event[key])):
       list2.append(new_grp_event[key][i][1]) 
    
    
    
    j=0    
    for j in range(len(list2)):
            if(list2[j]< first_interval):
                label.append(1)
            if(list2[j]> first_interval) and(list2[j]< second_interval):
                label.append(2)
            if(list2[j]> second_interval) and(list2[j]< third_interval):
                label.append(3)
            if(list2[j]> third_interval) and(list2[j]< fourth_interval):
                label.append(4)    
            if(list2[j]> fourth_interval) and(list2[j]< fifth_interval):
                label.append(5)
    dict1[key]=entropy3(label, base=2)  
    
    
pickle.dump( dict1, open( "g1_entropy", "wb" ) )    