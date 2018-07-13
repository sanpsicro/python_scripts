# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:54:30 2018

@author: Usuario
"""

import pandas as pd

#lista proporcionada por el nodo regiona
df_1 = pd.read_excel("concentrado_correos.xlsx",converters={'apoyoauto' : str, 'diabetesii':str,'lidenf':str,'HAS':str})
#lista proporcionada por virginia molina
df_2= pd.read_excel("concentrado_correos.xlsx", converters={'apoyoauto_plat' : str, 'diabetesii_plat':str,'lidenf_plat':str,'HAS_plat':str})

names_apoyoauto = []
names_diabetesii = []

names_lidenf = []
names_lidenf_UNEMES = []
names_lidenf_TAE = []

names_HAS = []

#transform desired column to list 
# 
L1_a = df_1['apoyoauto'].tolist()
#L2 = df_2['SKU'].tolist()
L2_a = df_2['apoyoauto_plat'].tolist()

#----------------------------------------------------
L1_d = df_1['diabetesii'].tolist()
#L2 = df_2['SKU'].tolist()
L2_d = df_2['diabetesii_plat'].tolist()
# this function intersects  both lists

#----------------------------------------------------
L1_l = df_1['lidenf'].tolist()
L1_lu = df_1['lidenf_UNEMES'].tolist()
L1_lt = df_1['lidenf_TAE'].tolist()
#L2 = df_2['SKU'].tolist()
L2_l = df_2['lidenf_plat'].tolist()
# this function intersects  both lists

#----------------------------------------------------
L1_h = df_1['HAS'].tolist()
#L2 = df_2['SKU'].tolist()
L2_h = df_2['HAS_plat'].tolist()
# this function intersects  both lists



def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def difference(a,b):
    return list(set(a)-set(b))


matching_apoyoauto = intersect(L1_a,L2_a)

matching_diabetesii = intersect(L1_d,L2_d)

matching_lidenf= intersect(L1_l,L2_l)
matching_lidenf_UNEMES= intersect(L1_lu,L2_l)
matching_lidenf_TAE= intersect(L1_lt,L2_l)

matching_HAS= intersect(L1_h,L2_h)
    
for i,x in enumerate(df_1['apoyoauto']):
    if x in matching_apoyoauto:
        names_apoyoauto.append([df_1['apoyoauto_name'][i],df_1['apoyoauto_cal_s2'][i]])
        
        
        
            
for i,x in enumerate(df_1['diabetesii']):
    if x in matching_diabetesii:
        names_diabetesii.append([df_1['diabetesii_name'][i],df_1['diabetesii_cal_s2'][i]])
        
        
            
for i,x in enumerate(df_1['lidenf']):
    if x in matching_lidenf:
        names_lidenf.append([df_1['lidenf_name'][i],df_1['lidenf_cal_s2'][i]])
        
for i,x in enumerate(df_1['lidenf_UNEMES']):
    if x in matching_lidenf_UNEMES:
        names_lidenf_UNEMES.append([df_1['lidenf_UNEMES_name'][i],df_1['lidenf_cal_s2'][i]])
        
for i,x in enumerate(df_1['lidenf_TAE']):
    if x in matching_lidenf_TAE:
        names_lidenf_TAE.append([df_1['lidenf_TAE_name'][i],df_1['lidenf_cal_s2'][i]])
        

            
for i,x in enumerate(df_1['HAS']):
    
    if x in matching_HAS:
        names_HAS.append([df_1['HAS_name'][i],df_1['HAS_cal_s2'][i]])
        
dif_HAS = difference(L1_h,matching_HAS)

names_HAS_dif = []            
for i,x in enumerate(df_1['HAS']):
    if x in dif_HAS:
        names_HAS_dif.append(df_1['HAS_name'][i])
        
        #-------------------------------------------------------------
        
dif_diabetesii = difference(L1_d,matching_diabetesii)

names_diabetesii_dif = []            
for i,x in enumerate(df_1['diabetesii']):
    if x in dif_diabetesii:
        names_diabetesii_dif.append(df_1['diabetesii_name'][i])
        
           #-------------------------------------------------------------
        
dif_lidenf = difference(L1_l,matching_lidenf)

names_lidenf_dif = []            
for i,x in enumerate(df_1['lidenf']):
    if x in dif_lidenf:
        names_lidenf_dif.append(df_1['lidenf_name'][i])
#------------------------------------------------------------        
dif_lidenf_UNEMES = difference(L1_lu,matching_lidenf_UNEMES)

names_lidenf_dif_UNEMES = []            
for i,x in enumerate(df_1['lidenf_UNEMES']):
    if x in dif_lidenf_UNEMES:
        names_lidenf_dif_UNEMES.append(df_1['lidenf_UNEMES_name'][i])
        
#---------------------------------------------------        
dif_lidenf_TAE= difference(L1_lt,matching_lidenf_TAE)

names_lidenf_dif_TAE = []            
for i,x in enumerate(df_1['lidenf_TAE']):
    if x in dif_lidenf_TAE:
        names_lidenf_dif_TAE.append(df_1['lidenf_TAE_name'][i])
        
 
          #-------------------------------------------------------------
        
dif_apoyoauto = difference(L1_a,matching_apoyoauto)

names_apoyoauto_dif = []            
for i,x in enumerate(df_1['apoyoauto']):
    if x in dif_apoyoauto:
        names_apoyoauto_dif.append(df_1['apoyoauto_name'][i])       
        
        