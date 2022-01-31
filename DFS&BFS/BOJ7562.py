import sys
from collections import deque

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n = int(sys.stdin.readline())
    show = deque()    
    array = [[-1]*n for _ in range(n)]
    ans = 1e9
    st_y, st_x = map(int, sys.stdin.readline().split())
    fi_y, fi_x = map(int, sys.stdin.readline().split())
    array[st_y][st_x] = 0
    show.append([st_y, st_x])


    while show:

        y1, x1 = show.popleft()

        for a, b in ([y1 - 2, x1 -1], [y1 - 2, x1 + 1], [y1 - 1, x1 + 2], [y1 + 1, x1 + 2], [y1 + 2, x1 -1], [y1 + 2, x1 + 1], [y1 + 1, x1 - 2], [y1 -1, x1 -2]):
            if 0 <= a < n and 0 <= b < n and array[a][b] == -1:
                array[a][b] = array[y1][x1] + 1

                show.append([a, b])
                if a == fi_y and b == fi_x:
                    tmp = array[a][b]

                    ans = min(tmp, ans)

    print(ans)