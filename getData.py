#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 14:31:33 2018
@author: echozhao
"""
#%% Data Preprocessing
# Import
import pandas as pd
import numpy as np
from random import sample

INPUT_PATH = './input/'

#%%
# Load the data

def get_data():

    child_wishlist = pd.read_csv(INPUT_PATH + 'child_wishlist_v2.csv', header=None).values
    gift_goodkids = pd.read_csv(INPUT_PATH + 'gift_goodkids_v2.csv', header=None).values

    child_wishlist = child_wishlist[:, 1:11]
    gift_goodkids  = gift_goodkids[:, 1:101]
    child_3 = child_wishlist[0:5001]    # ChildId 0-5000; triplets
    child_2 = child_wishlist[5001:45001]   # ChildId 5001-45000; twins
    child_1 = child_wishlist[45001:]      # ChildId 45000-999999; singlegift_goodkids_v2.csv'

    # Generate random sample
    rindex = np.array(sample(xrange(len(child_1)), 9549))
    child_1_sample = child_1[rindex]
    child_2_sample = child_2[0:400]
    child_3_sample = child_3[0:51]
    child_sample = np.concatenate([child_3_sample, child_2_sample, child_1_sample])

    rindex = np.array(sample(xrange(len(gift_goodkids)), 100))
    gift_sp = gift_goodkids[rindex]

    return child_sample, gift_sp
