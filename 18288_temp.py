from itertools import product

def generate_sequences(N):
    sequences = [''.join(seq) for seq in product('BC', repeat=N)]
    return sequences

N = 6
sequences = generate_sequences(N)
ans = 0
for seq in sequences:
    if 'BB' not in seq and 'C' in seq:
        ans += 1

print(ans)
