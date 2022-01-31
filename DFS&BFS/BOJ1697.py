import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
array = deque()

t_array = [0 for _ in range(100001)]

array.append(n)

while array:
    now = array.popleft()

    if now == m:
        print(t_array[now])
        break

    for i in (now-1, now+1, now*2):
        # 들리지 않은 경우를 기준으로 한 것
        if 0 <= i <= 100000 and t_array[i] == 0:
            t_array[i] = t_array[now] + 1
            array.append(i)