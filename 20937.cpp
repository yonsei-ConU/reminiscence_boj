#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    int cnt[50001] = {0};
    for (int i = 0; i < N; i++) {
        int c;
        std::cin >> c;
        cnt[c]++;
    }
    int ans = 0;
    for (int v : cnt) ans = std::max(ans, v);
    std::cout << ans;
    return 0;
}
