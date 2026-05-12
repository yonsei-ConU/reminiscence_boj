#include <iostream>
#include <vector>
#include <queue>

typedef long long ll;
const int MOD = 1000000007;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::vector<std::vector<int>> g(N);
    for (int i = 0; i < M; i++) {
        int u, v;
        std::cin >> u >> v;
        g[--u].push_back(--v);
        g[v].push_back(u);
    }
    ll ans = 1;
    std::vector<bool> visited(N, false);
    for (int i = 0; i < N; i++) {
        if (visited[i]) continue;
        visited[i] = true;
        ll mult = 1;
        std::queue<int> q;
        q.push(i);
        while (!q.empty()) {
            int cur = q.front(); q.pop();
            for (int nxt : g[cur]) {
                if (!visited[nxt]) {
                    visited[nxt] = true;
                    mult++;
                    q.push(nxt);
                }
            }
        }
        ans = ans * mult % MOD;
    }
    std::cout << ans;
    return 0;
}