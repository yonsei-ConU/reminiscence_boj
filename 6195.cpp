#include <iostream>
#include <vector>
#include <queue>

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int N;
    std::cin >> N;
    std::priority_queue<long long> planks;
    for (int i = 0; i < N; i++) {
        int t;
        std::cin >> t;
        planks.push(-t);
    }

    long long ans = 0;
    while (planks.size() != 1) {
        long long t1 = -planks.top(); planks.pop();
        long long t2 = -planks.top(); planks.pop();
        ans += t1 + t2;
        planks.push(-t1-t2);
    }

    std::cout << ans;
    return 0;
}
