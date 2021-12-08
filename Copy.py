import NumpyS as n

# Copy Vs View

# copy()
copyArray = n.FML.copy()
print(copyArray)
copyArray[0 , 1 , 1] = "abdelghani"
print(n.FML)

# view()
viewArray = n.FML.view()
viewArray[0 , 1 , 1] = "abdelghani"
print(n.FML)

# ndenumerate()
tupleArray = n.np.shape(n.FML)
for id1 , id2 in n.np.ndenumerate(n.FML):
    print(id1 , id2)

print(tupleArray[0])