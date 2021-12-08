import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ExcelSheet = pd.read_excel(r"C:\Users\admin\Desktop\School\CLASSES\Grades.xlsx" , sheet_name="mostafa")
data = pd.DataFrame(ExcelSheet , columns = ['Quiz 1(12)' , 'exp'])

plt.plot(data['Quiz 1(12)'] , data['exp'] , marker="o" , mfc = "#349123" , mec = "#ff3746" , linestyle = "dotted" , c = 'red')
plt.show()
