import sys

def star(n1, n2, t):
    if t == 3:
        array[n1 + 1][n2 + 1] = ' '
    else:
        tmp = t//3
        for i in range(n1+tmp, n1+(tmp*2)):
            for j in range(n2+tmp, n2+(tmp*2)):
                array[i][j] = ' '
    
        for a in range(0, t, tmp):          # 가운데를 찾기 위함
            for b in range(0, t, tmp):
                star(n1 + a, n2 + b, tmp)
        

n = int(sys.stdin.readline())

array = [['*']*n for _ in range(n)]

star(0 , 0, n)

for i in range(n):
    for j in range(n):
        print(array[i][j], end='')
    print()