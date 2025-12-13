for i in range(6):
    if i == 3:
        break;
    print(i);

print("Loop Separation!");

for i in range(6):
    if i == 3:
        continue;
    print(i);

print("Loop Separation!");

# Else // else will only work if loop got successfully completed without break
for i in range(3):
    print(i);
else:
    print("Loop ended successfully."); # Will work
for i in range(3):
    if i == 2:
        break;
    print(i);
else:
    print("Loop ended successfully."); # Won't work

## Use case : 
for i in range(20):
    if i == 40:
        print("Element found")
        break;
else:
    print("Not found!");
