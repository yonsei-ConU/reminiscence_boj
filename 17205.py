import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
password = input_().strip()
twentysix = [0, 26]
for i in range(2, 11):
    twentysix.append(twentysix[-1] + 26 ** i)

ans = 0
for i in range(len(password)):
    s = ord(password[i]) - 97
    ans += s * twentysix[N - 1 - i] + s + 1

print(ans)
