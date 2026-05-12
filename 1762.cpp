#include <iostream>
#include <vector>
#include <unordered_set>

typedef long long ll;

inline int intersection(const std::unordered_set<int> &a, const std::unordered_set<int> &b) {
    int ans = 0;
    if (a.size() < b.size()) {
        for (int x : a) {
            if (b.find(x) != b.end()) ans++;
        }
        return ans;
    } else {
        for (int x : b) {
            if (a.find(x) != a.end()) ans++;
        }
        return ans;
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::vector<std::unordered_set<int>> g(N);
    std::vector<int> deg(N);
    for (int i = 0; i < M; i++) {
        int u, v;
        std::cin >> u >> v;
        if (u > v) u ^= v ^= u ^= v;
        g[--u].insert(--v);
        deg[u]++;
    }
    std::vector<std::vector<int>> deg_to_id(100000);
    for (int i = 0; i < N; i++) {
        deg_to_id[deg[i]].push_back(i);
    }
    ll ans = 0;
    for (int u = 0; u < N; u++) {
        for (int v : g[u]) {
            ans += intersection(g[u], g[v]);
        }
        g[u].clear();
    }
//    for (int i = 0; i < N; i++) {
//        for (int u : deg_to_id[i]) {
//            for (int v : g[u]) {
//                ans += intersection(g[u], g[v]);
//            }
//            g[u].clear();
//        }
//    }
    std::cout << ans;
    return 0;
}
