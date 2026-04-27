import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M, X, Y = minput()
M -= 1
khy, h = minput()
students = []
for i in range(N - 1):
    id_, score = minput()
    if id_ >= 2024000000:
        students.append(score + max(0, + Y - (X - score)) - h)

students.sort()
while students and students[-1] > Y:
    students.pop()
    M -= 1
students.reverse()
if M < 0:
    print('NO')
else:
    print('YES')
    if len(students) > M:
        print(students[M])
    else:
        print(0)
