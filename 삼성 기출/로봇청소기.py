import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

# 방향과 관련된 문제는 따로 좌표를 형성하자.
dx = [-1, 0, 1, 0]
dy = [0, 1 , 0, -1]

array = list()

for _ in range(n):
    array.append(list(map(int, sys.stdin.readline().split())))

def turn_left():
    global d
    d = (d-1)%4

count = 1
# 방문처리
array[r][c] = 3

while True:
    check = False   # 방문 칸 유무 파악
    for _ in range(4):
        # 1, 1
        turn_left()
        nr = r + dx[d]
        nc = c + dy[d]
        if 0 <= nr < n and 0 <= nc <= m:
            if array[nr][nc] == 0:
                count += 1
                array[nr][nc] = 3
                r, c = nr, nc
                check = True
                break
    if not check:
        nr = r - dx[d]
        nc = c - dy[d]
        if 0 <= nr < n and 0 <= nc <= m:
            if array[nr][nc] == 3:
                r, c = nr, nc
            elif array[nr][nc] == 1:
                print(count)
                break
        else:
            print(count)
            break



#     0
#   3   1
#     2
# 