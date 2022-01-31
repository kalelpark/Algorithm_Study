import sys
sys.setrecursionlimit(1000000)
test_case = int(sys.stdin.readline())



for _ in range(test_case):
    n, m = map(int, sys.stdin.readline().split())

    check = [0]*(n+1)
    array = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        array[a].append(b)
        array[b].append(a)

    def dfs(x, c):
        check[x] = c
        for y in array[x]:
            if check[y] == 0:
                dfs(y, 3-c)
    
    ans  = True

    for i in range(n):
        if check[i] == 0:
            dfs(i, 1)
    
    for i in range(n):
        for j in array[i]:
            if check[j] == check[i]:
                ans = False
    
    if ans:
        print('YES')
    else:
        print('NO')
