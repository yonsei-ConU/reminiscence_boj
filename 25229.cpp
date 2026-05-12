#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

const int MX = 1500;

int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

void dfs(int cur, int parent, const std::vector<int> &v, const std::vector<std::vector<int>> &g, std::vector<std::vector<ll>> &dp, const std::vector<std::vector<int>> &harmonic) {
    for (int cur_num = 1; cur_num <= MX; cur_num++) {
        if (cur_num == v[cur]) {
            dp[cur][cur_num] = 0;
        } else {
            dp[cur][cur_num] = cur_num;
        }
    }
    for (int nxt : g[cur]) {
        if (nxt == parent) continue;
        dfs(nxt, cur, v, g, dp, harmonic);
        for (int cur_num = 1; cur_num <= MX; cur_num++) {
            ll tmp = 1000000000LL;
            for (int child_num : harmonic[cur_num]) {
                tmp = std::min(tmp, dp[nxt][child_num]);
            }
            dp[cur][cur_num] = std::min(1000000000LL, dp[cur][cur_num] + tmp);
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<int> v(n);
    for (int i = 0; i < n; i++) {
        std::cin >> v[i];
    }
    std::vector<std::vector<int>> g(n);
    for (int i = 0; i < n - 1; i++) {
        int a, b;
        std::cin >> a >> b;
        g[--a].push_back(--b);
        g[b].push_back(a);
    }
    std::vector<std::vector<ll>> dp(n, std::vector<ll>(MX + 1, 1000000000));
    std::vector<std::vector<int>> harmonic(MX + 1);
    for (int i = 1; i <= MX; i++) {
        for (int j = 1; j <= MX; j++) {
            if (gcd(i, j) != 1) harmonic[i].push_back(j);
        }
    }
    dfs(0, 0, v, g, dp, harmonic);
    ll ans = 1000000000;
    for (int i = 1; i <= MX; i++) {
        if (dp[0][i] < ans) ans = dp[0][i];
    }

    std::cout << ans;
    return 0;
}
