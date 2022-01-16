import sys
# 같은 수를 여러번 선택해도 되며, 중복되는 수열은 X 사전 순으로 증가
n , m = map(int, sys.stdin.readline().split())

ans = [0]*m

def Tracking(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')
        return
    
    for i in range(1, n+1):
        ans[index] = i
        Tracking(index+1, n, m)


Tracking(0, n, m)
