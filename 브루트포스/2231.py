import sys

num1 = int(sys.stdin.readline())

if (num1 - 57) <= 0:
    case = 0
else:
    case = num1 - 57

sums = 0

while 1:
    sums += case
    a = list(str(case))

    for i in a:
        sums += int(i)
    
    if sums == num1:
        print(case)
        break

    if case == num1:
        print(0)
        break
    
    sums = 0
    case += 1