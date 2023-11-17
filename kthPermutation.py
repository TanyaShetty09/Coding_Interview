import itertools

def kth_permutation(n, k):
    permutations = list(itertools.permutations(range(1, n+1)))
    return ''.join(map(str, permutations[k-1]))

# Taking user input for n and k
n = int(input("Enter the value of n: "))
k = int(input("Enter the value of k: "))

result = kth_permutation(n, k)
print(f"The {k}th permutation of numbers from 1 to {n} is: {result}")