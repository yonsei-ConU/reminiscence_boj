import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n, m = minput()
ans = []
for i in range(2, n + 1, 2):
    ans.append(f"{i} 1 {i} {m}")
for j in range(2, m + 1, 2):
    ans.append(f"1 {j} {n} {j}")

print(len(ans))
print('\n'.join(ans))
