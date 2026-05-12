#include <iostream>

typedef long long ll;
const int mod = 1000000007;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, L, R;
    std::cin >> N >> L >> R;
    int dp[N + 1][L + 1][R + 1];
    for (int i = 0; i <= N; i++) {
        for (int j = 0; j <= L; j++) {
            for (int k = 0; k <= R; k++) dp[i][j][k] = 0;
        }
    }

    dp[1][1][1] = 1;
    for (int i = 2; i <= N; i++) {
        for (int j = 1; j <= L && j <= i; j++) {
            for (int k = 1; k <= R && k <= i; k++) {
                ll ttmp = (ll)(i - 2) * dp[i - 1][j][k];
                int tmp = ttmp % mod;
                tmp += dp[i - 1][j][k - 1];
                if (tmp >= mod) tmp -= mod;
                tmp += dp[i - 1][j - 1][k];
                if (tmp >= mod) tmp -= mod;
                dp[i][j][k] = tmp;
            }
        }
    }

    std::cout << dp[N][L][R];
    return 0;
}
