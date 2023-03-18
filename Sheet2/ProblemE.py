# E. Debugging duck
n = int(input())
a = list(map(int, input().split()))
ex = a[0]
ch = a[0]
for i in range(1, n):
    if a[i] > ex:
        ex = a[i]
    elif a[i] < ch:
        ch = a[i]
print(ex, ch, end=" ")