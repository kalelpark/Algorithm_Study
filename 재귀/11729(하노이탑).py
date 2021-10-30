import sys

def hanoi(n, x, y, z):
    if n == 1:
        t = [x, y]
        out_list.append(t)
        return
        # 마지막 끝나는 부분이다.
        # 가장 작은 값이 가장 꼭대기에 올라가야 끝난다.
    hanoi(n-1, x, z, y)
    t = [x, y]
    out_list.append(t)
    hanoi(n-1, z, y, x)
    
out_list = list()
n = int(sys.stdin.readline())
hanoi(n, 1, 3, 2)
print(len(out_list))
for q, z in out_list:
    print(q, z)
