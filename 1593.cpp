#include <iostream>
#include <string>

inline int convert(char c) {
    if ('A' <= c && c <= 'Z') {
        return c - 'A';
    } else {
        return c - 'a' + 26;
    }
}

inline bool comp_array(int* a, int* b) {
    for (int i = 0; i < 52; i++) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int g, s;
    std::cin >> g >> s;
    std::string W, S;
    std::cin >> W >> S;
    int cnt[52] = {0};
    int goal_cnt[52] = {0};
    for (char c : W) {
        goal_cnt[convert(c)]++;
    }
    for (int i = 0; i < W.size(); i++) {
        cnt[convert(S[i])]++;
    }
    int ans = 0;
    if (comp_array(cnt, goal_cnt)) {
        ans++;
    }
    for (int ptr = W.size(); ptr < S.size(); ptr++) {
        cnt[convert(S[ptr])]++;
        cnt[convert(S[ptr - (int)W.size()])]--;
        if (comp_array(cnt, goal_cnt)) {
            ans++;
        }
    }
    std::cout << ans;
    return 0;
}
