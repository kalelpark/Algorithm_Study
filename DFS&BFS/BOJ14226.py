import sys
from collections import deque

n = int(sys.stdin.readline())
dict = [[-1]*(n+1) for _ in range(n+1)]
q = deque()
q.append((1, 0))
dict[1][0] = 0

while q:
    s, c = q.popleft()

    # 복사
    if dict[s][s] == -1:
        dict[s][s] = dict[s][c] + 1
        q.append((s, s))
    
    # 붙여넣기
    if s + c <= n and dict[s+c][c] == -1:
        dict[s+c][c] = dict[s][c] + 1
        q.append((s+c, c))
    
    # 삭제
    if s - 1 >= 0 and dict[s-1][c] == -1:
        dict[s-1][c] = dict[s][c] + 1
        q.append((s-1, c))


ans = 1e9
for i in range(n+1):
    if dict[n][i] != -1:
        if ans > dict[n][i]:
            ans = dict[n][i]
print(ans)
