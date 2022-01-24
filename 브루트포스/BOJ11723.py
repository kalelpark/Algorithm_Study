# 비어있는 공집합 S가 주어진 경우, 아래의 연산을 수행하는 프로그램 작성
import sys

test_case = int(sys.stdin.readline())

s = 0b0
all_s = 0b11111111111111111111
not_s = 0b00000000000000000000

for _ in range(test_case):
    cmd = sys.stdin.readline().rstrip().split(' ')
    if cmd[0] == 'add':
        s = s | (1 << int(cmd[-1]))
    elif cmd[0] == 'remove':
        s = s & ~(1 << int(cmd[-1]))
    elif cmd[0] == 'check':
        if s & (1 << int(cmd[-1])):
            print(1)
        else:
            print(0)
    elif cmd[0] == 'toggle':
        s = s ^ (1 << int(cmd[-1]))
    elif cmd[0] == 'all':
        s = all_s
    elif cmd[0] == 'empty':
        s = not_s