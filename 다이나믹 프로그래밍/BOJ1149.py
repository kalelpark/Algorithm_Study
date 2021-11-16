# 1번째 집의 색과 2번쨰 집의 색이 달라야 한다.
# 그러므로, 1번째 집의 색과 다른 색의 집들 중에서 가장 작은 최솟값을 선택해서 값을 지속적으로 더해 나가면 돤다.

import sys
num = int(sys.stdin.readline())

# 비용 지정
dp = list()
for _ in range(num):
    dp.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, num):
    dp[i][0] = min(dp[i-1][1] ,dp[i-1][2]) + dp[i][0]
    dp[i][1] = min(dp[i-1][0] , dp[i-1][2]) + dp[i][1]
    dp[i][2] = min(dp[i-1][1] , dp[i-1][0]) + dp[i][2]


print(min(dp[num-1]))
