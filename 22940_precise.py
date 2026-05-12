import sys
from fractions import Fraction
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def gaussian_elimintaion(eq):
    """
    :param eq: equation matrix
    :return: reduced row echelon form
    """
    N = len(eq)  # 식의 개수
    M = len(eq[0])  # 미지수의 개수 + 1
    for i in range(N):
        for j in range(M):
            eq[i][j] = Fraction(eq[i][j])
    nonzero_col = -1
    pivot_row = 0
    while pivot_row < N:
        ok = False
        nonzero_row = -1
        for col in range(nonzero_col + 1, M - 1):
            for row in range(pivot_row, N):
                if eq[row][col]:
                    ok = True
                    nonzero_col = col
                    nonzero_row = row
                    break
            if ok:
                break
        if not ok:
            break
        eq[pivot_row], eq[nonzero_row] = eq[nonzero_row], eq[pivot_row]
        a = eq[pivot_row][nonzero_col]
        if a != 1:
            eq[pivot_row] = [i / a for i in eq[pivot_row]]
        for row in range(pivot_row + 1, N):
            a = eq[row][nonzero_col]
            eq[row] = [eq[row][col] - a * eq[pivot_row][col] for col in range(M)]
        pivot_row += 1
    for row in range(N - 1, -1, -1):
        pivot_col = None
        for col in range(M - 1):
            if eq[row][col] != 0:
                pivot_col = col
                break
        if pivot_col is None:
            continue
        for k in range(row):
            a = eq[k][pivot_col]
            eq[k] = [eq[k][col] - a * eq[row][col] for col in range(M)]
    return eq


N = int(input_())
equation = [list(minput()) for _ in range(N)]
print(*[i[-1] for i in gaussian_elimintaion(equation)])
print(gaussian_elimintaion(equation))
