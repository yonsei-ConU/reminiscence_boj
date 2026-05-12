#include <iostream>
#include <queue>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, K;
    std::cin >> N >> K;
    int B[N];
    for (auto &i : B) std::cin >> i;
    int ans = 0;
    for (int mx = 1; mx <= 1000; mx++) {
        std::priority_queue<int> baskets;
        int x = 0;
        for (int b : B) {
            while (b >= mx) {
                b -= mx;
                baskets.push(mx);
                x++;
            }
            baskets.push(b);
            x++;
        }
        while (x < K) {
            int t = baskets.top(); baskets.pop();
            baskets.push(t >> 1);
            baskets.push((t >> 1) & 1);
            x++;
        }
        for (int i = 0; i < K / 2; i++) baskets.pop();
        int tmp = 0;
        for (int i = 0; i < K / 2; i++) {
            tmp += baskets.top(); baskets.pop();
        }
        ans = std::max(ans, tmp);
    }
    std::cout << ans;
    return 0;
}
