# 치킨집의 개수는 m보다 크거나 같으며, 13보다 작을 것이다. 
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

# 반복문을 돌렸을 때, 1인 경우 2랑 가장 가까운 값들의 합을 구하면 되는 것이다.
# 가장 먼것을 제거해야 한다.
# 2개를 무작위로 지정해서 제거하기?
# 2의 위치에 대한 정보를 전부 받아놓은 다음에 -> 그 중에서 한 군대를 선택해서,
# 그중 index를 선택해서 그것을 기준으로 정하는 방식? 이렇게 하면 장점은 1과 2만 찾고 나머지는 안찾아도 되니까 오히려 효율적일 수 있다.

# 배열을 먼저 입력하기
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 2와 1에 대한 index를 찾기
house_list = list()
chick_list = list()

# 무작위로 3가지 선택하기.  --> 조합으로 permutation 실행하기? 1초에 1억번 계산이므로, 
for i in range(n):
    for j in range(n):
        # chicken 정보 저장하기
        if array[i][j] == 2:
            chick_list.append([i,j])
        # house 정보 저장하기
        elif array[i][j] == 1:
            house_list.append([i, j])

# 집에 대한 정보를 조합으로 리스트 선택하기
real_chick = combinations(chick_list , m)
# tuple 형태로 데이터가 저장된다.
# print(list(real_chick))

# 도시의 치킨집의 길이를 구하기 위한 변수
cap = 1000000
for test_ch in real_chick:
    # 최솟값을 구하기 위한 도시값 초기화
    city_of_chicken =  0
    for test_hs in house_list:
        # 값 초기화
        tap = 1000
        for a in test_ch:
            # 값 저장히기
            tmp = abs(test_hs[0] - a[0]) + abs(test_hs[1] - a[1])
            if tap > tmp:
                tap = abs(test_hs[0] - a[0]) + abs(test_hs[1] - a[1])
        # 도시의 거리 길이 저장
        city_of_chicken += tap
    if cap > city_of_chicken:
        cap = city_of_chicken

print(cap)
    
        