# 12시 방향부터 시계방향 순서대로 주어진다.
import sys
from collections import deque
#  12시 방향부터 값 넣어주기
tooth_1 = deque(sys.stdin.readline().strip())
tooth_2 = deque(sys.stdin.readline().strip())
tooth_3 = deque(sys.stdin.readline().strip())
tooth_4 = deque(sys.stdin.readline().strip())

# 2번 톱니와 3번 톱니는 2, 6번쨰의 톱니를 파악해야 한다.
# 반대로 1번과 4번의 경우에는 각각 2, 6 번째의 톱니를 파악해야 한다. 

test_case = int(sys.stdin.readline())

# 회전할것인지 안할것인지 판단하기 위함이다.

# 문제의 형태가 처음 값을 애초에 비교를 시작한 다음에 그중에 틀린 것을 돌리는 것이다. 
tmp = 0

for _ in range(test_case):
    # 톱니 선택 및 방향선택
    choose, direction = map(int, sys.stdin.readline().split())

    # 방향 파악하기
    if direction == 1:
        # 1번 Case Solve
        if choose == 1:
            # 1번과 2번 톱니가 같은 경우
            if tooth_1[2] == tooth_2[6]:
                tooth_1.appendleft(tooth_1.pop())
            else:
                # 2번과 3번이 이 같은 경우
                if tooth_2[2] == tooth_3[6]:
                    tooth_1.appendleft(tooth_1.pop())
                    tooth_2.append(tooth_2.popleft())
                # 
                elif tooth_3[2] == tooth_4[6]:
                    # 2번, 3번이 서로 다르고, 4번은 회전시키지 않아도 되는 경우
                    tooth_1.appendleft(tooth_1.pop())
                    tooth_2.append(tooth_2.popleft())
                    tooth_3.appendleft(tooth_3.pop())
                else:
                    # 2번, 3번 4번 모두 다른 경우
                    tooth_1.appendleft(tooth_1.pop())
                    tooth_2.append(tooth_2.popleft())
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_4.append(tooth_4.popleft())
        # 2번 Case Solve
        elif choose == 2:
            # 모두 같은 경우
            if tooth_2[2] == tooth_3[6] and tooth_2[6] == tooth_1[2]:
                tooth_2.appendleft(tooth_2.pop())
            # 2번 회전시 1번과 같으며, 3번과 다른 경우
            elif tooth_2[2] != tooth_3[6] and tooth_2[6] == tooth_1[2]:
                # 3번과 4번이 다른 경우
                if tooth_3[2] != tooth_4[6]:
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_3.append(tooth_3.popleft())
                    tooth_4.appendleft(tooth_4.pop())
                # 3번과 4번이 같은 경우    
                else:
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_3.append(tooth_3.popleft())
                # 2번과 3번이 같은 경우, 1번과 2번이 다른경우
            elif tooth_2[2] == tooth_3[6] and tooth_2[6] != tooth_1[2]:
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_1.append(tooth_1.popleft())
            # 1,3번과 다른 경우
            else:
                # 3번과 4번이 다른 경우
                if tooth_3[2] != tooth_4[6]:
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_1.append(tooth_1.popleft())
                    tooth_3.append(tooth_3.popleft())
                    tooth_4.appendleft(tooth_4.pop())
                # 3번과 4번이 같은 경우
                else:
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_1.append(tooth_1.popleft())
                    tooth_3.append(tooth_3.popleft())
        # 3번 Case Solve
        elif choose == 3:
            # 모두 같은 경우
            if tooth_2[2] == tooth_3[6] and tooth_3[2] == tooth_4[6]:
                tooth_3.appendleft(tooth_3.pop())
            # 3번, 4번이 같으며, 2번과 다른 경우
            elif tooth_2[2] != tooth_3[6] and tooth_4[6] == tooth_3[2]:
                # 2번 과 1번이 다른 경우
                if tooth_1[2] != tooth_2[6]:
                    tooth_2.append(tooth_2.popleft())
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_1.appendleft(tooth_1.pop())
                # 2번과 1번이 같은 경우  
                else:
                    tooth_2.append(tooth_2.popleft())
                    tooth_3.appendleft(tooth_3.pop())
            # 3번과 4번이 다르며, 2번과 같은 경우
            elif tooth_3[2] != tooth_4[6] and tooth_3[6] == tooth_2[2]:
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_4.append(tooth_4.popleft())
            # 3번이 2번 4번과 다른 경우
            else:
                # 3번과 4번이 다른 경우
                if tooth_1[2] != tooth_2[6]:
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_2.append(tooth_2.popleft())
                    tooth_1.appendleft(tooth_1.pop())
                    tooth_4.append(tooth_4.popleft())
                # 3번과 4번이 같은 경우
                else:
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_2.append(tooth_2.popleft())
                    tooth_4.append(tooth_4.popleft())
        else:
            # 4인 경우
            if tooth_3[2] == tooth_4[6]:
                tooth_4.appendleft(tooth_4.pop())
            else:
                # 4,3 은 다르고, 3,2는 같은 경우
                if tooth_2[2] == tooth_3[6]:
                    # 1번, 2번 톱니만 다른 경우
                    tooth_4.appendleft(tooth_4.pop())
                    tooth_3.append(tooth_3.popleft())
                # 4,3 이 다르며, 1
                elif tooth_1[2] == tooth_2[6]:
                    # 2번, 3번이 서로 다르고, 4번은 회전시키지 않아도 되는 경우
                    tooth_4.appendleft(tooth_4.pop())
                    tooth_3.append(tooth_3.popleft())
                    tooth_2.appendleft(tooth_2.pop())
                else:
                    # 2번, 3번 4번 모두 다른 경우
                    tooth_4.appendleft(tooth_4.pop())
                    tooth_3.append(tooth_3.popleft())
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_1.append(tooth_1.popleft())
    else:
        if choose == 1:
            # tooth1.appendleft(tooth1.pop())
            if tooth_1[2] == tooth_2[6]:
                tooth_1.append(tooth_1.popleft())
            else:
                # 첫번째 서로 다름
                if tooth_2[2] == tooth_3[6]:
                    # 1번, 2번 톱니만 다른 경우
                    tooth_1.append(tooth_1.popleft())
                    tooth_2.appendleft(tooth_2.pop())
                    
                elif tooth_3[2] == tooth_4[6]:
                    # 2번, 3번이 서로 다르고, 4번은 회전시키지 않아도 되는 경우
                    tooth_1.append(tooth_1.popleft())
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_3.append(tooth_3.popleft())
                else:
                    # 2번, 3번 4번 모두 다른 경우
                    tooth_1.append(tooth_1.popleft())
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_3.append(tooth_3.popleft())
                    tooth_4.appendleft(tooth_4.pop())
        elif choose == 2:
            # 모두 같은 경우
            if tooth_2[2] == tooth_3[6] and tooth_2[6] == tooth_1[2]:
                tooth_2.append(tooth_2.popleft())
            # 2번 회전시 1번과 같으며, 3번과 다른 경우
            elif tooth_2[2] != tooth_3[6] and tooth_2[6] == tooth_1[2]:
                # 3번과 4번이 다른 경우
                if tooth_3[2] != tooth_4[6]:
                    tooth_2.append(tooth_2.popleft())
                    # tooth_1.append(tooth_1.popleft())
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_4.append(tooth_4.popleft())
                # 3번과 4번이 같은 경우    
                else:
                    tooth_2.append(tooth_2.popleft())
                    tooth_3.appendleft(tooth_3.pop())
                # 2번과 3번이 같은 경우, 1번과 2번이 다른경우
            elif tooth_2[2] == tooth_3[6] and tooth_2[6] != tooth_1[2]:
                    tooth_2.append(tooth_2.popleft())
                    tooth_1.appendleft(tooth_1.pop())
            # 1,3번과 다른 경우
            else:
                # 3번과 4번이 다른 경우
                if tooth_3[2] != tooth_4[6]:
                    tooth_2.append(tooth_2.popleft())
                    tooth_1.appendleft(tooth_1.pop())
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_4.append(tooth_4.popleft())
                # 3번과 4번이 같은 경우
                else:
                    tooth_2.append(tooth_2.popleft())
                    tooth_1.appendleft(tooth_1.pop())
                    tooth_3.appendleft(tooth_3.pop())
        elif choose == 3:
            # 모두 같은 경우
            if tooth_2[2] == tooth_3[6] and tooth_3[2] == tooth_4[6]:
                tooth_3.append(tooth_3.popleft())
            # 3번, 4번이 같으며, 2번과 다른 경우
            elif tooth_2[2] != tooth_3[6] and tooth_4[6] == tooth_3[2]:
                # 2번 과 1번이 다른 경우
                if tooth_1[2] != tooth_2[6]:
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_3.append(tooth_3.popleft())
                    tooth_1.append(tooth_1.popleft())
                # 2번과 1번이 같은 경우  
                else:
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_3.append(tooth_3.popleft())
            # 3번과 4번이 다르며, 2번과 같은 경우
            elif tooth_3[2] != tooth_4[6] and tooth_3[6] == tooth_2[2]:
                    tooth_3.append(tooth_3.popleft())
                    tooth_4.appendleft(tooth_4.pop())
            # 3번이 2번 4번과 다른 경우
            else:
                # 3번과 4번이 다른 경우
                if tooth_1[2] != tooth_2[6]:
                    tooth_3.append(tooth_3.popleft())
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_1.append(tooth_1.popleft())
                    tooth_4.appendleft(tooth_4.pop())
                # 3번과 4번이 같은 경우
                else:
                    tooth_3.append(tooth_3.popleft())
                    tooth_2.appendleft(tooth_2.pop())
                    tooth_4.appendleft(tooth_4.pop())
        else:
            # 4인 경우
            if tooth_3[2] == tooth_4[6]:
                tooth_4.append(tooth_4.popleft())
            else:
                # 4,3 은 다르고, 3,2는 같은 경우
                if tooth_2[2] == tooth_3[6]:
                    # 1번, 2번 톱니만 다른 경우
                    tooth_4.append(tooth_4.popleft())
                    tooth_3.appendleft(tooth_3.pop())
                # 4,3 이 다르며, 1
                elif tooth_1[2] == tooth_2[6]:
                    # 2번, 3번이 서로 다르고, 4번은 회전시키지 않아도 되는 경우
                    tooth_4.append(tooth_4.popleft())
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_2.append(tooth_2.popleft())
                else:
                    # 2번, 3번 4번 모두 다른 경우
                    tooth_4.append(tooth_4.popleft())
                    tooth_3.appendleft(tooth_3.pop())
                    tooth_2.append(tooth_2.popleft())
                    tooth_1.appendleft(tooth_1.pop())

    
point_1 = 0
point_2 = 0
point_3 = 0
point_4 = 0

if tooth_1[0] == '1':
    point_1 = 1

if tooth_2[0] == '1':
    point_2 = 2

if tooth_3[0] == '1':
    point_3 = 4

if tooth_4[0] == '1':
    point_4 = 8
print(point_4 + point_3 + point_2 + point_1)