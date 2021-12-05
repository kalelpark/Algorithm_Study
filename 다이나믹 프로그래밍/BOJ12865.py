import sys

N, K = map(int, sys.stdin.readline().split())
# 1부터 시작하기
items = [[0,0]]
# item 저장
for _ in range(N):
    items.append(list(map(int, sys.stdin.readline().split())))

# 1부터 시작하기
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,K+1):
        if j >= items[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - items[i][0]] + items[i][1])
        else:
            dp[i][j] = dp[i-1][j]


print(dp[N][K])
