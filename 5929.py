import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


binary = input_().rstrip()
l = len(binary)
s = set()
binary = int(binary, 2)
for i in range(l):
    s.add(binary ^ (1 << i))

ternary = input_().rstrip()
l = len(ternary)
t = int(ternary, 3)
ternary = ternary[::-1]
for i in range(l):
    if ternary[i] != "0" and t - 3 ** i in s:
        exit(print(t - 3 ** i))
    elif ternary[i] != "2" and t + 3 ** i in s:
        exit(print(t + 3 ** i))
    elif ternary[i] == "0" and t + 2 * 3 ** i in s:
        exit(print(t + 2 * 3 ** i))
    elif ternary[i] == "2" and t - 2 * 3 ** i in s:
        exit(print(t - 2 * 3 ** i))
