# Recursive algorithms should have an base case , i.e something to stop them
# Recursive algorithms should change state, i.e moving towards the base case
# Recursive algorithms should call theirselves

def listsum(numList):
   if len(numList) == 1:
       return numList[0]
   else:
       print numList[0]
       print numList[1:]
       return numList[0] + listsum(numList[1:])


print(listsum([1,3,5,7,9]))