def kth_Largest(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n - k]

n = int(input("Enter the number of elements in the array: "))
arr = []
print("Enter the array elements:")
for i in range(n):
    element = int(input())
    arr.append(element)

k = int(input("Enter the value of k: "))

result = kth_Largest(arr, k)
print(f"The {k}th largest element in the array is: {result}")
