import sys

n = int(sys.stdin.readline())
# 소수 개수 구하기
prime = [True, True] + [True for _ in range(n+1)]

# 소수 생성하기
for i in range(2, n+1):
    if prime[i] == True:
        for j in range(i*2, n+1, i):
            prime[j] = False

# 소수 덧셈하기
count = 0

for i in range(2, n+1):
    sum_prime = 0
    # 모든 합 연산하기
    if prime[i] == True:
        for j in range(i, n+1):
            if prime[j] == True:
                sum_prime += j

                if sum_prime == n:
                    count += 1 
                    break
                elif sum_prime > n:
                    break
        
print(count)
