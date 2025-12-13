string = input("Enter input: ");
revString = "";
l = len(string);
for i in range(l):
    revString += string[l-i-1];

print("Reversed string: " + revString);
