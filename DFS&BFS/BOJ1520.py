import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    if y == n-1 and x == m-1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for z in range(4):
        tmp_y = y + dy[z]
        tmp_x = x + dx[z]
        if 0 <= tmp_y < n and 0 <= tmp_x < m and array[y][x] > array[tmp_y][tmp_x]:
            dp[y][x] += dfs(tmp_y, tmp_x)

    return dp[y][x]

dy = [-1, 1, 0, 0]
dx = [0, 0,-1, 1]

n, m = map(int, sys.stdin.readline().split())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[-1]*m for _ in range(n)]
print(dfs(0, 0))