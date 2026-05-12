#include <iostream>
#include <vector>
#include <algorithm>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> A(N);
    for (auto &i : A) std::cin >> i;
    int ans = 0;

    // 2개
    for (int i = 0; i < N - 1; i++) {
        ans = std::max(ans, std::min(A[i], A[i + 1]));
    }
    // 3개
    for (int i = 0; i < N - 2; i++) {
        std::vector<int> vec = {A[i], A[i + 1], A[i + 2]};
        std::sort(vec.begin(), vec.end());
        ans = std::max(ans, vec[1]);
    }

    std::cout << ans;
    return 0;
}
