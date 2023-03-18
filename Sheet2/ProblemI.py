# I. Is it Palindrome?
n = int(input())
s = input()
i = 0
j = n-1
while i < j:
    if s[i] != s[j]:
        print("NO")
        break
    i = i+1
    j = j-1
else:
    print("YES")