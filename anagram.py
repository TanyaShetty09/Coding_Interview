def anagrams(s1,s2):
    if len(s1)!=len(s2):
        return False
    return sorted(s1)==sorted(s2)

s1=input("Enter the first string: ")
s2=input("Enter the second string: ")
n=anagrams(s1,s2)
if n==True:
    print("The two strings are anagrams.")
else:
    print("The two strings are not anagrams.")