#include <iostream>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> A(N);
    for (auto &i : A) std::cin >> i;
    std::vector<std::vector<bool>> dp(N + 1, std::vector<bool>(1200001, false));
    dp[0][600000] = true;
    int i = 1;
    int ans = 0;
    for (int v : A) {
        for (int j = 0; j < 1200001; j++) {
            dp[i][j] = dp[i - 1][j];
            if (j >= v) dp[i][j] = dp[i][j] || dp[i - 1][j - v];
            if (j + v < 1200001) dp[i][j] = dp[i][j] || dp[i - 1][j + v];
        }
        i++;
    }
    int Q;
    std::cin >> Q;
    while (Q--) {
        int asdf;
        std::cin >> asdf;
        if (dp[N][600000 + asdf] || dp[N][600000 - asdf]) std::cout << "Y ";
        else std::cout << "N ";
    }
    return 0;
}
