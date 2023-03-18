# K. Mutineer letter
n = int(input())
s = input()
for i in range(n):
    if s[i].isupper():
        print(s[i], i+1)