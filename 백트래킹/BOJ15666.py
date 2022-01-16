import sys

n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num.sort()

ans = [0]*m
array = list()
def tracking(index, n, m):
    if index == m:
        tmp = ' '.join(map(str, ans))

        if tmp in array:
            return
        else:
            array.append(tmp)
            return
    
    for i in range(n):
        if index == 0:
            ans[index] = num[i]
            tracking(index + 1, n, m)
        elif ans[index-1] <= num[i]:
            ans[index] = num[i]
            tracking(index + 1, n, m)
        else:
            continue

tracking(0, n, m)
for zz in array:
    print(zz)