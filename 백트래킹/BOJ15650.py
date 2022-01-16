import sys

n, m = map(int, sys.stdin.readline().split())

use = [False]*(n+1)
ans = [0]*m

def Tracking(index, n, m):
    
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    

    for i in range(1, n + 1):
        if use[i]:
            continue

        use[i] = True
        
        if index == 0:
            ans[index] = i
            Tracking(index+1, n, m)
            use[i] = False
        elif ans[index - 1] < i:
            ans[index] = i
            Tracking(index+1, n, m)
            use[i] = False
        else:
            use[i] = False
            continue


Tracking(0, n, m)