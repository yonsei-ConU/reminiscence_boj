#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<std::vector<int>> transitions(n);
    for (int i = 0; i < n; i++) {
        int m;
        std::cin >> m;
        while (m--) {
            std::string s;
            std::cin >> s;
            int v = 0;
            for (char c : s) {
                v |= 1 << (c - 'a');
            }
            transitions[i].push_back(v);
        }
    }
    std::vector<std::vector<int>> dp(n, std::vector<int>(n, 999999999));
    for (int i = 0; i < n; i++) dp[i][i] = 0;
    for (int end = 0; end < n; end++) {
        int mask = 1 << end;
        while (true) {
            int new_mask = 0;
            for (int start = 0; start < n; start++) {
                if (mask & (1 << start)) continue;
                bool chk = false;
                for (int trans : transitions[start]) {
                    if ((trans & mask) == trans) {
                        chk = true;
                        int t = 0;
                        for (int j = 0; j < n; j++) {
                            if (trans & (1 << j)) t = std::max(t, dp[j][end]);
                        }
                        dp[start][end] = std::min(dp[start][end], t + 1);
                    }
                }
                if (chk) new_mask |= 1 << start;
            }
            if (!new_mask) break;
            mask |= new_mask;
        }
    }
    for (auto &vec : dp) {
        for (int v : vec) {
            if (v == 999999999) std::cout << "-1 ";
            else std::cout << v << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}
