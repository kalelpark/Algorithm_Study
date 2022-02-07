import sys
import math

def bfs(i, j):
    count = 0
    bfs_array = list()
    bfs_array.append((i, j))
    visit[i][j] = True
    
    union = [(i, j)]
    sum_p = array[i][j]

    while bfs_array:
        y, x = bfs_array.pop()

        for z in range(4):
            tmp_y = y + dy[z]
            tmp_x = x + dx[z]
            if 0 <= tmp_y < n and 0 <= tmp_x < n and not visit[tmp_y][tmp_x]:
                if l <= abs(array[tmp_y][tmp_x] - array[y][x]) <= r:
                    union.append((tmp_y, tmp_x))
                    visit[tmp_y][tmp_x] = True
                    bfs_array.append((tmp_y, tmp_x))
                    sum_p += array[tmp_y][tmp_x]
    
    for y, x in union:
        array[y][x] = math.floor(sum_p / len(union))
    
    return len(union)


n, l, r = map(int, sys.stdin.readline().split())
array = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

days = 0
while True:
    visit = [[False]*n for _ in range(n)]
    rule = False
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i, j) > 1:
                    rule = True

    if not rule:
        break
    days += 1

print(days)     
                