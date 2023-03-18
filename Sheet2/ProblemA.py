# A. Escape Room
n = int(input())
TwoDimArr = [[1]*n for k in range(n)]
for i in range(1, n):
    for j in range(1, n):
        TwoDimArr[i][j] = TwoDimArr[i-1][j] + TwoDimArr[i][j-1]
for i in range(n):
    for j in range(n):
        print(TwoDimArr[i][j], end=' ')
    print()
#     https://stackoverflow.com/questions/62528848/print-a-matrix-using-for-loop-python