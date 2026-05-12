#include <iostream>
#include <vector>
#include <queue>

std::vector<std::pair<int, int> > dijkstra(const std::vector<std::vector<std::pair<int, int> > >& g, int st) {
    int INF = 2147483647;
    int N = g.size();
    std::vector<std::pair<int, int> > ret(N, std::make_pair(INF, INF));
    ret[st] = std::make_pair(0, INF);
    std::priority_queue<std::pair<int, int> > pq;
    pq.push(std::make_pair(0, st));
    while (!pq.empty()) {
        int dist = -pq.top().first;
        int cur = pq.top().second;
        pq.pop();
        if (dist > ret[cur].first) continue;
        for (const auto &edge: g[cur]) {
            int nextnum = edge.first;
            int nextdist = edge.second;
            if (ret[nextnum].first <= dist + nextdist) continue;
            ret[nextnum].first = dist + nextdist;
            pq.push(std::make_pair(-ret[nextnum].first, nextnum));
        }
    }
    return ret;
}

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int N, R;
    std::cin >> N >> R;
    std::vector<std::vector<std::pair<int, int> > > g(N);

    for (int i = 0; i < R; i++) {
        int A, B, D;
        std::cin >> A >> B >> D;
        A--;B--;
        g[A].push_back(std::make_pair(B, D));
        g[B].push_back(std::make_pair(A, D));
    }

    //
    return 0;
}
