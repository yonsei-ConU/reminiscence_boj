#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    if (N == 1) {
        std::cout << 1;
        return 0;
    }
    std::vector<int> A(N);
    for (auto &i : A) std::cin >> i;
    std::unordered_set<int> ans;

    // 2개
    for (int i = 0; i < N - 1; i++) {
        if (A[i] == A[i + 1]) ans.insert(A[i]);
    }
    // 3개
    for (int i = 0; i < N - 2; i++) {
        if (A[i] == A[i + 2]) ans.insert(A[i]);
    }

    std::cout << ans.size();
    return 0;
}