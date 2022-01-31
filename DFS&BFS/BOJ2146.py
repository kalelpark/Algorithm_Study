from collections import deque
import sys
# sys.setrecursionlimit(10000)

def bfs(i , j, num):
    check[i][j] = num
    
    for z in range(4):
        tmp_i = i + dy[z]
        tmp_j = j + dx[z]

        if 0 <= tmp_i < n and 0 <= tmp_j < n:
            if check[tmp_i][tmp_j] == -1:
                if array[i][j] == array[tmp_i][tmp_j]:
                    bfs(tmp_i , tmp_j, num)

n = int(sys.stdin.readline())
array = list()

for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

check = [[-1]*n for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

count = 0

for i in range(n):
    for j in range(n):
        if check[i][j] == -1 and array[i][j] != 0:
            count += 1
            bfs(i, j, count)
        if check[i][j] == -1 and array[i][j] == 0:
            bfs(i, j, 0)

ans = 10000
for num in range(1, count + 1):

    storage = deque()
    array = [[-1] * n for _ in range(n)]

    for i in range(n):
      for j in range(n):
          if check[i][j] == num:
              array[i][j] = 0
              storage.append((i, j))
    
    while storage:
        y, x = storage.popleft()

        for z in range(4):
            tmp_y = y + dy[z]
            tmp_x = x + dx[z]

            if 0 <= tmp_y < n and 0 <= tmp_x < n:
                if check[tmp_y][tmp_x] == 0 and array[tmp_y][tmp_x] == -1:
                    storage.append((tmp_y, tmp_x))
                    array[tmp_y][tmp_x] = array[y][x] + 1
                elif check[tmp_y][tmp_x] != 0 and check[tmp_y][tmp_x] != num:
                    ans = min(ans, array[y][x])
        
print(ans)