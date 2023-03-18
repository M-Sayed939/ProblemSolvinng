# D. Hazem Favorite game
n = int(input())
arr = list(map(int, input().split()))
c = int(input())
for i in range(n):
    if arr[i] == c:
        print(i)
        break
else:
    print(-1)