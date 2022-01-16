import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

use = [False]*(n+1)
ans = [0]*m

array = list()

def tracking(index,start,  n, m):
    if index == m:
        tmp = ' '.join(map(str, ans))

        if tmp in array:
            return
        else:
            array.append(tmp)
            return
    
    for i in range(start, n):
        
        if use[i]:
            continue

        use[i] = True
        ans[index] = num[i]

        tracking(index+1, i, n, m)
        use[i] = False

tracking(0, 0, n, m)

for zz in array:
    print(zz)