#include <iostream>
#include <vector>
#include <queue>

int pm[] = {-1, 1};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> clock(N);
    for (auto &i : clock) std::cin >> i;
    std::vector<std::vector<int>> g(N);
    for (int i = 0; i < N - 1; i++) {
        int c1, c2;
        std::cin >> c1 >> c2;
        g[--c1].push_back(--c2);
        g[c2].push_back(c1);
    }
    std::vector<int> dist(N, -1);
    dist[0] = 0;
    std::queue<int> q;
    q.push(0);
    while (!q.empty()) {
        int cur = q.front(); q.pop();
        for (int nxt : g[cur]) {
            if (dist[nxt] != -1) continue;
            dist[nxt] = dist[cur] + 1;
            q.push(nxt);
        }
    }
    int x = 0;
    int even = 0;
    for (int i = 0; i < N; i++) {
        x += clock[i] * pm[dist[i] & 1];
        if (!(dist[i] & 1)) even++;
    }
    x %= 12;
    if (x < 0) x += 12;
    if (!x) std::cout << N;
    else if (x == 11) std::cout << even;
    else if (x == 1) std::cout << N - even;
    else std::cout << 0;
    return 0;
}
