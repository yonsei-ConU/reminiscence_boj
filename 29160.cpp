#include <iostream>
#include <queue>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, K;
    std::cin >> N >> K;
    std::vector<std::priority_queue<int>> players(11);
    for (int i = 0; i < N; i++) {
        int P, W;
        std::cin >> P >> W;
        players[P - 1].push(W);
    }
    int ans = 0;
    while (K--) {
        for (int i = 0; i < 11; i++) {
            if (players[i].empty()) continue;
            int t = players[i].top(); players[i].pop();
            players[i].push(std::max(0, t - 1));
        }
        ans = 0;
        for (int i = 0; i < 11; i++) {
            if (players[i].empty()) continue;
            ans += players[i].top();
        }
    }
    std::cout << ans;
    return 0;
}