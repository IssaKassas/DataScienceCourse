import numpy as np
import matplotlib.pyplot as plt

n = np.array([
    1,2,3,4
])

sqrt = np.sqrt(n)

plt.plot(n , sqrt)
plt.xlabel("the values of n")
plt.ylabel("the values of sqrt(n)")
plt.show()