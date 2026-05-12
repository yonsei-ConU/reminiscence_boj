import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='ascii')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


def match(i, j):
    if S[i] == T[j]:
        return True
    elif S[i] == 'i' and T[j] in 'jl':
        return True
    elif S[i] == 'v' and T[j] == 'w':
        return True
    return False


output = []
n, m = minput()
S = sinput().rstrip()
T = sinput().rstrip()

# dp[i][j] = (1-indexed S[i], T[j]까지 확인했을 때 점수의 최솟값)
dp = [[2000000] * (m + 1) for _ in range(n + 1)]
for i in range(m + 1):
    dp[0][i] = i
for i in range(n + 1):
    dp[i][0] = i

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if match(i - 1, j - 1):
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

print(dp[-1][-1])

os.write(1, '\n'.join(output).encode())
os._exit(0)
