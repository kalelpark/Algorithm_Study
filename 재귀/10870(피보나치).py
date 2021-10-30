import sys

def fibo(n):
    if n == 1 or n == 2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibo(n-1)+fibo(n-2)
        # 자신의 함수를 다시 호출함으로써 작은문제로 변하여 해결하는 원리이다.

n = int(sys.stdin.readline())

print(fibo(n))
        
