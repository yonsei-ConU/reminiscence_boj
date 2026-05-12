import sys
from random import *
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


# 클래스 node는 이진 트리의 노드를 구성합니다.
# node는 클래스 변수로 L,R,Lc,Rc,x를 가집니다.
# L,R은 왼쪽과 오른쪽 자식 노드를 가리키는 포인터 또는 인덱스입니다.
# Lc와 Rc는 왼쪽과 오른쪽에 추가할 수 있는 리프 노드의 수를 나타냅니다.
# 예를 들어 새로운 노드에 대해 Lc와 Rc는 기본적으로 1입니다.
# x는 노드가 저장하는 정수 값입니다.


class Node:
    def __init__(self, x):
        self.x = x
        self.L = None
        self.R = None
        self.Lc = 1
        self.Rc = 1

def makenode(a):
  return Node(a)

def insert(rt,a):
  while True:
    M = rt.Lc+rt.Rc
    v = randint(0, M - 1)
    if v < rt.Lc: # 라인 A
      rt.Lc += 1
      if rt.Lc == 2:
        rt.L = makenode(a)
        return
      rt = rt.L
    else:
      rt.Rc += 1
      if rt.Rc == 2:
        rt.R = makenode(a)
        return
      rt = rt.R

def inorder(rt):
  global time
  time += 1
  if rt.Lc > 1:
    inorder(rt.L)
  ans[rt.x][time] += 1
  if rt.Rc > 1:
    inorder(rt.R)

# ...
# 데이터를 생성하는 방법
ans = [[0] * 1001 for _ in range(1001)]
for i in range(300000):
    if not i % 1000:
        print(i)
    root= makenode(1)
    for i in range(2,1000+1):
      insert(root,i)
    time = 0
    inorder(root)

sys.stdout = open('32295_correct_data.out', 'w')
for i in range(1001):
    for j in range(1001):
        sys.stdout.write(str(ans[i][j]))
        if j != 1000:
            sys.stdout.write(' ')
    sys.stdout.write('\n')
