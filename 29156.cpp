#include <iostream>
#include <iomanip>
#include <vector>
#include <cmath>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> length(N);
    for (int &i : length) std::cin >> i;
    std::vector<int> psum = {0};
    for (int v : length) psum.push_back(psum.back() + v);
    double L;
    std::cin >> L;
    int Q;
    std::cin >> Q;
    while (Q--) {
        int q;
        std::cin >> q;
        double ans = (double)psum[q - 1] + (double)length[q - 1] / 2 - L / 2;
        ans = (double)std::floor(ans * 100) / 100;
        if (ans > psum.back() - L) ans = psum.back() - L;
        if (ans < 0) ans = 0;
        std::cout << std::fixed << std::setprecision(2) << ans << '\n';
    }
    return 0;
}