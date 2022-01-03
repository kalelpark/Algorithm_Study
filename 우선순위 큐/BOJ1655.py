import sys
import heapq as hq

test_case = int(sys.stdin.readline())

left_heap = []  # 최대 힙
right_heap = []  # 최소 힙

for _ in range(test_case):
    n = int(sys.stdin.readline())

    if len(left_heap) == len(right_heap):
        hq.heappush(left_heap, -n)
    else:
        hq.heappush(right_heap, n)
    
    if right_heap and left_heap[0]*-1 > right_heap[0]:
        min = hq.heappop(right_heap)
        max = hq.heappop(left_heap)
        
        hq.heappush(left_heap , -min)
        hq.heappush(right_heap, -max)

    print(left_heap[0]*-1)


