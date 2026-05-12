import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


lst = [int(input_()) for _ in range(6)]

# 6개짜리 처리
ans = lst.pop()

# 5개짜리 처리
five = lst.pop()
ans += five
# 5개짜리 하나를 붙이면 1개짜리는 11개까지 붙일 수 있음
lst[0] = max(0, lst[0] - 11 * five)

# 4개짜리 처리
four = lst.pop()
ans += four
# 4개짜리 하나를 붙이면 2개짜리는 5개까지 붙일 수 있음
two_remove = four * 5
if lst[1] > two_remove:
    lst[1] -= two_remove
else:
    two_remove -= lst[1]
    lst[1] = 0
    lst[0] = max(0, lst[0] - 4 * two_remove)

# 3개짜리 처리
three = lst.pop()
# 3개짜리는 판 하나에 4개까지 붙일 수 있음
ans += three >> 2
three &= 3
ans += 1

# 4개만큼 못 묶이고 남은 것들은 나머지 개임
if three == 1:
    # 1개가 채워졌으면 2개짜리 5개, 1개짜리 7개를 채울 수 있음
    one_remove = 7
    if lst[1] < 5:
        one_remove += 4 * (5 - lst[1])
        lst[1] = 0
    else:
        lst[1] -= 5
    lst[0] = max(0, lst[0] - one_remove)

elif three == 2:
    # 2개가 채워졌으면 2개짜리 3개, 1개짜리 6개를 채울 수 있음
    one_remove = 6
    if lst[1] < 3:
        one_remove += 4 * (3 - lst[1])
        lst[1] = 0
    else:
        lst[1] -= 3
    lst[0] = max(0, lst[0] - one_remove)

elif three == 3:
    # 3개가 채워졌으면 2개짜리 1개, 1개짜리 5개를 채울 수 있음
    one_remove = 5
    if lst[1] < 1:
        one_remove += 4 * (1 - lst[1])
        lst[1] = 0
    else:
        lst[1] -= 1
    lst[0] = max(0, lst[0] - one_remove)

else:
    ans -= 1

# 2개짜리 처리
two = lst.pop()
# 2개짜리는 판 하나에 9개까지 붙일 수 있음
ans += two // 9
two %= 9
# 이제 2짜리가 two개 붙어있는 판이 하나 있음
# 1짜리는 4 * (9 - two)개 붙일 수 있음
ans += bool(two) | bool(lst[0])
lst[0] = max(0, lst[0] - 4 * (9 - two))

# 1개짜리 처리
ans += (lst.pop() + 35) // 36

print(ans)
