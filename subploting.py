import matplotlib.pyplot as plt
import numpy as np
import math as m
import attribute as att

xaxis  = np.array([1,2,4,8])

yaxis1 = []
yaxis2= []
for x in np.nditer(xaxis):
    yaxis1.append(m.pow(x,2))
    yaxis2.append(m.exp(x))

# subplot(i,j,k): i ligne j colonne k indice
plt.subplot(3,1,1)
plt.plot(xaxis , yaxis1)
plt.title("Khaled")
plt.xlabel(att.xLabel)
plt.ylabel(f"{att.courbe} (C)")

plt.subplot(3,1,3)
plt.plot(xaxis , yaxis2)
plt.xlabel(att.xLabel)
plt.title("Nour")
plt.ylabel(f"{att.courbe} (C')")
plt.suptitle("Issa", fontdict= att.font1)
plt.show()