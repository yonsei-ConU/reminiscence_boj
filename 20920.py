import sys
from functools import cmp_to_key
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def cmp(a, b):
    if words[a] > words[b]:
        return -1
    elif words[a] < words[b]:
        return 1
    elif len(a) > len(b):
        return -1
    elif len(a) < len(b):
        return 1
    elif a < b:
        return -1
    else:
        return 1


N, M = minput()
words = defaultdict(int)
for _ in range(N):
    word = input_().rstrip()
    if len(word) >= M:
        words[word] += 1

distinct = list(words.keys())
for word in sorted(distinct, key=cmp_to_key(cmp)):
    print(word)
