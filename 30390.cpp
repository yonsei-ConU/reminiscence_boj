#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    ll A, B, K;
    std::cin >> A >> B >> K;
    ll X = A + B;
    std::vector<ll> divisors;
    int sz = 0;
    for (ll d = 1; d * d <= X; d++) {
        if (!(X % d)) {
            divisors.push_back(d);
            divisors.push_back(X / d);
            sz += 2;
        }
    }
    std::sort(divisors.begin(), divisors.end());
    for (int idx = sz - 1; sz >= 0; idx--) {
        ll v = divisors[idx];
        ll m = std::min(A % v, B % v);
        if (m <= K) {
            std::cout << v;
            return 0;
        }
    }
    return 1;
}
