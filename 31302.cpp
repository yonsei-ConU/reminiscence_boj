#include <iostream>
#include <string>
#include <vector>
#include <utility>

const int MOD = 9302023;

void update(std::vector<std::pair<int, int>> &dp, int i, int len) {
    int t = (i >= len ? dp[i - len].first : 0) + 1;
    if (t < dp[i].first) {
        dp[i] = (i >= len ? dp[i - len] : std::make_pair(0, 1));
        dp[i].first++;
    } else if (t == dp[i].first) {
        dp[i].second += i >= len ? dp[i - len].second : 0;
    }
    dp[i].second %= MOD;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string S;
    std::cin >> S;
    int N = S.size();

    std::vector<std::pair<int, int>> dp(N);
    dp[0] = {1, 1};

    for (int i = 1; i < N; i++) {
        dp[i] = dp[i - 1];
        dp[i].first++;
        if (S[i] == 'e') {
            // one, three, five, nine
            if (i >= 2 && S[i - 2] == 'o' && S[i - 1] == 'n') {
                update(dp, i, 3);
            } else if (i >= 4 && S[i - 4] == 't' && S[i - 3] == 'h' && S[i - 2] == 'r' && S[i - 1] == 'e') {
                update(dp, i, 5);
            } else if (i >= 3 && S[i - 3] == 'f' && S[i - 2] == 'i' && S[i - 1] == 'v') {
                update(dp, i, 4);
            } else if (i >= 3 && S[i - 3] == 'n' && S[i - 2] == 'i' && S[i - 1] == 'n') {
                update(dp, i, 4);
            }
        } else if (S[i] == 'o') {
            // zero, two
            if (i >= 3 && S[i - 3] == 'z' && S[i - 2] == 'e' && S[i - 1] == 'r') {
                update(dp, i, 4);
            } else if (i >= 2 && S[i - 2] == 't' && S[i - 1] == 'w') {
                update(dp, i, 3);
            }
        } else if (i >= 3 && S[i - 3] == 'f' && S[i - 2] == 'o' && S[i - 1] == 'u' && S[i] == 'r') {
            update(dp, i, 4);
        } else if (i >= 2 && S[i - 2] == 's' && S[i - 1] == 'i' && S[i] == 'x') {
            update(dp, i, 3);
        } else if (i >= 4 && S[i - 4] == 's' && S[i - 3] == 'e' && S[i - 2] == 'v' && S[i - 1] == 'e' && S[i] == 'n') {
            update(dp, i, 5);
        } else if (i >= 4 && S[i - 4] == 'e' && S[i - 3] == 'i' && S[i - 2] == 'g' && S[i - 1] == 'h' && S[i] == 't') {
            update(dp, i, 5);
        }
    }

    std::cout << dp[N - 1].first << '\n' << dp[N - 1].second;
    return 0;
}
