s = {1,2,3,4,5,6,7,8}
print(s)
s.add(9)
s.remove(3) # will give error if element not found
print(s)
s.discard(10) # won't give error if element not found
s.pop() # removes random element
s.clear()
print(s)
s = {1,2,3}
print(s)

# Operations on 2 sets
## Union (A|B) , intersection(A&B), difference(A-B), symmetricDifference(A^B)

A = {1,2,3}
B = {3,4,5}
unionSet = A.union(B)
intersectionSet = A.intersection(B)
differenceSet = A.difference(B)
symmetricDifferenceSet = A.symmetric_difference(B)

print("Union", unionSet)
print("Intersection", intersectionSet)
print("Difference", differenceSet)
print("Symmetric difference", symmetricDifferenceSet)