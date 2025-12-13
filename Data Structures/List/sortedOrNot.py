numbers = [3,4,2,6,4,7,8,4,2]

sortedNumbers = [1,2,3,4]

def checkSorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            print("Unsorted")
            break
    else: print("Sorted")

checkSorted(numbers)
checkSorted(sortedNumbers)