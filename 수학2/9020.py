import sys

prime_list = [False, False] + [True]*10000          # 소수를 저장할 리스트 만들기

for i in range(2, 101):     
    if prime_list[i] == True:           # 이미 False 로 되어있는 수는 다시 구하지 않아도 되기 때문이다.           
        for j in range(i+i, 10001, i):
            prime_list[j] = False              # 자기자신을 제외한 수는 모두 False 만들기

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    prime = int(sys.stdin.readline())
    
    num1 = (prime//2)
    num2 = num1
    while 1:
        if prime_list[num1] and prime_list[num2] :
            print(num1, num2)
            break
        else:
            num1 -= 1
            num2 += 1
import sys

prime_test = [False, False] + [True]*10001

for i in range(2,101):
    if prime_test[i] == True:
        for j in range(i+i, 10001, i):
            prime_test[j] = False

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    prime = int(sys.stdin.readline())
    
    num1 = (prime//2)
    num2 = num1
    
    while 1:
        if prime_test[num1] and prime_test[num2]:
            print(num1, num2)
            break
        else:
            num1 -= 1
            num2 += 1
            

