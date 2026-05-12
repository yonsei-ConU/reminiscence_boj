#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T;
    std::cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        int N;
        std::cin >> N;
        int C[N];
        for (auto &v : C) std::cin >> v;
        int ans = -1;
        for (int mask = 1; mask < (1 << N) - 1; mask++) {
            int v = 0, s = 0, p = 0;
            for (int i = 0; i < N; i++) {
                if (mask & (1 << i)) {
                    v += C[i];
                    s ^= C[i];
                } else {
                    p ^= C[i];
                }
            }
            if (s == p) ans = std::max(ans, v);
        }
        std::cout << "Case #" << tc << ": ";
        if (ans == -1) std::cout << "NO\n";
        else std::cout << ans << '\n';
    }
    return 0;
}
