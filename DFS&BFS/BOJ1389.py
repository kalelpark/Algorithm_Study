from collections import deque
import sys
n, m = map(int, sys.stdin.readline().split())

array = [[] for _ in range(n+1)]
ans = 10000
real_num = 1
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    array[a].append(b)
    array[b].append(a)

for i in range(1, n+1):
    check = [1000] * (n+1)

    bfs_array = deque()
    check[0] = 0    
    check[i] = 0

    bfs_array.append(i)
    while bfs_array:
        z = bfs_array.popleft()
        for min in array[z]:
            if check[min] == 1000:
                if check[min] > (check[z] + 1):
                    check[min] = check[z] + 1
                bfs_array.append(min)
    
    if ans > sum(check):
        ans = sum(check)
        real_num = i

print(real_num)



    
