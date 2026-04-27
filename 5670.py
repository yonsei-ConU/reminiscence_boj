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

    def dfs(self, cur, depth, auto=False):
        global ans
        if cur.s == '\n':
            if not auto:
                depth -= 1
            ans += depth
        elif len(cur.children) == 1 and cur != self.root:
            for nxt in cur.children:
                self.dfs(cur.children[nxt], depth, True)
        else:
            for nxt in cur.children:
                self.dfs(cur.children[nxt], depth + 1)


while True:
    try:
        N = int(input_())
    except:
        break
    ans = 0
    trie = Trie()
    for __ in range(N):
        trie.insert(input_())
    trie.dfs(trie.root, 0)
    print(f"{ans / N:.2f}")
