import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

dp = [[0 for _ in range(n)] for __ in range(n)]

for i in range(1, n):
    for j in range(n-i):

        if i == 1:
            dp[j][j+i] = array[j][0]*array[j][1]*array[j+i][1]
            continue

        dp[j][j+i] =  2**32
        for k in range(j, j + i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k] + dp[k+1][j+i] + array[j][0] * array[k][1] * array[j+i][1])

print(dp[0][n-1])