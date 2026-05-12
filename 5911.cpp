#include <iostream>
#include <vector>
#include <algorithm>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, B;
    std::cin >> N >> B;
    std::vector<std::pair<int, int>> gifts(N);
    for (auto &i : gifts) {
        std::cin >> i.first >> i.second;
    }
    std::sort(gifts.begin(), gifts.end(), [](const std::pair<int, int> &a, const std::pair<int, int> &b) {
        return a.first + a.second < b.first + b.second;
    });
    int ans = 0;
    for (int i = 0; i < N; i++) {
        int cost = gifts[i].first + gifts[i].second;
        if (cost > B) break;
        B -= cost;
        ans++;
    }
    if (ans == N) {
        std::cout << ans;
        return 0;
    }
    int next_cost = gifts[ans].first + gifts[ans].second;
    for (int i = 0; i < ans; i++) {
        if (gifts[i].first / 2 + B >= next_cost) {
            std::cout << ans + 1;
            return 0;
        }
    }
    for (int i = ans; i < N; i++) {
        if (gifts[i].first / 2 + gifts[i].second <= B) {
            std::cout << ans + 1;
            return 0;
        }
    }
    std::cout << ans;
    return 0;
}
