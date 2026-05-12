#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    int p[5];
    for (int &v : p) std::cin >> v;
    std::vector<std::vector<int>> problems(5);
    for (int i = 0; i < N; i++) {
        int k, t;
        std::cin >> k >> t;
        problems[k - 1].push_back(t);
    }
    for (auto &vec : problems) std::sort(vec.begin(), vec.end());
    int ans = -60;
    for (int i = 0; i < 5; i++) {
        if (problems[i].empty()) continue;
        ans += 60;
        int sum = 0;
        int max = 0;
        int min = 999999999;
        for (int j = 0; j < p[i]; j++) {
            sum += problems[i][j];
            max = std::max(max, problems[i][j]);
            min = std::min(min, problems[i][j]);
        }
        ans += sum + max - min;
    }
    std::cout << ans;
    return 0;
}
