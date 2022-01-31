import sys
from collections import deque

def bfs(y, x):
    q = deque()
    q.append([y, x])
    while q:
        y, x = q.popleft()
    
        for y1, x1 in ([y+1, x-1], [y+1, x], [y+1, x+1], [y, x-1], [y, x+1], [y-1, x-1], [y-1, x], [y-1, x+1]):
            if 0 <= y1 < m and 0 <= x1 < n:
                if array[y1][x1] == 1:
                    q.append([y1, x1])
                    array[y1][x1] = 0

    return

while True:
    n , m = map(int, sys.stdin.readline().split())
    
    if n == 0 and m == 0:
        break
    
    array = list()
    for _ in range(m):
        array.append(list(map(int , sys.stdin.readline().split())))

    count = 0

    for i in range(m):
        for j in range(n):
            if array[i][j] == 1:
                array[i][j] = 0
                bfs(i, j)
                count += 1

    print(count)
