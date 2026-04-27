import sys
from collections import defaultdict
input = sys.stdin.readline

trees = defaultdict(int)
total = 0

for line in sys.stdin:
    tree = line.rstrip()
    total += 1
    trees[tree] += 1

treenames = sorted(trees.keys())
for tree in treenames:
    print("%s %.4f" % (tree, trees[tree] / total * 100))
