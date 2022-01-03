import heapq

heap = []

heapq.heappush(heap, 100)
heapq.heappush(heap, 90)
heapq.heappush(heap, 10)

print(heapq.heappop(heap))
print(heap)

array = [5, 4, 3, 2, 1]

heapq.heapify(array)
print(array)