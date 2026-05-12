#include <iostream>
#include <vector>

inline int convert(char c) {
    if (c == 'A') return 0;
    else if (c == 'B') return 1;
    else return 2;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string S;
    std::cin >> S;
    std::vector<std::vector<int>> DFA(8, std::vector<int>(3));
    DFA[0] = {7, 1, 7};
    DFA[1] = {2, 1, 7};
    DFA[2] = {7, 7, 3};
    DFA[3] = {4, 7, 7};
    DFA[4] = {7, 7, 5};
    DFA[5] = {6, 7, 7};
    DFA[6] = {7, 1, 5};
    DFA[7] = {7, 7, 7};
    // dp[i][j] = i번째 글자가 j번 상태일 때 최소 횟수
    std::vector<std::vector<int>> dp(S.size() + 1, std::vector<int>(7, 0x3f3f3f3f));
    dp[0][0] = 0;
    for (int i = 0; i < S.size(); i++) {
        int c = convert(S[i]);
        for (int cur = 0; cur < 8; cur++) {
            for (int j = 0; j < 3; j++) {
                int nxt = DFA[cur][j];
                int d = j != c;
                dp[i + 1][nxt] = std::min(dp[i + 1][nxt], dp[i][cur] + d);
            }
        }
    }
    std::cout << dp[S.size()][6];
    return 0;
}
