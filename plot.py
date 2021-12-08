# matplotlib package
# installation
import matplotlib.pyplot as plt
import numpy as np
import math

# matplotlib version
import matplotlib as mp
print(mp.__version__)

# y = lnx
xaxis = np.array([1,2,math.e,3,4])
yaxis = []
for x in np.nditer(xaxis):
    yaxis.append(math.log(x))

# marker argument
plt.plot(yaxis , marker = 'o')
plt.show()

# y = e^x
xaxis = [1,2,3,5,7, 11]
ordonnee = np.exp(xaxis)
# color argument
plt.plot(xaxis , ordonnee , marker = "*" , color= "r")
plt.show()

# more arguments
plt.plot(xaxis , ordonnee, linestyle = "dashed" , c = "#4EEC18", marker = "o", 
         ms = 12, mec = "r" , mfc = "#C638CB" , linewidth = '12.8') 
# mec: marker edge color , mfc: marker face color for markers &  c === color for linestyle
plt.show()