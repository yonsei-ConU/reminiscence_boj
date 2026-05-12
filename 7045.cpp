#include <iostream>
#include <vector>
#include <algorithm>

int N;

void dfs(int cur, int parent, const std::vector<std::vector<int>> &g, std::vector<int> &sz, std::vector<int> &centroid) {
    int max_subtree_size = 0;
    for (int nxt : g[cur]) {
        if (nxt == parent) continue;
        dfs(nxt, cur, g, sz, centroid);
        sz[cur] += sz[nxt];
        max_subtree_size = std::max(max_subtree_size, sz[nxt]);
    }
    if (max_subtree_size <= N / 2 && N - sz[cur] <= N / 2) {
        centroid.push_back(cur + 1);
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::cin >> N;
    std::vector<std::vector<int>> g(N);
    for (int i = 0; i < N - 1; i++) {
        int X, Y;
        std::cin >> X >> Y;
        g[--X].push_back(--Y);
        g[Y].push_back(X);
    }
    std::vector<int> sz(N, 1);
    std::vector<int> centroid;
    dfs(0, -1, g, sz, centroid);
    std::sort(centroid.begin(), centroid.end());
    for (int v : centroid) std::cout << v << '\n';
    return 0;
}
