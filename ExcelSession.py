import pandas as pd
from openpyxl import load_workbook

# create an Excel file and write in it
fileCreated = pd.ExcelWriter(r"C:\Users\admin\Desktop\Python-Courses\Data.xlsx" , engine = "openpyxl")
fileCreated.book = load_workbook(r"C:\Users\admin\Desktop\Python-Courses\Data.xlsx")
fileCreated.sheets = dict((ws.title, ws) for ws in fileCreated.book.worksheets)
reader = pd.read_excel(r"C:\Users\admin\Desktop\Python-Courses\Data.xlsx")

dataStudents = pd.DataFrame({
    "name": ["Abdelghani" , "mostafa" , "issa" , "khaled" , "nour"],
    "age": [17 , 34 , 28 , 27 , 26],
    "email": ["abdejf2@gmail.com","mg@outlook.com" , "issakassas1993@gmail.com" , "kfjsol" , "elrjs;z"],
    "phone": ["9343e" , "73682342", "3287e2","dkfdsjdlf","38642"]
        })
dataStudents.to_excel(fileCreated,index= False , header= False , startrow= len(reader) + 1)
fileCreated.close()

dataTeachers = pd.DataFrame({
    "name": ["Ahmad" , "mostafa" , "issa" , "khaled" , "nour"],
    "age": [17 , 34 , 28 , 27 , 26],
    "email": ["abdejf2@gmail.com","mg@outlook.com" , "issakassas1993@gmail.com" , "kfjsol" , "elrjs;z"],
    "phone": ["9343e" , "73682342", "3287e2","dkfdsjdlf","38642"]
        })

# dataStudents.to_excel(fileCreated , sheet_name = "Students" , index = False)
# dataTeachers.to_excel(fileCreated , sheet_name = "Teachers" , index = False)
#fileCreated.save()

# read from Excel
# reader = pd.read_excel(r"C:\Users\admin\Desktop\Python-Courses\File.xlsx" , sheet_name= "Students")
# print(reader[["name" , "email"]])