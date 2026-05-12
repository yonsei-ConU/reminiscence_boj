import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def convert(number, a, b):
    if a == b:
        return number

    power_a = 10 ** (9 - a)
    power_b = 10 ** (9 - b)

    digit_a = (number // power_a) % 10
    digit_b = (number // power_b) % 10

    number -= digit_a * power_a
    number -= digit_b * power_b

    number += digit_b * power_a
    number += digit_a * power_b

    return number


dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
dpos = [3, -3, 1, -1]
for _ in range(int(input_())):
    input_()
    A = ''
    idx = -1
    for i in range(3):
        s = input_().rstrip()
        for j in range(3):
            char = s[j]
            if char.isdigit():
                A += char
            else:
                A += '0'
                idx = i * 3 + j
    A = int(A)
    assert idx != -1
    q = deque([(A, idx)])
    dist = {A: 0}
    while q:
        cur, idx = q.popleft()
        y, x = divmod(idx, 3)
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if not (0 <= ny < 3 and 0 <= nx < 3):
                continue
            change1 = idx - 1
            change2 = idx + dpos[i] - 1
            if change1 > change2:
                change1, change2 = change2, change1
            nxt = convert(cur, idx + 1, idx + dpos[i] + 1)
            if nxt == 123456780:
                dist[nxt] = dist[cur] + 1
                q = []
                break
            if nxt not in dist:
                dist[nxt] = dist[cur] + 1
                q.append((nxt, idx + dpos[i]))
    print(dist.get(123456780, 'impossible'))
