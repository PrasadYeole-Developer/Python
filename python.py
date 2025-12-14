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

# functions
def greet(name):
    print(f"Hello, {name}")
greet("Jack")

# types of arguments
# 1 
def add(a,b):
    return a+b

print(add(3,5));

# 2
def introduce(name, age):
    print(f"Hello I'm {name} and I'm {age} years old.")

introduce(age=21, name="Prasad");

# 3 
def greet(name="Guest"):
    print(f"Hello, {name}")

greet() # if not provided will print Guest
greet("Bob") # this will print Hello, Bob

# Data Structures
## List : ordered, mutable, duplicates, heterogeneous
fruits = ["apple", "banana", "cherry"]
numbers = [10,20,30,40]
print(numbers)
numbers[1] = 99
print(numbers)

## Tuple : ordered, immutable, duplicates, heterogeneous, has only 2 methods count and index
nums = (1,2,3,4,53,22,4)
print(nums.index(4))
print(nums.count(4))

## Set : unordered, mutable, heterogeneous, duplicates, can not be traversed, has powerful methods
s = {1,2,3,4,5,6,7,8}
print(s)
s.add(9)
s.remove(3) # will give error if element not found
print(s)
s.discard(10) # won't give error if element not found
s.pop() # removes random element
s.clear()
print(s)
s = {1,2,3}
print(s)

# Operations on 2 sets
## Union (A|B) , intersection(A&B), difference(A-B), symmetricDifference(A^B)

A = {1,2,3}
B = {3,4,5}
unionSet = A.union(B)
intersectionSet = A.intersection(B)
differenceSet = A.difference(B)
symmetricDifferenceSet = A.symmetric_difference(B)

print("Union", unionSet)
print("Intersection", intersectionSet)
print("Difference", differenceSet)
print("Symmetric difference", symmetricDifferenceSet)

## Dictionary : mutable, insertion order, duplicate values, unique keys, heterogeneous
student = {"name":"Jacob", "age":28}
print(student)
print(student["name"])
for i in student:
    print(f"{i} : {student[i]}")

"""
| Method     | Use                |
| ---------- | ------------------ |
| `keys()`   | get all keys       |
| `values()` | get all values     |
| `items()`  | key-value pairs    |
| `update()` | merge dictionaries |
| `clear()`  | remove all items   |
"""