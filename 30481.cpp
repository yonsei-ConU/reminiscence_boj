#include <iostream>
#include <vector>
#include <algorithm>
typedef long long ll;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    ll N;
    std::cin >> N;
    if (N == 2) {
        std::cout << '*';
        return 0;
    }
    std::vector<ll> ans;
    // p(x + 1) = N
    ll p = 1;
    for (;p * p + 2 * p <= N;p++) {
        ll x = N / p - 1;
        if (!(N % p)) {
            ans.emplace_back(x);
        }
    }
    p = 2;
    for (;p * p < N;p++) {
        // sqrt(N) 이하에 대해서는 직접 만들어 보면서 브포
        std::vector<ll> table;
        ll q = N;
        while (q) {
            table.emplace_back(q % p);
            q /= p;
        }
        auto left = table.begin();
        auto right = table.end() - 1;
        bool ok = true;
        while (left < right) {
            if (*left != *right) {
                ok = false;
                break;
            }
            left++; right--;
        }
        if (ok) ans.push_back(p);
    }
    std::sort(ans.begin(), ans.end());
    ll last = 0;
    for (ll val : ans) {
        if (val == last) continue;
        else {
            last = val;
            std::cout << val << ' ';
        }
    }
    return 0;
}
