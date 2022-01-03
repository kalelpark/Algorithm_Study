import sys
import heapq as hq

array = []

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    num = int(sys.stdin.readline())

    if num == 0:
        if not array:
            print(0)
        else:
            print(hq.heappop(array))
    else:
        hq.heappush(array, num)