import sys

n = int(sys.stdin.readline())

array = list()
for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))
array.append([0,0])
array = sorted(array, key = lambda x : x[0])
# print(array)

dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = 1
    for j in range(1, i):
        if array[j][1] < array[i][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1

print(n-max(dp))