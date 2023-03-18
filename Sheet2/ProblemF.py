# F. minimum string
n1, n2 = map(int, input().split())
s = input()
t = input()
if len(s) == n1 and n2 == len(t):
    if s < t:
        print(s)
    else:
        print(t)