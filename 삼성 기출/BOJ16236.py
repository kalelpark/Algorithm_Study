import heapq
import sys
from collections import deque

def bfs(x, y):
    global res, eat, shark_size
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while True:
        queue = deque([(x, y, 0)])
        visited = [[False]*n for _ in range(n)]
        visited[x][y] = True
        heap = []
        flag = n**2

        while queue:
            a, b, cnt = queue.popleft()

            if cnt > flag:
                break

            for i in range(4):
                xx = a + dx[i]
                yy = b + dy[i]

                if 0 <= xx < n and 0 <= yy < n and visited[xx][yy] == False and board[xx][yy] <= shark_size:
                    if board[xx][yy] < shark_size and board[xx][yy] != 0:
                        heapq.heappush(heap, (xx, yy, cnt + 1))
                        flag = cnt
                    
                    queue.append([xx, yy, cnt + 1])
                    visited[xx][yy] = True

        if len(heap) > 0:
            x, y, move = heapq.heappop(heap)
            res += move
            eat += 1
            board[x][y] = 0

            if eat == shark_size:
                shark_size += 1
                eat = 0
        
        else:
            break

n = int(sys.stdin.readline())
board = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))
shark_size = 2
res = 0  # 최소 이동 시간
eat = 0  # 먹은 물고기 수

for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            board[i][j] = 0
            bfs(i, j)
            break

print(res)