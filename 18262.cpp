#include <iostream>
#include <vector>
#include <queue>

std::vector<int> dijkstra(const std::vector<std::vector<std::pair<int, int>>>& g, int st) {
    int INF = 2147483647;
    int N = g.size();
    std::vector<int> ret(N, INF);
    ret[st] = 0;
    std::priority_queue<std::pair<int, int>> pq;
    pq.emplace(0, st);
    while (!pq.empty()) {
        int dist = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        if (dist > ret[cur]) continue;
        for (const auto &edge: g[cur]) {
            int nextnum = edge.first;
            int nextdist = edge.second;
            if (ret[nextnum] <= dist + nextdist) continue;
            ret[nextnum] = dist + nextdist;
            pq.emplace(-ret[nextnum], nextnum);
        }
    }
    return ret;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::vector<std::vector<std::vector<int>>> edges(1001);
    while (M--) {
        int a, b, c, f;
        std::cin >> a >> b >> c >> f;
        edges[f].push_back({a - 1, b - 1, c});
    }
    std::vector<std::vector<std::pair<int, int>>> g(N);
    int ans = 0;
    for (int flow = 1000; flow > 0; flow--) {
        for (std::vector<int> &edge : edges[flow]) {
            g[edge[0]].emplace_back(edge[1], edge[2]);
            g[edge[1]].emplace_back(edge[0], edge[2]);
        }
        std::vector<int> dist = dijkstra(g, 0);
        ans = std::max(ans, flow * 1000000 / dist[N - 1]);
    }
    std::cout << ans;
    return 0;
}
