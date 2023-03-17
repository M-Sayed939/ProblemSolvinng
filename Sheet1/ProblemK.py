n = int(input())
# n=5
# n=n//2 ->2.5 - 0.5
# print(n) ->2
for i in range(1, n+1):
    if i <= n//2: #the odd number before n
        star = "*" * i
    else:
        star = "*" * (n-i+1)
    print(star)
