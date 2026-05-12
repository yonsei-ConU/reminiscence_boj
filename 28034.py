import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def range_merge(r1, r2):
    if not r1 or not r2:
        return range(0)

    len_r1 = len(r1)
    len_r2 = len(r2)

    if len_r1 == 1 and len_r2 == 1:
        step_s3 = 1
    elif len_r1 == 1:
        step_s3 = r2.step
    elif len_r2 == 1:
        step_s3 = r1.step
    elif r1.step == 1 or r2.step == 1:
        step_s3 = 1
    else:
        step_s3 = 2

    min_sum = r1.start + r2.start
    max_sum = r1[-1] + r2[-1]
    return range(min_sum, max_sum + step_s3, step_s3)


"""
...F or F... (F가 k개) : 0,...,k점까지 모두 만들 수 있음
   EF...FE (F가 m개)   : range((m & 1) ^ 1, m + 2, 2)
   EF...FB (F가 n개)   : range(n & 1, n + 1, 2)
"""
N = int(input_())
S = input_().rstrip()

# 양쪽 끝에서 시작하는 연속된 F의 개수를 구함
lf = 0
while lf <= N - 1 and S[lf] == 'F':
    lf += 1
rf = 0
while rf <= N - 1 and S[N - 1 - rf] == 'F':
    rf += 1

# F만으로 이루어진 문자열일 때
if lf == rf == N:
    sys.stdout.write(str(N) + '\n')
    for i in range(N):
        sys.stdout.write(str(i) + '\n')
    sys.exit(0)

# B, E가 적어도 하나 포함되어 있음
else:
    # B 연속, E 연속은 고정적으로 더함
    t = sum(1 for i in range(N - 1) if S[i] == S[i + 1] != 'F')
    ans = range(t, t + 1)

    # 양끝 연속된 F와 합침
    ans = range_merge(ans, range(lf + 1))
    ans = range_merge(ans, range(rf + 1))

    # 양끝이 아닌 문자열에서 연속된 F 계산
    f = 0
    last = 0
    for idx in range(lf, N - rf):
        if S[idx] != 'F':
            if f:
                if S[idx] == S[last]:
                    ans = range_merge(ans, range((f & 1) ^ 1, f + 2, 2))
                else:
                    ans = range_merge(ans, range(f & 1, f + 1, 2))
            f = 0
            last = idx
        else:
            f += 1

print(len(ans))
for a in ans:
    print(a)
