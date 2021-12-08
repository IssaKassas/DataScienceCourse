# array <===> list
# array is better than list
import numpy as np
# version
print(np.__version__)

# array's Dimension: 0D 1D 2D 3D nD

# array 0D
number  = np.array(5)

# array 1D
Students = np.array([
    "nour" , 
    "mostafa",
    "riwa"
])

# array 2D
EmailPass = np.array(
    [[
      "issakasass1993@gmail.com",
      "nounajaber00@gmail.com"  
    ],
    [
       "3u2483424d",
       "3829wdje34" 
    ]]
)

FML = np.array(
    [[[
        "issa",
        "mostafa",
        "riwa"
    ], 
    [
        "jalal",
        "abdelsalam",
        "fadi"
    ],
    [
        "kassas",
        "ghemrawi",
        "hammoud"
    ]],
    [[
        28,
        35,
        17
    ], [
        "Zahriye",
        "Badawi",
        "Dam ElFeraz"
    ],
    [
       "issakasass1993@gmail.com",
        "nounajaber00@gmail.com" ,
        "riwa11@outlook.com" 
    ]]]
)

# ndim attribute to know the dimension
print(FML.ndim)

# ndmin argument to change the dimension
print(np.array(FML , ndmin = 5))

# indexing in array
print(f"the index 1 give us {FML[1]}")
# print(f"the index 1 give us {FML[2]}") ERROR

# slicing in array
print(f"the index 0 ,2 give us {FML[0:2 , 2 , 0 : 2]}")

# in database engine, For Example, SQL Server has stored procedure or (Backup) to store 
# your data and your queries

# shape()
print(np.shape(FML))

Students = np.array(
    [[
        "issa",
        "mostafa",
        "riwa"
    ], 
    [
        "jalal",
        "abdelsalam",
        "fadi"
    ],
    [
        "kassas",
        "ghemrawi",
        "hammoud"
    ]])

Teachers = np.array( 
    [[
        28,
        35,
        17
    ], [
        "Zahriye",
        "Badawi",
        "Dam ElFeraz"
    ],
    [
       "issakasass1993@gmail.com",
        "nounajaber00@gmail.com" ,
        "riwa11@outlook.com" 
    ]])

# concatenate()
array = np.concatenate((Students , Teachers) , axis = 1)

# stack()
arrayStack = np.stack((Students , Teachers))

print(array)
print("=" * 100)
print(arrayStack)