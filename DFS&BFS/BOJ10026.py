import sys
# sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline())
array = list()
for _ in range(n):
    array.append(list(map(str, sys.stdin.readline().rstrip())))

check = [[False]*n for _ in range(n)]

dy = [-1, 1, 0, 0]
dx = [ 0, 0, -1, 1]

def bfs(i, j):
    check[i][j] = True
    
    for z in range(4):
        tmp_y = i + dy[z]
        tmp_x = j + dx[z]
        if 0 <= tmp_y < n and 0 <= tmp_x < n:
            if not check[tmp_y][tmp_x]:
                if array[tmp_y][tmp_x] == array[i][j]:
                    bfs(tmp_y, tmp_x)

count = 0
for i in range(n):
    for j in range(n):
        if not check[i][j]:
            bfs(i, j)
            count += 1
            
tmp = count


for i in range(n):
    for j in range(n):
        if array[i][j] == 'R':
            array[i][j] = 'G'

# print(array)

count = 0
check = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not check[i][j]:
            bfs(i, j)
            count += 1

tmp_1 = count

print(tmp, tmp_1)