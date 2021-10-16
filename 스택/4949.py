import sys


while True:
    st = sys.stdin.readline().rstrip()

    if st[0] == '.':
        break
    
    braket_list = []
    t = 0

    for i in st:
        if i == '(' or i == '[':
            braket_list.append(i)
        

        elif i == ')':
            if not braket_list:
                t = 1
                break
            if braket_list[-1] == '(':
                braket_list.pop()
            else:
                t = 1
                break
        
        elif i == ']':
            if not braket_list:
                t = 1
                break
            if braket_list[-1] == '[':
                braket_list.pop()
            else:
                t = 1
                break
                
    if (t == 0) and (not braket_list):
        print('yes')
    else:
        print('no') 
    
    braket_list.clear()
