import decimal

decimal.getcontext().prec = 500
γ = decimal.Decimal(
    "0.5772156649015328606065120900824024310421593359399235988057672348848677267776646709369470632917467495"
)

ln2 = decimal.Decimal(
    '0.6931471805599453094172321214581765680755001343602552541206800094933936219696947156058633269964186875420014810205706857336855202'
)


def harmonic(n):  #조화급수
    if n < 1000:
        r = decimal.Decimal("0")
        for i in range(1, n + 1):
            r += decimal.Decimal("1") / decimal.Decimal(str(i))
        return r
    else:
        return decimal.Decimal(n).ln() + γ + (decimal.Decimal(1) / decimal.Decimal(2 * n)) - (
            decimal.Decimal(1) / decimal.Decimal(12 * n * n))


n, k = map(int, input().split())
ans = n * (harmonic(n) - harmonic(n - k))
print(ans)
