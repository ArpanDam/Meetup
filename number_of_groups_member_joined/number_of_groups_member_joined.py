# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 18:08:37 2020

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

egroup=pickle.load(open("egroup","rb"))

etime=pickle.load(open("etime","rb"))

groupjoin=pickle.load(open("groupjoin","rb"))

memjoin=pickle.load(open("memjoin","rb"))  

dict1={}
for key in memjoin:
    dict1[key]=len(memjoin[key])

pickle.dump( dict1, open( "number_of_group_member_wise", "wb" ) )   