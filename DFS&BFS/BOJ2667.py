import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
array = list()

for _ in range(m):
    array.append(list(map(int, sys.stdin.readline().split())))

direc = [[-1]*n for _ in range(m)]

stora = deque()

for i in range(m):
    for j in range(n):
        if array[i][j] == 1:
            direc[i][j] = 0
            stora.append((i,j))

while stora:
    y, x = stora.popleft()

    for y1, x1 in ([y-1, x], [y+1, x], [y, x+1], [y, x-1]):
        if 0 <= y1 < m and 0 <= x1 < n:
            if array[y1][x1] == 0 and direc[y1][x1] == -1:
                stora.append((y1,x1))
                direc[y1][x1] = direc[y][x] + 1


ans = max([max(row) for row in direc])
for i in range(m):
    for j in range(n):
        if array[i][j] == 0 and direc[i][j] == -1:
            ans = -1

print(ans)