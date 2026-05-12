import sys
from algorithms import AhoCorasickTrieNode
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class AhoCorasickTrie:
    def __init__(self):
        self.root = AhoCorasickTrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = AhoCorasickTrieNode(c)
            cur = cur.children[c]
        cur.output.append(len(word))

    def build_aho_corasick(self):
        q = deque()
        for child in self.root.children.values():
            q.append(child)
            child.fail = self.root
        while q:
            cur = q.popleft()
            for c, nxt in cur.children.items():
                fail_node = cur.fail
                while fail_node and c not in fail_node.children:
                    fail_node = fail_node.fail
                nxt.fail = fail_node.children[c] if fail_node else self.root
                if nxt.fail:
                    nxt.output += nxt.fail.output
                q.append(nxt)

    def search(self, text):
        cur = self.root
        matches = []
        for i, c in enumerate(text):
            while c not in cur.children and cur != self.root:
                cur = cur.fail
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur = self.root
            if cur.output:
                for pattern in cur.output:
                    matches.append((i - pattern + 1, pattern))
        return matches


MOD = 1337377
# longword = input_().rstrip()
longword = 'a' * 300000
trie = AhoCorasickTrie()
for _ in range(int(input_())):
    # trie.insert(input_().rstrip())
    trie.insert('a' * (_ + 1))

trie.build_aho_corasick()
matches = trie.search(longword)
print(len(matches))
dp = [1] + [0] * len(longword)
for idx, t in matches:
    dp[idx + t] += dp[idx]
    if dp[idx + t] >= MOD:
        dp[idx + t] -= MOD

print(dp[-1])
