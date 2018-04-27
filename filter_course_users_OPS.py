# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:20:48 2018

@author: Santiago Pérez
         filter Mexican users from the total  list of users of the course 
"""

import pandas as pd


xl = pd.ExcelFile('Excel_files\Informe_CVSP_Curso_Liderazgo_2018.xls')

sheet_name = xl.sheet_names  # see all sheet names

xl.parse(sheet_name)  


x = sheet_name[49].split(' ')

for x in sheet_name:
    y = x.split(' ')
    if len(y) > 1:
        if int(y[1]) >= 49:
            current_sheet = pd.read_excel('Excel_files\Informe_CVSP_Curso_Liderazgo_2018.xls', sheetname=x)
    

