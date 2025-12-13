num = int(input("Enter number: "))

strNum = str(num)
revNum = ""

l = len(strNum)
i = l-1

while i>=0:
        revNum += strNum[i]
        i-=1

print(strNum == revNum)