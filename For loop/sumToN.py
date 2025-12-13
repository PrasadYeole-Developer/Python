n = int(input("Enter input: "));
s = 0;
for i in range(1, n+1):
    s = s+i;
print(s);

# OR

n = int(input("Enter input: "));
s = 0;
for i in range(1, n+1):
    s += i;
print(s);