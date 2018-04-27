# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 10:44:51 2018

@author: sperezp
"""

"Validación de la categorización"


import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import comparacion as compar


df = pd.read_excel('Excel_files\categorizacion_lakin_19042018.xlsx', sheetname=0)
df2 = pd.read_excel('Excel_files\Catalogo_varios.xlsx',sheetname=0 )
cp_list = []
#lista total de DIVERSOS o VARIOS
total_list = []
cpclean_list = []
cpclean_list2 = []
cpclean_list3 = []
unidentified_list = []
categorias = [] 
comp = []



#Separa los articulos DIVERSOS y varios del resto del total
for index,x in enumerate(df['DescripcionBien']):
    if "Familia:Varios" in x or "Familia:DIVERSOS" in x:
        var = "%s|%s" % (index,x)
        total_list.append(var)

#Separa los articulos de acuerdo a -existe la categoria, -no existe, -CELULARES        
for t in total_list:
    local = t.split("|")
    index = local[0]
    x=local[1]
    index=int(index)
    flag = 0;
    for index_y,y in enumerate(df2['Producto']):
            x_1 = x[x.find("Artículo:"):x.find(",Marca")]
            #El artículo existe en las categorías
            if y.lower().replace(" ", "") in x_1.lower().replace(" ", ""):
                   v = "%s:%s esta en %s >>>>,Departamento: %s-%s , cat1:%s-%s, cat2:%s-%s" % (index,y,x,df.iloc[index,0] , df2.iloc[index_y,0],df.iloc[index,1] , df2.iloc[index_y,1],df.iloc[index,2] , df2.iloc[index_y,2])
                   cp_list.append(v)
                   cpclean_list.append(x)
                   h = "%s -- %s|%s-%s-%s|%s-%s-%s" % (index,x,df.iloc[index,0],df.iloc[index,1],df.iloc[index,2] , df2.iloc[index_y,0] , df2.iloc[index_y,1] , df2.iloc[index_y,2])
                   categorias.append(h)
                   flag = 1;
                   break
            #El artículo es un celular   
            elif y.lower().replace(" ", "") in x.lower().replace(" ", "") and "CELULAR" in y:
                    v = "%s:%s esta en %s >>>>,Departamento: %s-%s , cat1:%s-%s, cat2:%s-%s" % (index,y,x,df.iloc[index,0] , df2.iloc[index_y,0],df.iloc[index,1] , df2.iloc[index_y,1],df.iloc[index,2] , df2.iloc[index_y,2])
                    cp_list.append(v)
                    cpclean_list3.append(x)
                    h = "%s -- %s|%s-%s-%s|%s-%s-%s" % (index,x,df.iloc[index,0],df.iloc[index,1],df.iloc[index,2] , df2.iloc[index_y,0] , df2.iloc[index_y,1] , df2.iloc[index_y,2])
                    categorias.append(h)
                    flag = 1;
                    break
            #El articulo se encuentra en alguna parte de la descripcion    
            elif y.lower() in x.lower():  
                    v = "%s:%s esta en %s >>>>,Departamento: %s-%s , cat1:%s-%s, cat2:%s-%s" % (index,y,x,df.iloc[index,0] , df2.iloc[index_y,0],df.iloc[index,1] , df2.iloc[index_y,1],df.iloc[index,2] , df2.iloc[index_y,2])
                    cp_list.append(v)
                    cpclean_list2.append(x)
                    h = "%s -- %s|%s-%s-%s|%s-%s-%s" % (index,x,df.iloc[index,0],df.iloc[index,1],df.iloc[index,2] , df2.iloc[index_y,0] , df2.iloc[index_y,1] , df2.iloc[index_y,2])
                    categorias.append(h)
                    flag = 1;
                    break
    #El articulo no se encuentra en ninguna categoría            
    if flag == 0:
        v = "%s >>>>,Departamento: -%s , cat1:-%s, cat2:-%s" % (x,df.iloc[index,0] ,df.iloc[index,1] ,df.iloc[index,2] )
        unidentified_list.append(v)        
                   
                
#Decide que tercias de categorias son iguales y cuales no
for x in categorias:
    L = x.split("|")
    if L[1] == L[2]:
        comp.append(1)
    else:
        comp.append(x)
        
 

    
#diferencia = compar.difference(total_list,cpclean_list)

    
        
