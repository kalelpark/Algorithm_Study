import sys

def pisano(m):
    n2, n3 = 0, 1
    count = 0
    while True:
        n2, n3 = n3 % m , (n2 + n3)%m
        count += 1
        if n2 == 0 and n3 == 1:
            break
    
    return count


test_case = int(sys.stdin.readline())

for _ in range(test_case):
    n, m = map(int, sys.stdin.readline().split())

    re_nu = pisano(m)
    print(n, re_nu)
