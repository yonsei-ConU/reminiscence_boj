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


N = int(input_())
words = [input_() for _ in range(N)]
trie = Trie()
for word in words:
    trie.insert(word)
