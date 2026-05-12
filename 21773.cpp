#include <iostream>
#include <queue>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T, n;
    std::cin >> T >> n;
    std::priority_queue<std::array<int, 3>> process;
    for (int i = 0; i < n; i++) {
        int A, B, C;
        std::cin >> A >> B >> C;
        process.push({C, -A, B});
    }
    while (T--) {
        auto &cur = process.top();
        std::cout << -cur[1] << '\n';
        if (cur[2] > 1) process.push({cur[0] - 1, cur[1], cur[2] - 1});
        process.pop();
    }
    return 0;
}
