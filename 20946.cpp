#include <iostream>
#include <vector>

typedef long long ll;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    ll N;
    std::cin >> N;
    ll n = N;
    std::vector<ll> factors;
    for (ll i = 2; i * i <= n; i++) {
        while (!(n % i)) {
            factors.push_back(i);
            n /= i;
        }
    }
    if (n > 1) factors.push_back(n);
    if (factors.size() == 1) {
        std::cout << -1;
        return 0;
    }
    int ptr = 0;
    while (ptr < factors.size()) {
        if (ptr + 3 == factors.size()) {
            std::cout << factors[ptr] * factors[ptr + 1] * factors[ptr + 2];
            ptr += 3;
        } else {
            std::cout << factors[ptr] * factors[ptr + 1] << ' ';
            ptr += 2;
        }
    }
    return 0;
}