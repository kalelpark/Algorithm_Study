import sys
n = int(sys.stdin.readline())
# 배열 생성
array = [list(sys.stdin.readline().strip()) for _ in range(n)]
# 값저장
count_array = [[0]*n for _ in range(n)]


# 움직이는 방향
dx = [-1, 1, 0, 0]
dy = [0,  0, 1, -1]
mam = 0

for i in range(n):
    for j in range(n):
        count = 0
        for t in range(4):
            tmp_i = i + dy[t]
            tmp_j = j + dx[t]

            if tmp_i < 0 or tmp_j < 0 or tmp_i >= n or tmp_j >= n:
                continue
            # 값 변경
            else:
                tmp = array[i][j]
                jmp = array[tmp_i][tmp_j]
                array[i][j] = jmp
                array[tmp_i][tmp_j] = tmp
                
                # 열
                for x in range(n):
                    if x == 0:
                        candy_count = 1
                        qx = array[i][x]
                    else:
                        if qx == array[i][x]:
                            candy_count += 1
                        else:
                            qx = array[i][x]
                            candy_count = 1

                    if count < candy_count:
                        count = candy_count

                                
                # 행
                for x in range(n):
                    if x == 0:
                        candy_count = 1
                        qx = array[x][j]
                    else:
                        if qx == array[x][j]:
                            candy_count += 1
                        else:
                            qx = array[x][j]
                            candy_count = 1

                    if count < candy_count:
                        count = candy_count
                
                array[i][j] = tmp
                array[tmp_i][tmp_j] = jmp            
        
        if mam < count:
            mam = count

print(mam)

                    

                        
                    
