numbers = [3,4,2,6,4,7,8,4,2]

maxVal = 0

for num in numbers:
    if maxVal < num:
        maxVal = num

print("Greatest element:", maxVal)
