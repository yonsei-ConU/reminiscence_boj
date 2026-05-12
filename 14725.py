import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class TrieNode:
    def __init__(self, s=None):
        self.children = {}
        self.s = s

    def __str__(self):
        return str(self.s)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode(c)
            cur = cur.children[c]

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True


def dfs(cur, depth):
    if depth + 1:
        print('--' * depth + str(cur))
    for c in sorted(cur.children):
        dfs(cur.children[c], depth + 1)


N = int(input_())
trie = Trie()
for _ in range(N):
    path = input_().split()[1:]
    trie.insert(path)

dfs(trie.root, -1)
