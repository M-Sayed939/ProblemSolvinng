# N. waiting line
n = int(input())
s = input()
s1 = ""
for i in range(n):
    if i == 0 or s[i] != s[i - 1]:
        s1 += s[i]
print(s1)