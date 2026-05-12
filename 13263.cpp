#include <iostream>
#include <vector>
#include <set>

typedef long long ll;

struct Line {
    mutable ll p, q, x;
};

struct stack_cht {
    // assuming that no duplicate inclination line is added
    static const ll inf = 9223372036854775807;
    std::vector<Line> s;
    ll div(ll a, ll b) { // floored division
        return a / b - ((a ^ b) < 0 && a % b); }
    void add(ll p, ll q) {
        if (s.empty()) {
            s.push_back({p, q, -inf});
        } else {
            while (true) {
                auto &top = s.back();
                if (top.p == p) {
                    if (top.q < q) continue;
                    else break;
                }
                ll intersection = div(q - top.q, top.p - p);
                if (intersection <= top.x) {
                    s.pop_back();
                } else {
                    s.push_back({p, q, intersection});
                    break;
                }
            }
        }
    }
    ll query(ll x) {
        int lo = -1;
        int hi = (int)s.size();
        while (lo + 1 < hi) {
            int mid = (lo + hi) / 2;
            if (s[mid].x < x) lo = mid;
            else hi = mid;
        }
        return s[lo].p * x + s[lo].q;
    }
};

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<ll> a(n), b(n);
    for (auto &i : a) std::cin >> i;
    for (auto &i : b) std::cin >> i;
    stack_cht cht;
    cht.add(b[0], 0);
    ll ans = 0;
    for (int i = 1; i < n; i++) {
        ll x = cht.query(a[i]);
        ans = x;
        cht.add(b[i], x);
    }
    std::cout << ans;
    return 0;
}
