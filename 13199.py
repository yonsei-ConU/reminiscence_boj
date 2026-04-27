import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for _ in range(int(input_())):
    P, M, F, C = minput()
    coupon = M // P * C
    ans = -(coupon // F)
    while coupon >= F:
        extra = coupon // F
        ans += extra
        coupon %= F
        coupon += extra * C
        print(coupon)
    print(ans)
