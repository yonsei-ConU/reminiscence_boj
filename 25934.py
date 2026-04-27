import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for tc in range(1, int(input_()) + 1):
    students, brownies = minput()
    print(f"Practice #{tc}: {students} {brownies}")
    groups = int(input_())
    for _ in range(groups):
        t = int(input_())
        while brownies <= t:
            brownies *= 2
        brownies -= t
        print(t, brownies)
    print()
