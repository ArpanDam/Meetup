# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 21:22:14 2021

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

#total_degree_1=pickle.load(open("total_degree_1","rb"))

total_degree_1=pickle.load(open("total_degree_1","rb"))


m1=pickle.load(open("m1","rb"))

dict1={}
for key in total_degree_1:
    #i=0
    #for i in range(len(total_degree_1[key])):
    dict1[key]=len(total_degree_1[key])
        
pickle.dump( dict1, open( "m1", "wb" ),protocol=2 ) 