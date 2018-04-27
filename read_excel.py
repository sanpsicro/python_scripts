# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 11:55:34 2017

@author: Usuario
"""

import xlrd


def getSKU(filename,index_col):
    from os.path import join, dirname, abspath
    fname = join(dirname(dirname(abspath(__file__))),'carga_masiva',filename)
    print(fname)
    wb = xlrd.open_workbook(fname)
    sh = wb.sheet_by_index(0)
    colA = sh.col_values(index_col)
    colA.pop(0)
    return colA
    
