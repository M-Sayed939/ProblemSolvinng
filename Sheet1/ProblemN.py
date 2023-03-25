# N. Glass hour
n = int(input())
for i in range((n+1) // 2):
    print(" " * i + "*" * (n - 2 * i) + " " * i)
for i in range((n-1) // 2, -1, -1):
    print(" " * i + "*" * (n - 2 * i) + " " * i)