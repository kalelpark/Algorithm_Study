import sys

result = 0
def re_spuared(n, x, y):
    global result
    
    if x == r and y == c:
        print(int(result))
        sys.exit()

    if n == 1:
        result += 1
        return

    if not (x <= r < x + n and y <= c < y + n):
        result += n * n
        return

    re_spuared(n / 2, x, y)
    re_spuared(n / 2, x, y + n / 2)
    re_spuared(n / 2, x + n / 2, y)
    re_spuared(n / 2, x + n / 2, y + n / 2)


n, r, c = map(int, sys.stdin.readline().split())
re_spuared(2 ** n, 0, 0)