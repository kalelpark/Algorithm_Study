from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

n, m = map(int, input().split())
array = [list(map(int,list(input()))) for _ in range(m)]
dist = [[-1]*n for _ in range(m)]

q = deque()
q.append((0, 0))
dist[0][0] = 0

while q:
    y, x = q.popleft()

    for i in range(4):
        tmp_y = y + dy[i]
        tmp_x = x + dx[i]
        
        if 0 <= tmp_y < m and 0 <= tmp_x < n and dist[tmp_y][tmp_x] == -1:
            if array[tmp_y][tmp_x] == 0:
                dist[tmp_y][tmp_x] = dist[y][x]
                q.appendleft((tmp_y, tmp_x))
            
            else:
                dist[tmp_y][tmp_x] = dist[y][x] + 1
                q.append((tmp_y, tmp_x))

print(dist[m-1][n-1])
                