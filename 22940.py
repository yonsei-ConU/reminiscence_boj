import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def gaussian_elimintaion(eq):
    """
    :param eq: equation matrix
    :return: reduced row echelon form
    """
    N = len(eq)  # 식의 개수
    M = len(eq[0])  # 미지수의 개수 + 1
    nonzero_col = -1
    pivot_row = 0
    # Step 5. Now cover the top row and begin again with Step 1 to the submatrix that remains. Continue in this way until the entire matrix is in row echelon form.
    while pivot_row < N:
        # Step 1. Locate the leftmost column that does not consist entirely of zero.
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
        # Step 2. Interchange the top row with another row, if necessary, to bring a nonzero entry to the top of the column found in Step 1.
        eq[pivot_row], eq[nonzero_row] = eq[nonzero_row], eq[pivot_row]
        # Step 3. If the top entry of the column in Step 2 is 'a', multiply the first row by 1/a to introduce a leading 1.
        a = eq[pivot_row][nonzero_col]
        if a != 1:
            eq[pivot_row] = [i / a for i in eq[pivot_row]]
        # Step 4. Add suitable multiple of the top row to the rows below so that all entries below the leading 1 become zeros.
        for row in range(pivot_row + 1, N):
            a = eq[row][nonzero_col]
            eq[row] = [eq[row][col] - a * eq[pivot_row][col] for col in range(M)]
        pivot_row += 1
    # Step 6. Beginning with the last nonzero row and working upward, add suitable multiple of each row to the rows above to introduce zeros above the leading 1’s
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
print(*[round(i[-1]) for i in gaussian_elimintaion(equation)])
