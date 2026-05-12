#include <iostream>
#include <vector>
#include <map>
#include <array>

typedef long long ll;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, K;
    std::cin >> N >> K;
    std::map<int, std::pair<int, std::vector<int>>> X, Y;
    for (int i = 0; i < N; i++) {
        int x, y;
        std::cin >> x >> y;
        x /= 2; y /= 2;
        std::string pattern;
        std::cin >> pattern;
        X[x].first = y;
        Y[y].first = x;
        for (int j = 0; j < K; j++) {
            X[x].second[j] = pattern[j] - '1';
            Y[y].second[j] = pattern[j] - '1';
        }
    }

    std::map<std::array<int, 4>, std::array<int, 4>> nxt; // x, y, direction, time
    return 0;
}
