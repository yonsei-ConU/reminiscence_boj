#include <iostream>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string S, T;
    std::cin >> S >> T;
    std::vector<int> fail(T.size(), 0);
    int j = 0;
    for (int i = 1; i < T.size(); i++) {
        while (j > 0 && T[i] != T[j]) j = fail[j - 1];
        if (T[i] == T[j]) {
            j++;
            fail[i] = j;
        }
    }
    std::vector<int> J(S.size() + 1, 0);
    std::vector<char> ans(S.size());
    j = 0;
    int r = 0;
    for (char c : S) {
        ans[r++] = c;
        while (j > 0 && c != T[j]) j = fail[j - 1];
        if (c == T[j]) j++;
        J[r] = j;
        if (j == (int)T.size()) {
            r -= (int)T.size();
            j = J[r];
        }
    }
    for (int i = 0; i < r; i++) {
        std::cout << ans[i];
    }
    return 0;
}
