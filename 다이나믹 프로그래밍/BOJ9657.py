import sys
num = int(sys.stdin.readline())

dp = [0]*(num + 5)

dp[1] = 1   # 선공이 이기는 경우
dp[2] = 0   # 후공이 이기는 경우
dp[3] = 1   # 선공이 이기는 경우
dp[4] = 1   # 선공이 이기는 경우

for i in range(5 , num+1):
    if dp[i-4] == 0 or dp[i-3] == 0 or dp[i-1] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[num] == 1:
    print('SK')
else:
    print('CY')