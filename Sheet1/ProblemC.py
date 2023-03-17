# Given two integers n and x Print all numbers from 1 to n which are divisible by x separated by white spaces.
n, x = map(int, input().split())
divisble = []
for i in range(1, n+1):
    if i % x == 0:
        divisble.append(str(i))
if divisble:
    print(" ".join(divisble))
else:
    print(-1)