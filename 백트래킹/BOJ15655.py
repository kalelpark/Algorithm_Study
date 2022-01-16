import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

ans = [0]*m

def tracking(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')

        return
    
    for i in range(n):
        if index == 0:
            ans[index] = num[i]
            tracking(index + 1, n, m)
        elif ans[index - 1] < num[i]:
            ans[index] = num[i]
            tracking(index + 1, n, m)
        else:
            continue
            
tracking(0, n, m)