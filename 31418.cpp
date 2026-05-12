#include <iostream>

typedef long long ll;
const int MOD = 998244353;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int W, H, K, T;
    std::cin >> W >> H >> K >> T;
    ll ans = 1;
    for (int i = 0; i < K; i++) {
        int x, y;
        std::cin >> x >> y;
        ll l = std::max(1, x - T);
        ll r = std::min(W, x + T);
        ll u = std::max(1, y - T);
        ll d = std::min(H, y + T);
        ll mult = (r - l + 1) * (d - u + 1) % MOD;
        ans = (ans * mult) % MOD;
    }
    std::cout << ans;
    return 0;
}
