# 문자열이 VPS인지 판단하기

# 예를 들어 “(())()”와 “((()))” 는 VPS 이지만 
# “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 

# 괄호가 나오면 스택, 큐 항상 먼저 생각해줘야한다.

# 반례 유의하기
# 990009 문제가 있지만, 숫자로 할 경우에는 그냥 넘어가게 된다. 이러한 경우도 해결하게 끔 
# 구조를 파악해야 한다.

# 음수가 되면 바로 박살내기 또는 0일 때, 참이 되게 끔 하면 된다. ( -> 1 ) -> -1 
# 만약 -1 인 경우 바로 pop 하기

import sys
test_case = int(sys.stdin.readline())

for _ in range(test_case):
    parasite = sys.stdin.readline().rstrip()
    count = 0
    taf = 0
    for i in parasite:
        if i == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                print('NO')
                taf = 1  
                break
    if count == 0:
        print('YES')
    elif count > 0:
        print('NO')
