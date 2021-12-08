import matplotlib.pyplot as plt
import numpy as np
import information as info
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.random.randint(100 , size = (13))
size = np.random.randint(1000 , size=(13))
#plt.scatter(x , y , color = "#9231dd")
plt.scatter(x, y ,  c = colors , cmap = "PiYG"  , s = size , alpha = 0.7)
plt.colorbar()
plt.show()
marks = np.array([7,8,10,11,12,14,15,18])
students = np.array([2,4,1,6,4,3,5,0])


plt.scatter(marks , students , color = info.colors)

plt.xlabel("Marks over 20")
plt.ylabel("Frequency")
plt.title("Statistics")
plt.colorbar()
plt.show()
