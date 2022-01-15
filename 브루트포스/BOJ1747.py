import sys

n = int(sys.stdin.readline())

prime = [False, False] + [True for _ in range(n+1)]

array = []
for i in range(2, n+1):
    if prime[i] == True:
        for j in range(2*i, n+1, i):
            prime[j] = False
            
answer = list()
if n < 8:
    print(-1)
    sys.exit()

if n >= 8 and n%2 == 0:
    answer.append(2)
    answer.append(2)
    n -= 4
elif n >=8 and n%2 == 1:
    answer.append(2)
    answer.append(3)
    n -= 5

for i in range(2, n+1):
    if prime[i] and prime[n - i]:
        answer.append(i)
        answer.append(n - i)
        break

answer = sorted(answer)

for i in answer:
    print(i, end = ' ')

