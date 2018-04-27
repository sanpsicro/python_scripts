# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 17:42:19 2017

@author: sperezp
"""

import pandas as pd

# load dataframe for data to compare
#
df_1 = pd.read_excel("Excel_files/2_articulos_categorizados_previa_segunda_carga.xlsx",converters={'Nrobien' : str})
#df_2 = pd.read_excel("Excel_files/2_articulos_categorizados_previa_segunda_carga.xlsx", converters={'SKU' : str})
df_2= pd.read_excel("Excel_files/2_catalog_product_20180426_234709.xlsx", converters={'sku' : str})

#transform desired column to list 
# 
L1 = df_1['Nrobien'].tolist()
#L2 = df_2['SKU'].tolist()
L2 = df_2['sku'].tolist()


# this function intersects  both lists
def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

#this function gets set difference between tow list
def difference(a,b):
    return list(set(a)-set(b))


matches = intersect(L1,L2)
diferencia = difference(L2,L1)




def remove_duplicates(l):
    newL=[]
    for i in l:
        if i not in newL:
            newL.append(i)
    return newL            
            
    