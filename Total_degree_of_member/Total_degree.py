# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 18:58:50 2021

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

#ersvp=pickle.load(open("ersvp","rb"))


mem_event=pickle.load(open("mem_event_1","rb"))



    
    
nbr={}
for m1 in mem_event:
           nbr[m1]=set()
           
           for m2 in mem_event:
                 if m2!=m1 and len(set(mem_event[m1]).intersection(set(mem_event[m2])))>0:
                     nbr[m1].add(m2)
                       
                     

#json_object = json.dumps(nbr, indent = 4)
pickle.dump( nbr, open( "total_degree_1", "wb" ),protocol=2 ) 

#protocol=2                    

#pickle.dump(total_degree_1, nbr, protocol=2)