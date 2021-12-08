# first topic: Data Science
# Excel, Data Analysis , Data Entry , Matplotlib , Database CRUD
# pie chart , line graph , bar graph , diagramme en tuyaux d'orgue
# packages: Random , Numpy , Scipy , Seaborn , matplotlib , pandas
# Random packages

import random as rd

# randrange(), randint() and uniform()
print(f"the number is {rd.randrange(1 , 10)}") # not included
print(f"the number is {rd.randint(1 , 10)}") #10 included 
print(f"the number is {rd.uniform(1 , 10)}") # it returns floating number between 1 and 10

Students = [
    "Abdelghani",
    "Ghina",
    "mostafa",
    "nour",
    'ahmad',
    "bilal"
]

# choice() and choices()
print(f"my name is {rd.choice(Students)}")
print(f"the new List is {rd.choices(Students , weights=[2 , 4, 1 , 1, 6 , 3] , k = 17 )}")

# shuffle()
rd.shuffle(Students)
print(Students)

# random() and sample()
print(f"the random is {rd.random()}") # the random method give us a floating number between 0 and 1
print(rd.sample(Students ,  k = 2)) # probability between 0 and 1