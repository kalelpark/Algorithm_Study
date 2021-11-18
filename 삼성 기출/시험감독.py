import sys

n = int(sys.stdin.readline())
my = list(map(int, sys.stdin.readline().split()))
b, c = map(int , input().split())

sum = 0
tmp = 0
for i in my:
    tap = 0
    i -= b
    tap += 1
    
    if i > 0:
        if i%c == 0:
            tap += (i//c)
        else:
            tap += ((i//c) + 1)
    sum += tap
print(sum)