#include <iostream>
#include <vector>
#include <deque>

inline int go(const int &cur, const std::pair<int, int> &p) {
    return cur ^ p.first ^ p.second;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<std::vector<std::pair<int, int>>> g(N);
    std::vector<int> odd_degree;
    int e = 0;
    for (int i = 0; i < N; i++) {
        int deg = 0;
        for (int j = 0; j < i; j++) {
            int t;
            std::cin >> t;
            deg += t;
            while (t--) {
                g[i].emplace_back(j, e);
                g[j].emplace_back(i, e++);
            }
        }
        for (int j = i; j < N; j++) {
            int t;
            std::cin >> t;
            deg += t;
        }
        if (deg & 1) odd_degree.push_back(i);
    }
    if (!odd_degree.empty()) {
        std::cout << -1;
        return 0;
    }
    std::vector<bool> used(e, false);
    std::vector<int> ptr(N, 0);
    odd_degree.push_back(0);
    std::deque<std::pair<int, int>> trail;
    int cur = odd_degree[0];
    while (e) {
        while (ptr[cur] < g[cur].size() && used[g[cur][ptr[cur]].second]) {
            ptr[cur]++;
        }
        if (ptr[cur] == g[cur].size()) {
            cur = go(cur, trail.back());
            trail.push_front(trail.back());
            trail.pop_back();
        } else {
            auto &[nxt, eid] = g[cur][ptr[cur]];
            used[eid] = true;
            trail.emplace_back(cur, nxt);
            cur = nxt;
            e--;
        }
    }
    auto &e1 = trail.front();
    auto &e2 = trail.back();
    if (e1.first == e2.first || e1.first == e2.second) cur = e1.first;
    else cur = e1.second;
    int start = cur;
    for (auto &p : trail) {
        std::cout << cur + 1 << ' ';
        cur = go(cur, p);
    }
    std::cout << start + 1;
    return 0;
}
