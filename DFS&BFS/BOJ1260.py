from collections import deque
import sys

n, m, start = map(int, sys.stdin.readline().split())
# 인접리스트 만들기
array_1 = [[] for _ in range(n+1)]
array = [False]*(n+1)

# 인접 리스트 생성 및 정렬
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    array_1[a].append(b)
    array_1[b].append(a)


for i in range(1, n+1):
    array_1[i].sort()


def dfs(x):
    array[x] = True
    ans.append(x)

    for i in array_1[x]:
        if array[i] == False:
            dfs(i)

def bfs(x):
    array[x] = True

    array_de = deque()
    array_de.append(x)

    while array_de:
        x = array_de.popleft()
        ans.append(x)
        for i in array_1[x]:
            if array[i] == False:
                array[i] = True
                array_de.append(i)

# 출력
ans = list()
dfs(start)
print(*ans)
ans = list()
array = [False]*(n+1)
bfs(start)
print(*ans)
