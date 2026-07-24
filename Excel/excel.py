import openpyxl
from openpyxl import*

path = r"Excel\excel.xlsx"
workBook = Workbook()
workBook.save(path)