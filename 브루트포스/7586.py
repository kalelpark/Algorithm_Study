import sys

test_case = int(sys.stdin.readline())

people = list()

for _ in range(test_case):
    kg , length  = map(int, sys.stdin.readline().split())

    people.append([kg, length])
    # Kg 저장


rank = []

for kg, length in people:
    count = 1
    for kg_1 , length_1 in people:
        if kg_1 > kg and length_1 >length:
            count += 1
    rank.append(count)

print(*rank)