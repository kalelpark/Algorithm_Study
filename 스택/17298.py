import sys

count = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))

answer_array = [-1]*count
index_stack = []

for i in range(count):
    while (len(index_stack) != 0) and (array[index_stack[-1]] < array[i]):
        answer_array[index_stack.pop()] = array[i]
    index_stack.append(i)

print(*answer_array)


