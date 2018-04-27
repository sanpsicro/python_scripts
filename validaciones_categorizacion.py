# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 11:06:46 2018

@author: sperezp
"""

import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile


df = pd.read_excel('Importacion productos_23-4-18.xlsx', sheetname=0)
L1 = []


for x in df['price']:
    if 1500<x<15000:
        L1.append(1)
    else: 
        L1.append(0)
