#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    if (N <= 4) {
        std::vector<std::pair<int, int>> edges = {
                {1, 2}, {1, 3}, {2, 3}, {1, 4}, {2, 4}, {3, 4}
        };
        if (N == 2) edges.resize(1);
        else if (N == 3) edges.resize(3);
        for (int i = 0; i < N - 1; i++) {
            int u, v;
            std::cin >> u >> v;
            if (u > v) u ^= v ^= u ^= v;
            std::pair<int, int> pp = {u, v};
            for (auto it = edges.begin(); it != edges.end(); it++) {
                if (*it == pp) {
                    edges.erase(it);
                    break;
                }
            }
        }
        std::cout << edges.size() << '\n';
        std::cout << "1\n";
        for (auto &[u, v] : edges) std::cout << u << ' ' << v << '\n';
    } else {
        std::vector<bool> chk(N, false);
        for (int i = 0; i < N - 1; i++) {
            int u, v;
            std::cin >> u >> v;
            if (u > v) u ^= v ^= u ^= v;
            if (u == 1) chk[v - 1] = true;
        }
        std::vector<std::pair<int, int>> ans;
        for (int i = 1; i < N; i++) {
            if (!chk[i]) ans.emplace_back(1, i + 1);
        }
        std::cout << ans.size() << '\n';
        std::cout << "2\n";
        for (auto &[u, v] : ans) std::cout << u << ' ' << v << '\n';
    }
    return 0;
}
