import sys

d = int(sys.stdin.readline())
dp = [0]*(d+1)

day = [0]
point = [0]

# 기간별로 값 넣기
for _ in range(d):
    n, m = map(int, sys.stdin.readline().split())

    day.append(n)
    point.append(m)

# 배열 넣기
for i in range(1,d+1):
    r = 0
    t = day[i]
    s = point[i]
    if (i + t -1) <= d:
        r = s
    else:
        pass
    
    # 이전 날짜의 값에서 합 구하기
    tmp = 0
    for z in range(i):
        if dp[z] > tmp:
            tmp = dp[z]

    if (i + t -1) <= d:            
        r += tmp
        dp[i + t -1] = max(dp[i + t -1], r)
    else:
        pass

print(max(dp))

// https://jrc-park.tistory.com/119 더 깔끔한 코드 참고하세욤

