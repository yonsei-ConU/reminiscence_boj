import sys
from collections import deque
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class AhoCorasickTrieNode:
    def __init__(self, s=None):
        self.children = {}
        self.s = s
        self.fail = None
        self.output = []

    def __str__(self):
        return str(self.s)


class AhoCorasickTrie:
    def __init__(self):
        self.root = AhoCorasickTrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = AhoCorasickTrieNode(c)
            cur = cur.children[c]
        cur.output.append(word)

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

    def search(self, text, mode):
        cur = self.root
        ret = set()
        for i, c in enumerate(text):
            while c not in cur.children and cur != self.root:
                cur = cur.fail
            if c in cur.children:
                cur = cur.children[c]
            else:
                cur = self.root
            if cur.output:
                for pattern in cur.output:
                    if (not i - len(pattern)  1 and not mode) or (i == len(text) - 1 and mode):
                        ret.add(len(pattern))

        return ret


C, N = minput()

colors = AhoCorasickTrie()
for _ in range(C):
    colors.insert(input_().rstrip())
colors.build_aho_corasick()

names = AhoCorasickTrie()
for _ in range(N):
    names.insert(input_().rstrip())
names.build_aho_corasick()

for _ in range(int(input_())):
    teamname = input_().rstrip()
    color_match = sorted(colors.search(teamname, 0))
    name_match = sorted(names.search(teamname, 1))
    c = 0
    n = len(name_match) - 1
    chk = False
    while c < len(color_match) and n >= 0:
        t = color_match[c] + name_match[n]
        if t > len(teamname):
            n -= 1
        elif t == len(teamname):
            chk = True
            break
        else:
            t += 1
    print('YNeos'[1 - chk::2])
