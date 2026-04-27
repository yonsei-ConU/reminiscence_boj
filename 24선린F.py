import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
binary = [f"{bin(i)[2:]:0>{N}}" for i in range(2 ** N)]
binary.sort(key=lambda x: (x.count('1'), int(x[::-1])))
print(binary.index(input_().rstrip()))
