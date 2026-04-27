import sys
from collections import defaultdict
input_ = sys.stdin.readline
def minput(): return map(int, input().split())

N, money, Q = minput()
groups = [list() for i in range(101)]
companies = dict()
stocks = defaultdict(int)

for _ in range(N):
    G, H, P = input().split()
    G = int(G)
    P = int(P)
    groups[G].append(H)
    companies[H] = P

for _ in range(Q):
    query = input().split()

    if query[0] == '1':
        B = int(query[2])
        if money >= companies[query[1]] * B:
            money -= companies[query[1]] * B
            stocks[query[1]] += B
        else:
            amount = money // companies[query[1]]
            money -= amount * companies[query[1]]
            stocks[query[1]] += amount

    elif query[0] == '2':
        B = int(query[2])
        if stocks[query[1]] >= B:
            stocks[query[1]] -= B
            money += B * companies[query[1]]
        else:
            money += stocks[query[1]] * companies[query[1]]
            stocks[query[1]] = 0

    elif query[0] == '3':
        C = int(query[2])
        companies[query[1]] += C

    elif query[0] == '4':
        D, C = map(int, query[1:])
        for company_name in groups[D]:
            companies[company_name] += C

    elif query[0] == '5':
        D, E = map(int, query[1:])
        for company_name in groups[D]:
            cur = companies[company_name]
            cur *= 100 + E
            cur = 10 * int(cur // 1000)
            companies[company_name] = cur

    elif query[0] == '6':
        print(money)

    elif query[0] == '7':
        ans = money
        for company_name in stocks:
            ans += companies[company_name] * stocks[company_name]
        print(ans)
