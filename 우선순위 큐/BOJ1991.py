import sys

class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

def preorder(x):
    if x == -1:
        return
    print(chr(x+ord('A')), end='')
    preorder(a[x].left)
    preorder(a[x].right)

def inorder(x):
    if x == -1:
        return
    inorder(a[x].left)
    print(chr(x+ord('A')), end = '')
    inorder(a[x].right)

def postorder(x):
    if x == -1:
        return
    
    postorder(a[x].left)
    postorder(a[x].right)
    print(chr(x + ord('A')), end ='')

a = dict()

n = int(sys.stdin.readline())
for _ in range(n):
    x, y, z = map(str, sys.stdin.readline().rstrip().split())

    x = ord(x) - ord('A')
    
    left = -1
    right = -1

    if y != '.':
        left = ord(y) - ord('A')
    
    if z != '.':
        right = ord(z) - ord('A')
    
    a[x] = Node(left, right)   # 트리 설정

preorder(0)
print()
inorder(0)
print()
postorder(0)