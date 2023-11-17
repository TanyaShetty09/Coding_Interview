def first_and_last(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            start = i
            while i + 1 < len(arr) and arr[i + 1] == target:
                i += 1
            return [start, i]
    return [-1, -1]

target = int(input("Enter the target number: "))
n = int(input("Enter the number of elements in the array: "))

arr = []
print("Enter the array elements")
for i in range(0, n):
    l = int(input())
    arr.append(l)

i, j = first_and_last(arr, target)
print(i, j)
