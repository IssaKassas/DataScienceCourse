import numpy as np
import random as rd
colors = np.array(["#23fd23" , "#734211" , "#837421" ,"red" , "blue" , "red" , "#000000" , "yellow"])

cmapColors = []
for i in range(0 , 13):
    x = rd.randint(0 , 100)
    cmapColors.append(x)
