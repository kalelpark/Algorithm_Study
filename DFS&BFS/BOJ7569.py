import sys
from collections import deque
# 파이썬 인덱스 층, 행, 열 순으로 주어집니다,
         
# 주어지는 것은 열, 행, 층
m, n, h = map(int, sys.stdin.readline().split())

array = list()

for _ in range(h):
    array.append(list(list(map(int, sys.stdin.readline().split())) for _ in range(n)))

dx = [-1, 1, 0, 0, 0, 0]
dy = [ 0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

direct = list()
for _ in range(h):
    direct.append([[-1]*m  for _ in range(n)])

start = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if array[z][y][x] == 1:
                direct[z][y][x] = 0
                start.append((z, y, x))

while start:
    z, y, x = start.popleft()
    for i in range(6):
        z1 = z + dz[i]
        y1 = y + dy[i]
        x1 = x + dx[i]
        if 0 <= z1 < h and 0 <= y1 < n and 0 <= x1 < m:
            if array[z1][y1][x1] == 0 and direct[z1][y1][x1] == -1:
                start.append((z1, y1, x1))
                direct[z1][y1][x1] = direct[z][y][x] + 1

ans = -100
for z in range(h):
    for y in range(n):
        for x in range(m):
            if array[z][y][x] == 0 and direct[z][y][x] == -1:
                ans = -1
                print(ans)
                sys.exit()
            else:
                ans = max(ans, direct[z][y][x])

print(ans)