import sys

n, m = map(int, sys.stdin.readline().split())
# 재귀 순열에서, 중복없이 이므로,
# index를 활용하면 됩니다.
use = [False]*(n+1)

# 결과를 저장
a = [0]*m

def Tracking(index, n, m):
    if index == m:
        sys.stdout.write(' '.join(map(str, a)) + '\n')
        return
    
    # 사전순으로 출력되는 것이다.
    for i in range(1, n + 1):
        if use[i]:
            continue

        use[i] = True
        a[index] = i
        # 재귀 활용
        Tracking(index+1, n, m)
        use[i] = False


Tracking(0, n, m)