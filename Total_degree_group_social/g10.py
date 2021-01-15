# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 19:25:40 2020

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
ersvp=pickle.load(open("ersvp","rb"))

dict1={}

for key in new_grp_event:
    degree=0
    i=0
    for i in range(len(new_grp_event[key])):
        
        try:
            degree=degree+ len(ersvp[new_grp_event[key][i][0]])
        except:
            print("event not found")
    if(degree>0):
        dict1[key]=degree


pickle.dump( dict1, open( "g10_total_degree", "wb" ) )    