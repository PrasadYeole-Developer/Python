str1 = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0

for i in range(len(str1)):
    if str1[i].isalpha():
        chars += 1
    elif str1[i].isdigit():
        digits += 1
    else:
        symbols += 1    

print("Chars =", chars)
print("Digits =", digits)
print("Symbols =", symbols)