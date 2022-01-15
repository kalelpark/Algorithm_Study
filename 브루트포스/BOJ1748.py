import sys
# 숫자간의 규칙을 찾을 때 활용합니다.
n = int(sys.stdin.readline())

pom = 0
tmp = 0
t = len(str(n))
for i in range(t):
    if i == 0:
        pom = n
    else:
        pom -= 9*(10**(i-1))
    
    tmp += pom

print(tmp)