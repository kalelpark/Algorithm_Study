import sys
import heapq as hq

test_case = int(sys.stdin.readline())

array = list()
for _ in range(test_case):
    num = int(sys.stdin.readline())

    if num == 0:
        # 0 입력시 배열에 값이 없는 경우
        if not array: 
            print(0)
        else:
            # 음수로 값을 넣었으므로, 다시 양수로 변경하기
            print(-1*(hq.heappop(array)))
    else:
        hq.heappush(array, -1*num)