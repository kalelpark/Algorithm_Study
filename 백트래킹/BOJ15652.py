import sys

# 자연수 N과 M이 주어진 경우, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
#     
#     1부터 N까지 자연수 중에서 M개를 고른 수열
#     같은 수를 여러 번 골라도 된다.
#     고른 수열은 비내림차순이어야 한다.
n , m = map(int, sys.stdin.readline().split())

ans = [0]*m

def Tracking(index, start, n, m):
    
    if index == m:
        sys.stdout.write(' '.join(map(str, ans)) + '\n')

        return
    
    for i in range(start, n+1):
        ans[index] = i
        Tracking(index+1, i, n, m)
    

Tracking(0, 1, n, m)