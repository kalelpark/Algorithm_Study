import sys
num1, num2 = map(int, sys.stdin.readline().split())

array = list(list(sys.stdin.readline().strip()) for _ in range(num1))

why = list()

for i in range(num1 - 7):
    for j in range(num2 - 7):
        w, b = 0, 0
        for y in range(i, i+8):
            for x in range(j, j+8):
                if (y+x)%2  == 0:
                    if array[y][x] != 'W':
                        w += 1
                    if array[y][x] != 'B':
                        b += 1
                else:
                    if array[y][x] != 'B':
                        w += 1
                    if array[y][x] != 'W':
                        b += 1
        why.append(w)
        why.append(b)
print(min(why))