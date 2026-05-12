#include <iostream>
#include <vector>
#include <queue>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int tc = 1;
    while (true) {
        int n, m;
        std::cin >> n >> m;
        if (!n) break;
        std::vector<std::vector<int>> g(n);
        for (int i = 0; i < m; i++) {
            int u, v;
            std::cin >> u >> v;
            g[--u].push_back(--v);
            g[v].push_back(u);
        }
        int ans = 0;
        std::vector<bool> visited(n, false);
        std::vector<std::vector<bool>> edge_visited(n, std::vector<bool>(n, false));
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue;
            std::queue<int> q;
            q.push(i);
            visited[i] = true;
            bool chk = true;
            while (!q.empty()) {
                int cur = q.front(); q.pop();
                for (int nxt : g[cur]) {
                    if (visited[nxt]) {
                        if (!edge_visited[cur][nxt]) chk = false;
                    } else {
                        visited[nxt] = true;
                        q.push(nxt);
                    }
                    edge_visited[cur][nxt] = edge_visited[nxt][cur] = true;
                }
            }
            if (chk) ans++;
        }
        std::cout << "Case " << tc << ": ";
        if (!ans) std::cout << "No trees.\n";
        else if (ans == 1) std::cout << "There is one tree.\n";
        else {
            std::cout << "A forest of " << ans << " trees.\n";
        }
        tc++;
    }
    return 0;
}
