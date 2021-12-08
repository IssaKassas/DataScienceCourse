import pandas as pd
from openpyxl import load_workbook
# create an Excel file and write in it


wb = load_workbook(r"C:\Users\admin\Desktop\Python-Courses\file.xlsx")

wb.sheets = dict((ws.title, ws) for ws in wb.worksheets)

reader = pd.read_excel(r"C:\Users\admin\Desktop\Python-Courses\file.xlsx")

dataStudents = pd.DataFrame({
    "name": ["Abdelghani" , "mostafa" , "issa" , "khaled" , "nour"],
    "age": [17 , 34 , 28 , 27 , 26],
    "email": ["abdejf2@gmail.com","mg@outlook.com" , "issakassas1993@gmail.com" , "kfjsol" , "elrjs;z"],
    "phone": ["9343e" , "73682342", "3287e2","dkfdsjdlf","38642"]
        })

dataStudents.to_excel(wb,index= False , header= False , startrow= len(reader) + 1)

wb.close()

