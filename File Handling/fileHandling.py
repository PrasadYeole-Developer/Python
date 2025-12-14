# -------------------------------
# 1. OPEN A FILE
# -------------------------------
file = open("data.txt", "r")   # open for reading
file.close()


# -------------------------------
# 2. FILE MODES
# -------------------------------
"""
"r"  -> read
"w"  -> write (overwrite)
"a"  -> append
"x"  -> create new file
"""


# -------------------------------
# 3. READ ENTIRE FILE
# -------------------------------
file = open("data.txt", "r")
content = file.read()
print(content)
file.close()


# -------------------------------
# 4. READ LINE BY LINE
# -------------------------------
file = open("data.txt", "r")
for line in file:
    print(line)
file.close()


# -------------------------------
# 5. READ ONE LINE
# -------------------------------
file = open("data.txt", "r")
print(file.readline())
file.close()


# -------------------------------
# 6. WRITE TO FILE (OVERWRITE)
# -------------------------------
file = open("data.txt", "w")
file.write("Hello Python\n")
file.write("File Handling")
file.close()


# -------------------------------
# 7. APPEND TO FILE
# -------------------------------
file = open("data.txt", "a")
file.write("\nNew line added")
file.close()


# -------------------------------
# 8. BEST PRACTICE (with statement)
# -------------------------------
with open("data.txt", "r") as file:
    print(file.read())
# file auto-closed


# -------------------------------
# 9. FILE NOT FOUND HANDLING
# -------------------------------
try:
    with open("abc.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found")


# -------------------------------
# 10. CHECK FILE EXISTS
# -------------------------------
import os

if os.path.exists("data.txt"):
    print("File exists")
else:
    print("File does not exist")


# -------------------------------
# 11. COUNT LINES IN FILE
# -------------------------------
with open("data.txt", "r") as file:
    print("Lines:", len(file.readlines()))


# -------------------------------
# 12. COUNT WORDS IN FILE
# -------------------------------
with open("data.txt", "r") as file:
    words = file.read().split()
    print("Words:", len(words))


# -------------------------------
# 13. COPY ONE FILE TO ANOTHER
# -------------------------------
with open("data.txt", "r") as f1, open("copy.txt", "w") as f2:
    f2.write(f1.read())


# -------------------------------
# END OF FILE HANDLING NOTES
# -------------------------------
