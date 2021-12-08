import pandas as pd

from openpyxl import load_workbook

# create a file
writer = pd.ExcelWriter(r"Grades.xlsx" , engine= "xlsxwriter")

df = pd.DataFrame({'Name': ['A', 'B', 'C', 'D'],
                   'Age': [10, 0, 30, 50]})
df.to_excel(writer, sheet_name='Sheet1', index=False)

writer.save()

'''
writer = pd.ExcelWriter(r'Grades.xlsx', engine='openpyxl')
writer.book = load_workbook(r"Grades.xlsx")

writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)

reader = pd.read_excel(r"Grades.xlsx")

df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

writer.close()
'''
