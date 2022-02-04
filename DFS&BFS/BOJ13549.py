import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maxlen = 100000

check = [-1]*(maxlen + 1)
q = deque()
q.append(n)
check[n] = 0

while q:
    num = q.popleft()

    if num == m:
        print(check[m])
        break

    if 2*num <= 100000 and check[2*num] == -1:
        check[2*num] = check[num]
        q.append(2*num)   
        
    if num - 1 >= 0 and check[num -1] == -1:
        check[num -1] = check[num] + 1
        q.append(num -1)

    if num + 1 <= 100000 and check[num + 1] == -1:
        check[num + 1] = check[num] + 1
        q.append(num + 1)

             