import sys

test_case =int(sys.stdin.readline())

dp = [0 for _ in range(1000001)]

for i in range(1,1000001):
    for j in range(i, 1000001, i):
        dp[j] += i
    dp[i] += dp[i-1]
    
for _ in range(test_case):
    n = int(sys.stdin.readline())
    print(dp[n])