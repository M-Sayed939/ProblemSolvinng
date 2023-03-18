# C. Increasing Progress
n=int(input())
arr=list(map(int, input().split()))
flag = 0
i = 1
while i < len(arr):
    if (arr[i] < arr[i - 1]):
        flag = 1
    i += 1
if (not flag):
    print("YES")
else:
    print("NO")