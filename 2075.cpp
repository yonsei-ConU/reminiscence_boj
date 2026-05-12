#include <iostream>
#include <vector>
#include <queue>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> idx(N, N - 1);
    std::vector<std::vector<int>> num(N, std::vector<int>(N));
    for (auto &i : num) {
        for (auto &j : i) std::cin >> j;
    }
    std::priority_queue<std::pair<int, int>> q;
    for (int i = 0; i < N; i++) {
        q.emplace(num[idx[i]][i], i);
        idx[i]--;
    }
    int c = 1;
    while (!q.empty()) {
        auto [v, i] = q.top(); q.pop();
        if (c == N) {
            std::cout << v;
            break;
        }
        c++;
        if (idx[i] >= 0) q.emplace(num[idx[i]][i], i);
        idx[i]--;
    }
    return 0;
}
