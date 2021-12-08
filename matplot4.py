# matplotlib bars histograms
import matplotlib.pyplot as plt
import numpy as np
# stastics 
# caractere qualitatif
# Lebanon , USA , Canada
# colors blue , black , red

names = np.array([
    "Nour",
    "Khaled",
    "Ahmad",
    "Riwa",
    "Mohamad"
])

grades = [
    33,
    2,
    2,
    9,
    20
]
# vertical
plt.subplot(3,2,1)
# diagramme en tuyaux d'orgue
plt.bar(names , grades , color = "#298302" , width = 0.5)
plt.subplot(3,2,2)
plt.barh(names , grades , color = "black" , height = 0.5)
plt.subplot(3 , 2 , 3)
# histogram : caractere quantitatif continue => classe => interval
normal = np.random.normal(100 , 5 , 300) # N(0,1) X = 0 , standard deviation = 0
plt.hist(normal , color= "red")
plt.subplot(3 , 2 , 4)
normal2 = np.random.normal(0 , 1 , 300) # N(0,1) X = 0 , standard deviation = 0
plt.hist(normal2)
plt.subplot(3,2,5)
plt.pie(grades)
plt.show()
ex = [ 0.3 , 0.1 , 0 , 0 , 0.2]
col = ["#253126" , "#111032" , "red" , "yellow" , 'hotpink']
plt.pie(grades , labels= names , startangle= 90 , explode= ex , shadow = True , colors=col)
plt.legend()
plt.show()

# pie chart == diagramme circulaire
# 100 -> 360degree -> 2Pi radians

# probabilite == frequence
# frequency = effectif ni  effectif total = n
# relative frequency = frequence fi = ni/n
# percentage = pourcentage => % = fi * 100

# angle
# 100 -> 360
# 30-> 
# 30 x 360/100 = 10