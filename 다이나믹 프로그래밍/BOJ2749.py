import sys
n = int(sys.stdin.readline())
n %= (15*100000)
a, b = 0, 1
for _ in range(n):
    a, b = b % 1000000 , (a+b)% 1000000
print(a)