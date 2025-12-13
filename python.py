a = "a";
b = "12";
c = 12;
print("Hello");
print(ord(a)); # ord() function to get unicode of any charactor
print(chr(ord(a))); # chr() function to get charactor out of unicode

# String Indexing : 
string = "Number";
print(string[0]);
print(string[-2]);

# String Slicing : str[start:stop:steps] // Will stop on previous element of given
print(string[1:4:1]);
print(string[0:4:2]);

# type conversion my main 4 str() bool() int() float()
print(str(c));
print(int(b));

# input // default datatype is string
name = input("Enter name: ");
print(f"Hello {name}");

# for loop and range 
"""
range takes (start, stop, steps), if start not given 0 will be considered, if steps not then 1 will be considered, always have to give stop and will end just before given value
"""
for i in range(1,6):
    print(i);
print("Loop Separation!");
for i in range(6):
    print(i);

strLength = "Nature";
print("Length of String:",len(strLength));

# iterating over string using indexes and using chars
for i in (range(len(strLength))):
    print(strLength[i]);
print("Loop Separation!");
for char in strLength:
    print(char);

# if-elif ladder
n = int(input("Enter input: "));
if n<0:
    print("Negative.");
elif n>0:
    print("Positive.");
else:
    print("Zero.");