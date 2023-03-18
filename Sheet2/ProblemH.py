# H. mountains and lows
n = int(input())
arr = list(map(int, input().split()))
local_max = 0
local_min = 0
for i in range(1, n-1):
    if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
        local_max += 1
    elif arr[i] < arr[i-1] and arr[i] < arr[i+1]:
        local_min += 1
print(local_max, local_min,end=" ")