import sys
from algorithms import AhoCorasickTrie
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
S = [input_().rstrip() for _ in range(N)]
trie = AhoCorasickTrie()
for i in range(N):
    trie.insert(S[i])

trie.build_aho_corasick()
for _ in range(int(input_())):
    matches = trie.search(input_().rstrip())
    if matches:
        print("YES")
    else:
        print("NO")
