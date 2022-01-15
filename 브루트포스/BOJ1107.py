import sys

num = int(sys.stdin.readline())

broke_count = int(sys.stdin.readline())
broken_array = [False for _ in range(10)]


if broke_count > 0:
    array = list(map(int, sys.stdin.readline().split()))
else:
    array = []

# Broken Array
for i in array:
    broken_array[i] = True

def possible(c):
    if c == 0:
        if broken_array[0]:
            return 0
        else:
            return 1

    l = 0
    while c > 0:
        if broken_array[c%10]:
            return 0
        l += 1
        c //= 10

    return l

ans = abs(num - 100)
for i in range(0 , 1000001):
    c = i
    l = possible(c)
    if l > 0:
        press = abs(c-num)
        if ans > l + press:
            ans = l + press

print(ans)
