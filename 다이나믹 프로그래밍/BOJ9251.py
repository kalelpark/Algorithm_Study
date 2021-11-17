# LCS(최장 공통 부분 수열)
import sys
str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

n = len(str1)
m = len(str2)

# 배열 생성하기
dp = [[0]*(m+1) for _ in range(n+1)]
 
# 배열을 벗어나는 것을 방지하기 위해 0을 한칸 더 추가하는 것이다.
ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        if dp[i][j] > ans:
            ans = dp[i][j]

print(ans)


# 반례
# VREGDFELK
# VLSKD
# qsdferrfgtfsawfsefeesgdtdrgthyytfgfddsdawdwd
# efvs