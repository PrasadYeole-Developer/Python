n = int(input("Enter input: "));
evenSum = 0;
oddSum = 0;
for i in range(1, n+1):
    if i%2 == 0:
        evenSum += i;
    else: 
        oddSum += i;

print("Even sum:", evenSum)
print("Odd sum:", oddSum)
