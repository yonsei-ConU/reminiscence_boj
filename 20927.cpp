#include <iostream>
#include <vector>
#include <algorithm>
#include "algorithms.cpp"
using namespace ConU;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    if (N - 1 > M) {
        std::cout << "NO";
        return 0;
    }
    std::vector<int> b(N);
    for (int i = 0; i < N; i++) std::cin >> b[i];
    std::vector<std::vector<int>> edges;
    for (int i = 0; i < M; i++) {
        int p, q, r;
        std::cin >> p >> q >> r;
        edges.push_back({p - 1, q - 1, r});
    }
    int ans_weight = 1000000000;
    std::vector<std::vector<int>> ans;
    std::vector<bool> select(M, false);
    std::fill(select.end() - N + 1, select.end(), true);
    do {
        UnionFind uf(N);
        int cost = 0;
        bool ok = true;
        std::vector<int> deg(N);
        for (int i = 0; i < M; i++) {
            if (select[i]) {
                if (uf.find(edges[i][0]) == uf.find(edges[i][1])) {
                    ok = false;
                    break;
                }
                uf.unite(edges[i][0], edges[i][1]);
                cost += edges[i][2];
                deg[edges[i][0]]++;
                deg[edges[i][1]]++;
            }
        }
        for (int i = 0; i < N; i++) {
            if (deg[i] > b[i]) {
                ok = false;
                break;
            }
        }
        if (ok && uf.size[uf.find(0)] == N) {
            if (cost < ans_weight) {
                ans_weight = cost;
                ans.clear();
                for (int i = 0; i < M; i++) {
                    if (select[i]) {
                        ans.push_back({edges[i][0], edges[i][1]});
                    }
                }
            }
        }
    } while (std::next_permutation(select.begin(), select.end()));
    if (ans_weight == 1000000000) {
        std::cout << "NO";
    } else {
        std::cout << "YES\n";
        for (auto edge : ans) {
            std::cout << edge[0] + 1 << ' ' << edge[1] + 1 << '\n';
        }
    }
    return 0;
}
