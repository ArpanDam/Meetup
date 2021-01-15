# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:49:23 2021

@author: HP
"""


# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 21:15:45 2021

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
memjoin=pickle.load(open("memjoin","rb"))
total_degree_1=pickle.load(open("total_degree_1","rb"))

#m1=pickle.load(open("m1","rb"))
dict1={}


for key in total_degree_1:
    i=0
    sum1=0
    list_event_number=[]
    list1=[]
    
    for i in total_degree_1[key]:
        list1.append(i)  # list1 contains 1 hop neighbour
    j=0
    for j in range(len(list1)):
        try:
            number_of_event=len(memjoin[list1[j]])
            list_event_number.append(number_of_event)
            #sum1=sum1+number_of_event
        except:
            print("")
    
    dict1[key]=list_event_number

pickle.dump( dict1, open( "m11_event_number_of_1hop", "wb" ),protocol=2 )    