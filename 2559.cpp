#include <iostream>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, K;
    std::cin >> N >> K;
    std::vector<int> t(N);
    for (auto &i : t) std::cin >> i;
    std::vector<int> psum = {0};
    for (int i = 0; i < N; i++) {
        psum.push_back(psum[i] + t[i]);
    }
    int ans = -2147483648;
    for (int i = 0; i + K <= N; i++) {
        ans = std::max(ans, psum[i + K] - psum[i]);
    }
    std::cout << ans;
    return 0;
}
