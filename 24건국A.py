import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


rnrneksby = set(range(1, 10))
for i in range(2, 10):
    for j in range(2, 10):
        rnrneksby.add(i * j)
N = int(input_())
print(+(N in rnrneksby))
