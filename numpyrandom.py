from numpy import random as rd
import numpy as np

# randint()
A = rd.randint(10 , size = (2 , 3))
B = rd.randint(5 , size = (2 , 3))
print(f'A = \n{A}')
print(f"B = \n{B}")

# sum of two matrices
Sum = A + B
print(f"Sum = \n{Sum}")

# difference between two matrices
Diff = A - B
print(f"Diff = \n{Diff}")

# product
Prod = A * B
print(f"Prod = \n{Prod}")
print("--" * 20)

# transpose()
B = np.transpose(B)
print(f'A = \n{A}')
print(f"B = \n{B}")

# product using @ or dot()
ProducMatrix = A.dot(B)
ProducMatrix = A @ B
print(f"Multiple = \n{ProducMatrix}")

# rand()
FloatArray = rd.rand(2,3)
print(FloatArray)

# choice()
choiceArray = rd.choice([1,2,3,4] , size = (3,4))
numbers = np.array([1,2,3,4,5])
probability = rd.choice(numbers , p = [0.3 , 0.2 , 0.2 , 0.1 , 0.2] , size=(3,5))

# sum of probability = 1 
# probability = relative frequency
# permutation() <===> shuffle()
rd.permutation(probability) # shuffle()
print(probability)

# particular matrices
zerArray  = np.zeros((2, 5 , 4))
oneArray = np.ones((1,2,3))
emptyArray = np.empty((2,3))
print(zerArray)
print(emptyArray)
print(oneArray)