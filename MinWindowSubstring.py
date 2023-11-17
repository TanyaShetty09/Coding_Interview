from collections import Counter

def contains_all(freq1, freq2):
    for ch in freq2:
        if freq1[ch] < freq2[ch]:
            return False
    return True

def min_window(s, t):
    n, m = len(s), len(t)
    if m > n or m == 0:
        return ""

    freqt = Counter(t)
    shortest = '*' * (n + 1)

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            sub = s[i:i + length]
            freqs = Counter(sub)

            if contains_all(freqs, freqt) and length < len(shortest):
                shortest = sub
    
    return shortest if len(shortest) <= n else ""

# Taking user input for strings s and t
s = input("Enter string s: ")
t = input("Enter string t: ")

result = min_window(s, t)
if result:
    print(f"The minimum window containing all characters of '{t}' in '{s}' is: {result}")
else:
    print("No such window exists.")
