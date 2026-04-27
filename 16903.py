import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class TrieNode:
    def __init__(self, parent=None):
        self.children = [None, None]
        self.parent = parent


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def get_word(self, num):
        word = []
        for i in range(30):
            word.append(num & 1)
            num >>= 1
        word = word[::-1]
        return word

    def insert(self, num):
        word = self.get_word(num)
        cur = self.root
        for c in word:
            if not cur.children[c]:
                cur.children[c] = TrieNode(cur)
            cur = cur.children[c]

    def remove(self, num):
        word = self.get_word(num)
        cur = self.root
        path = []
        for c in word:
            if not cur.children[c]:
                assert False
            path.append((cur, c))
            cur = cur.children[c]
        for par, c in path[::-1]:
            if cur.children == [None, None]:
                par.children[c] = None
                cur = par
            else:
                break

    def query(self, x):
        x = self.get_word(x)
        cur = self.root
        ret = 0
        bit = 29
        for c in x:
            if cur.children[1 - c]:
                ret += 1 << bit
                cur = cur.children[1 - c]
            elif cur.children[c]:
                cur = cur.children[c]
            else:
                break
            bit -= 1
        return ret


trie = Trie()
trie.insert(0)
cnt = defaultdict(int)
cnt[0] = 1
for _ in range(int(input_())):
    q, x = minput()
    if q == 1:
        if not cnt[x]:
            trie.insert(x)
        cnt[x] += 1
    elif q == 2:
        if cnt[x] == 1:
            trie.remove(x)
        cnt[x] -= 1
    else:
        print(trie.query(x))
