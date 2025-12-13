numbers = [3,4,2,6,4,7,8,4,2]

maxVal = numbers[0]
secondMax = float("-inf")

for num in numbers:
    if maxVal<num:
        secondMax = maxVal
        maxVal = num
    elif num!=maxVal and secondMax<num:
        secondMax = num

print("Second largest element:",secondMax)