# Data Science
# random , math and numpy packages
# scipy , seaborn matplotlib and pandas
import numpy as np
FootballClub = np.array(
    [
        [ 
         [ 
             "FC Barcelona",
             "Real Madrid",
             "Valencia",
             "Celta Vigo"
          ],
         [ 
          "PSG",
          "Marseille",
          "Lyon",
          "Auxerre"
          ],
         ],
        [ 
         [ 
          "Manchester United",
          "Chelsea",
          "Liverpool",
          'Leicester City'
          ],
         [ 
          "Inter Milan",
          "AC Milan",
          "Roma",
          "Genoa"
          ]
         ]
    ]
)

# array is faster than list
# shape()
print(np.shape(FootballClub))
print("=" * 30)

# reshape the array using reshape()
newArray = FootballClub.reshape( 1, 8 , 2)

# looping usinng ndenumerate nditer
# ndenumerate(): two result first one :tuple second one : items
for id , club in np.ndenumerate(FootballClub):
    print(f"{id} - {club}")

# nditer()
club = np.random.choice(np.nditer(FootballClub))
print(club)

# numpy : contains math cmath random ,....
# periodic functions : sin cos
# numpy using math methods
angle = np.array([30 , 60 , 90])
sinAngle = np.sin(angle)# array
print(sinAngle)

# sorting using sort()
FootballClub.sort()
print(FootballClub)

# filtering
booleanArray = []
for x in np.nditer(FootballClub):
    if str(x).startswith('FC'):
        booleanArray.append(True)
    else:
        booleanArray.append(False)
print(booleanArray)