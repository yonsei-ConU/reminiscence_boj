import io, os
reader = io.BufferedReader(io.FileIO(0), buffer_size=131072)
text_reader = io.TextIOWrapper(reader, encoding='utf-8')
input_ = reader.readline
sinput = text_reader.readline
def minput(): return map(int, input_().split())


output = []
N = int(input_())
perm = list(minput())
output.append(str(2 * N - 1))
matrix = [[0] * (2 * N - 1) for _ in range(2 * N - 1)]
for x in range(N):
    y = N - 1 - x
    for j in range(N):
        matrix[y + j][x] = perm[j]
        matrix[y][x + j] = perm[j]

for x in range(N, 2 * N - 1):
    y = 3 * N - 2 - x
    for j in range(N):
        matrix[y - j][x] = perm[N - 1 - j]
        matrix[y][x - j] = perm[N - 1 - j]

for i in range(2 * N - 1):
    for j in range(2 * N - 1):
        if not matrix[i][j]:
            matrix[i][j] = perm[0]
for i in range(2 * N - 1):
    output.append(' '.join(map(str, matrix[i])))
os.write(1, '\n'.join(output).encode())
os._exit(0)
