import matplotlib.pyplot as plt
import numpy as np
import math as m
import attribute as attr

xaxis  = np.array([1,2,4,8])

yaxis1 = []
yaxis2= []
for x in np.nditer(xaxis):
    yaxis1.append(m.pow(x,2))
    yaxis2.append(x*3)

# dictionnary
font1 = {
    "family":  attr.fontFamily1,
    "color": "#9ab321",
    "size": attr.fontSizeLabels
}

font2 = {
    "family":  attr.fontFamily2,
    "color": "#342abc",
    "size": attr.fontSizeLabels
}

fonttitle = {
    "family":  "arial",
    "color": "yellow",
    "size": "21"
}

plt.xlabel("The value of X".upper() , fontdict = font1)
# dict : dictionnary == json data

plt.ylabel("The value of Y".capitalize() , fontdict= font2)

plt.title("Graphs f(x) and g(x)" , fontdict=fonttitle , loc=attr.location)

plt.plot(xaxis,yaxis1,xaxis,yaxis2 , linestyle = "--" , c = "#374938", marker = "*",
         mfc = "red" , mec = "#923211")

plt.grid(axis = "x" , color = "red" , linestyle = 'dotted')

plt.show()