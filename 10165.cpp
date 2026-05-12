#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::vector<std::vector<int>> bus(M, std::vector<int>(3));
    for (int i = 1; i <= M; i++) {
        std::cin >> bus[i - 1][0] >> bus[i - 1][1];
        if (bus[i - 1][0] > bus[i - 1][1]) bus[i - 1][1] += N;
        bus[i - 1][2] = i;
    }

    std::sort(bus.begin(), bus.end(), [&](const std::vector<int> &a, const std::vector<int> &b) {
        if (a[0] < b[0]) return true;
        else if (a[0] > b[0]) return false;
        else if (a[1] > b[1]) return true;
        else if (a[1] < b[1]) return false;
        else return a[2] < b[2];
    });
    std::vector<std::pair<int, int>> survived;

    int mx = -1;
    for (auto vec : bus) {
        int end = vec[1];
        int idx = vec[2];
        if (end > mx) survived.emplace_back(end, idx);
        mx = std::max(mx, end);
    }

    std::vector<int> ans;
    for (auto & i : survived) {
        if (i.first > mx - N) ans.push_back(i.second);
    }
    std::sort(ans.begin(), ans.end());
    for (int val : ans) std::cout << val << ' ';
    return 0;
}
