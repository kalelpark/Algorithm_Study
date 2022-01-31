from collections import deque

y, x = map(int, input().split())
array = [list(map(int, input())) for _ in range(y)]
check = [[[0] * 2 for _ in range(x)] for _ in range(y)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def Bfs(start_x, start_y, iscrash, check, array):
    #crash 0: 벽안부시고 가는경우, 1: 부신 경우
    queue = deque()
    queue.append((start_x, start_y, iscrash))
    check[start_x][start_y][iscrash] = 1

    while queue:
        tm_x, tm_y, crash = queue.popleft()
        if tm_x == y - 1 and tm_y == x - 1:
            return check[tm_x][tm_y][crash]
        for z in range(4):
            tmp_x = tm_x + dx[z]
            tmp_y = tm_y + dy[z]

            if  0 <=tmp_x < y and 0<= tmp_y < x:
                if array[tmp_x][tmp_y] == 0 and check[tmp_x][tmp_y][crash] == 0:
                    queue.append((tmp_x, tmp_y, crash))
                    check[tmp_x][tmp_y][crash] = check[tm_x][tm_y][crash] + 1
                if array[tmp_x][tmp_y] == 1 and crash == 0:
                    queue.append((tmp_x, tmp_y, crash + 1))
                    check[tmp_x][tmp_y][crash + 1] = check[tm_x][tm_y][crash] + 1

    return -1

print(Bfs(0, 0, 0, check, array))