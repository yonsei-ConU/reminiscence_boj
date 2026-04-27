#include <iostream>
#include <set>

typedef long long ll;

struct Line {
    mutable ll k, m, p;
    bool operator<(const Line& o) const { return k < o.k; }
    bool operator<(ll x) const { return p < x; }
};

struct LineContainer : std::multiset<Line, std::less<>> {
    // (for doubles, use inf = 1/.0, div(a,b) = a/b)
    static const ll inf = 9223372036854775807;
    ll div(ll a, ll b) { // floored division
        return a / b - ((a ^ b) < 0 && a % b); }
    bool isect(iterator x, iterator y) {
        if (y == end()) return x->p = inf, 0;
        if (x->k == y->k) x->p = x->m > y->m ? inf : -inf;
        else x->p = div(y->m - x->m, x->k - y->k);
        return x->p >= y->p;
    }
    void add(ll k, ll m) {
        auto z = insert({k, m, 0}), y = z++, x = y;
        while (isect(y, z)) z = erase(z);
        if (x != begin() && isect(--x, y)) isect(x, y = erase(y));
        while ((y = x) != begin() && (--x)->p >= y->p)
            isect(x, erase(y));
    }
    ll query(ll x) {
        auto l = *lower_bound(x);
        return l.k * x + l.m;
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    LineContainer lc;
    int Q;
    std::cin >> Q;
    while (Q--) {
        int q;
        std::cin >> q;
        if (q == 1) {
            ll a, b;
            std::cin >> a >> b;
            lc.add(a, b);
        } else {
            ll x;
            std::cin >> x;
            std::cout << lc.query(x) << '\n';
        }
    }
    return 0;
}
