#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

std::vector<std::pair<int, int>> dijkstra(const std::vector<std::vector<std::pair<int, int>>>& g, const std::vector<int> &t, int st) {
    int INF = 2147483647;
    int N = g.size();
    std::vector<std::pair<int, int>> ret(N, {INF, 0});
    ret[st] = {0, t[st]};
    std::priority_queue<std::pair<int, int> > pq;
    pq.emplace(0, st);
    while (!pq.empty()) {
        int dist = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        if (dist > ret[cur].first) continue;
        for (const auto &edge: g[cur]) {
            int nextnum = edge.first;
            int nextdist = edge.second;
            if (ret[nextnum].first == dist + nextdist) {
                ret[nextnum].second = std::max(ret[nextnum].second, ret[cur].second + t[nextnum]);
            } else if (ret[nextnum].first > dist + nextdist) {
                ret[nextnum].first = dist + nextdist;
                ret[nextnum].second = ret[cur].second + t[nextnum];
                pq.emplace(-ret[nextnum].first, nextnum);
            }
        }
    }
    return ret;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<int> t(n);
    for (auto &i : t) std::cin >> i;
    int m;
    std::cin >> m;
    std::vector<std::vector<std::pair<int, int>>> g(n);
    while (m--) {
        int a, b, d;
        std::cin >> a >> b >> d;
        g[--a].emplace_back(--b, d);
        g[b].emplace_back(a, d);
    }
    std::vector<std::pair<int, int>> dist = dijkstra(g, t, 0);
    if (dist[n - 1].first == 2147483647) {
        std::cout << "impossible";
        return 0;
    }
    std::cout << dist[n - 1].first << ' ' << dist[n - 1].second;
    return 0;
}
