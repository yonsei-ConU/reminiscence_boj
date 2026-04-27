import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for i in range(1, int(input_()) + 1):
    S = input_().rstrip()
    stack = []
    ans = 0
    for s in S:
        if stack and stack[-1] == s:
            stack.pop()
            ans += 10
        else:
            stack.append(s)
    print(f"Case #{i}: {ans + len(stack) * 5 // 2}")
