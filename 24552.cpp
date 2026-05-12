#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string S;
    std::cin >> S;
    int plus = 0;
    int minus = 0;
    std::vector<int> height;
    int cur = 0;
    for (char c : S) {
        if (c == '(') {
            cur++;
            plus++;
        } else {
            cur--;
            minus++;
        }
        height.push_back(cur);
    }
    if (cur == -1) {
        int ans = 0;
        for (int i = 0; i < S.size(); i++) {
            if (S[i] == ')') ans++;
            if (height[i] == -1) {
                std::cout << ans;
                break;
            }
        }
    } else {
        int idx = -1;
        for (int i = (int)S.size() - 1; i >= 0; i--) {
            if (height[i] == 0) {
                idx = i;
                break;
            }
        }
        int ans = 0;
        for (int i = idx + 1; i < S.size(); i++) {
            if (S[i] == '(') ans++;
        }
        std::cout << ans;
    }
    return 0;
}