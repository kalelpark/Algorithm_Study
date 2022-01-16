import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()
use = [False]*n
ans = [0]*m

def tracking(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')

        return
    
    for i in range(n):
        if use[i]:
            continue
        
        use[i] = True
        ans[index] = num[i]
        tracking(index + 1, n, m)
        use[i] = False

tracking(0, n, m)