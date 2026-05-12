import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
candidates = {}
for i in range(n):
    a = input_().rstrip()
    b = input_().rstrip()
    candidates[a] = b
votes = {i: 0 for i in candidates.keys()}
for _ in range(int(input_())):
    voted = input_().rstrip()
    if voted in candidates:
        votes[voted] += 1

v = list(votes.values())
M = max(v)
if v.count(M) > 1:
    print('tie')
else:
    for key in votes:
        if votes[key] == M:
            print(candidates[key])
