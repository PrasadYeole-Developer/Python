A = {1:11,2:22}
B = {3:33,4:44}

A.update(B) # This is the one way
print(A) 

A = {1:11,2:22}
B = {3:33,4:44}

merged = {**A, **B} # Other way
print(merged) 

