import sys

n = int(sys.stdin.readline())

dp = [0, 1, 2, 3, 1]

for i in range(5, n+1):
    
    num = 1
    tmp1 = 1_000_000
    while (num ** 2) <= i:
        if 1 + dp[i - (num**2)] < tmp1:
            tmp1 = 1 + dp[i - (num**2)]
        num += 1

    dp.append(tmp1)

print(dp[n])