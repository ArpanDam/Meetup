# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 09:29:44 2021

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

#m9=pickle.load(open("m9","rb"))
m11_event_number_of_1hop=pickle.load(open("m11_event_number_of_1hop","rb"))



def entropy1(labels, base=2):
  value,counts = np.unique(labels, return_counts=True)
  return entropy(counts, base=2)

def entropy3(labels, base=2):
  vc = pd.Series(labels).value_counts(normalize=True, sort=False)
  base = e if base is None else base
  return -(vc * np.log(vc)/np.log(base)).sum()


list1=[]
for key in m11_event_number_of_1hop:
    i=0
    for i in range(len(m11_event_number_of_1hop[key])):
        list1.append(m11_event_number_of_1hop[key][i])


min_event=min(list1)
max_event=max(list1)  
interval_size=(max_event-min_event)/5
first_interval=min_event + interval_size
second_interval=first_interval+ interval_size
third_interval=second_interval+ interval_size
fourth_interval=third_interval+ interval_size
fifth_interval=fourth_interval+ interval_size



list2=[]
dict1={}
for key in m11_event_number_of_1hop:
    i=0
    label=[]
    list2=[]
    for i in range(len(m11_event_number_of_1hop[key])):
        list2.append(m11_event_number_of_1hop[key][i])
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
    dict1[key]=entropy1(label, base=2)          


pickle.dump( dict1, open( "m11", "wb" ) )

    

print(" ")