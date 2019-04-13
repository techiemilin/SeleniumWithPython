'''
Created on Apr. 11, 2019

@author: milinpatel
'''
import openpyxl

path = "/Users/milinpatel/Documents/workspace/SeleniumWithPython/excelfiles/WriteData.xlsx"

workbook = openpyxl.load_workbook(path)

sheet = workbook.active

for r in range (1, 5 + 1):
    for c in range(1, 3 + 1):
        sheet.cell(row=r, column=c).value = "Welcome,Milin"
        
workbook.save(path)
