numbers = [-1,2,3,-4,5,-5,-6,6,7,8]

negativeNumbers = []
positiveNumbers = []

for num in numbers:
    if(num>=0): positiveNumbers.append(num)
    else: negativeNumbers.append(num)

print("Positive numbers: ", positiveNumbers)
print("Negative numbers: ", negativeNumbers)
