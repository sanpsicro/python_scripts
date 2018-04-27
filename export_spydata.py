# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 12:56:40 2018

@author: Usuario
"""

import pandas

df = pandas.DataFrame(data=matches)

df.to_clipboard(excel=True)