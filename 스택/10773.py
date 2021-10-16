# 잘못된 수를 부를 때마다 0을 외쳐 수를 지우게 한다.

# 모두 받아 적은 수의 합

# 첫번째 K, 이후 K개의 줄에 정수가 하나씩 주어진다.
# 간단하게 생각하면 된다.
# 0을 부르면 pop 나머지는 append 해주면 된다. 이후로 마자막에 Sum을 구하면 된다.

import sys

test_case = int(sys.stdin.readline())

cash_counter = []

for _ in range(test_case):
    cash = int(sys.stdin.readline())

    if cash == 0:
        cash_counter.pop()
    else:
        cash_counter.append(cash)

print(sum(cash_counter))