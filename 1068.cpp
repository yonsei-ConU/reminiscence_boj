#include <iostream>
#include <vector>

int remove_node;

void dfs(int cur, const std::vector<std::vector<int>> &g, std::vector<int> &sz) {
    sz[cur] = 1;
    for (int nxt : g[cur]) {
        if (nxt == remove_node) {
            continue;
        }
        dfs(nxt, g, sz);
        sz[cur] += sz[nxt];
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, root;
    std::cin >> N;
    std::vector<std::vector<int>> g(N);
    for (int i = 0; i < N; i++) {
        int par;
        std::cin >> par;
        if (par == -1) {
            root = i;
        } else {
            g[par].push_back(i);
        }
    }
    std::cin >> remove_node;
    std::vector<int> sz(N, 0);
    if (root != remove_node) {
        dfs(root, g, sz);
    }
    int ans = 0;
    for (int x : sz) {
        if (x == 1) ans++;
    }
    std::cout << ans;
    return 0;
}
