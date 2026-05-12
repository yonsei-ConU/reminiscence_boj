#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>

inline int dist2(int x1, int y1, int x2, int y2) {
    return (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::pair<int, int> cows[N];
    for (int i = 0; i < N; i++) std::cin >> cows[i].first >> cows[i].second;
    std::vector<std::vector<std::pair<int, int>>> dist(N);
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) continue;
            dist[i].emplace_back(dist2(cows[i].first, cows[i].second, cows[j].first, cows[j].second), j);
        }
        std::sort(dist[i].begin(), dist[i].end());
    }
    int survived = N;
    bool surviving[N];
    for (int i = 0; i < N; i++) surviving[i] = true;
    int turn = 0;

    while (survived > 1) {
        while (!surviving[turn]) {
            turn++;
            if (turn == N) turn = 0;
        }
        for (int i = 0; i < N - 1; i++) {
            if (surviving[dist[turn][i].second]) {
                survived--;
                surviving[dist[turn][i].second] = false;
                break;
            }
        }
        turn++;
        if (turn == N) turn = 0;
    }

    for (int i = 0; i < N; i++) {
        if (surviving[i]) std::cout << i + 1;
    }
    return 0;
}
