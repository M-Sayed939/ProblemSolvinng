# B. Preparing a party
n = int(input())
arr = list(map(int, input().split()))
max = 0
min = float('inf')
for i in range(1,n):
    diff = abs(arr[i] - arr[i-1])
    if diff < min:
        min = diff
    if diff > max:
        max = diff
print(max, min,end=" ")