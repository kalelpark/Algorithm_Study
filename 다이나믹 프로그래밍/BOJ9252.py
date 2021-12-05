import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

n = len(str1)
m = len(str2)

t = 0

dp = [['']*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = str(dp[i-1][j-1]) + str(str2[j-1])
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = str(dp[i-1][j])
            else:
                dp[i][j] = str(dp[i][j-1])
            # dp[i][j] = max((dp[i-1][j]), dp[i][j-1])

        if len(dp[i][j]) > t:
            ans = str(dp[i][j])
            t = len(dp[i][j])

print(t)
if t == 0:
    pass
else:
    print(ans)

# print(dp)
# print(t)
# c ='a' + 'b'
# print(c)