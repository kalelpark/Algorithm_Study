import sys
n, m = map(int, sys.stdin.readline().split())

# 간섭 리스트 생성하기
edge = []
# 인접 행렬 만들기
a = [[False]*n for _ in range(n)]
# 인접 리스트 생성하기
g = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    edge.append((u,v))    
    edge.append((v,u))    
    # 인접 행렬 연결된 부분 참으로 만들기
    a[u][v] = a[v][u] = True
    g[u].append(v)
    g[v].append(u)        

# 간선은 양밯향이므로, bidirectional 이므로, 간선을 두배해줘야 합니다.
m *= 2
for i in range(m):
    for j in range(m):
        A, B = edge[i]
        C, D = edge[j]
        if A == B or A == C or A == D or B == C or B == D or C == D:
            continue

        if not a[B][C]:
            continue

        for E in g[D]:
            if A == E or B == E or C == E or D == E:
                continue

            print(1)
            sys.exit()
print(0)
