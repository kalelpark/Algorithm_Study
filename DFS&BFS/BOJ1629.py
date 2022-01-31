import sys

n, m = map(int, sys.stdin.readline().split())

# 색상 배열
color = list()
for _ in range(n):
    color.append(list(map(str, sys.stdin.readline().rstrip())))

# 방문 확인
check = [[False]*m for _ in range(n)]

# 4가지 경로 설정
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# DFS 지정
def dfs(y, x, qy, qx, col):
    # 만약 이전에 방문한 경우가 있는 경우 즉 4번째이상일 때 방문 하는 경우 return True
    if check[y][x]:
        return True
    
    # 방문 확인
    check[y][x] = True
    # 경로 지정
    for z in range(4):
        # 4가지 경로 설정
        tmp_y = y + dy[z]    
        tmp_x = x + dx[z]    
        
        # 공간 내에서 이동하기
        if 0 <= tmp_y < n and 0 <= tmp_x < m:
            
            # 이전의 위치와 다르고, 이전의 색상과 내가 갈곳의 색상이 동일한 경우
            # if (tmp_x != qx or tmp_y != qy) and (color[qy][qx] == color[tmp_y][tmp_x]):
                # if dfs(tmp_y, tmp_x, y, x):
                    # return True
            if (tmp_y, tmp_x) == (qy, qx):
                continue
            if color[tmp_y][tmp_x] == col:
                if dfs(tmp_y, tmp_x, y, x, col):
                    return True

    return False

# 반복문
for i in range(n):
    for j in range(m):
        # 아직 방문을 안한 경우로 진행
        if not check[i][j]:
            tmp = dfs(i, j, -1, -1, color[i][j])

        if tmp:
            print('YES')
            sys.exit()

print('NO')

# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# n,m = map(int,input().split())
# a = [input() for _ in range(n)]
# check = [[False]*m for _ in range(n)]
# def go(x, y, px, py, color):
#     if check[x][y]:
#         return True
#     check[x][y] = True
#     for k in range(4):
#         nx,ny = x+dx[k],y+dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if (nx,ny) == (px,py):
#                 continue
#             if a[nx][ny] == color:
#                 if go(nx,ny,x,y,color):
#                     return True
#     return False
# for i in range(n):
#     for j in range(m):
#         if check[i][j]:
#             continue
#         ok = go(i, j, -1, -1, a[i][j])
#         if ok:
#             print('Yes')
#             exit()
# print('No')