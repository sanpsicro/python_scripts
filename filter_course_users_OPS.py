# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 17:20:48 2018

@author: Santiago Pérez
         filter Mexican users from the total  list of users of the course 
"""

import pandas as pd
import xlsxwriter


xl = pd.ExcelFile('Excel_files\Informe_CVSP_Curso_Liderazgo_2018.xls')

sheet_name = xl.sheet_names  # see all sheet names

xl.parse(sheet_name)  

workbook = xlsxwriter.Workbook('relacion_alumnos_liderazgo_en_enfermeria.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': 1})

worksheet.write('A1', 'Curso', bold)
worksheet.write('B1', 'Inicio', bold)
worksheet.write('C1', 'Estado', bold)
worksheet.write('D1', 'Nombre', bold)
worksheet.write('E1', 'Apellido', bold)
worksheet.write('F1', 'Lugar de trabajo', bold)
worksheet.write('G1', 'fecha2', bold)
worksheet.write('H1', 'sexo', bold)
worksheet.write('I1', 'Correo', bold)
worksheet.write('J1', 'fecha3', bold)
worksheet.write('K1', 'x', bold)
worksheet.write('L1', 'estatus', bold)
worksheet.write('M1', 'calificación', bold)


x = sheet_name[49].split(' ')

row = 1


for x in sheet_name:
    y = x.split(' ')
    if len(y) > 1:
        if int(y[1]) >= 49:
            current_sheet = pd.read_excel('Excel_files\Informe_CVSP_Curso_Liderazgo_2018.xls', sheetname=x, header = None)
            for this_index,this_cell in enumerate(current_sheet[2]):
                if this_cell == 'MEXICO': #current_sheet(columna,fila)
                     worksheet.write_string(row, 0, current_sheet[this_index][0] )  #nombre del curso 
                     worksheet.write_string(row,  1, current_sheet[this_index][0]) #fecha de inicio
                     worksheet.write_string(row,  2, current_sheet[this_index][0]) # Estado 
                     worksheet.write_string(row, 3,current_sheet[this_index][0] ) # Nombre
                     worksheet.write_string(row, 4, current_sheet[this_index][0]) #Apellido
                     worksheet.write_sting(row,5,current_sheet[this_index][0]) #Lugar de trabajo 
                     worksheet.write_string(row, 6, current_sheet[this_index][0]) #fecha 2
                     worksheet.write_string(row, 7, current_sheet[this_index][0]) # sexo
                     worksheet.write_string(row, 8, current_sheet[this_index][0]) #correo
                     worksheet.write_string(row, 9, current_sheet[this_index][0]) #fecha3 
                     worksheet.write_string(row, 10, current_sheet[this_index][0]) #x
                     worksheet.write_string(row, 11, current_sheet[this_index][0]) #estatus
                     worksheet.write_string(row, 12, current_sheet[this_index][0]) #Calificación
                     row = row +1
    else: continue           
    

workbook.close()
