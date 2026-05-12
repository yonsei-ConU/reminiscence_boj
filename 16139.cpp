#include <iostream>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string s;
    std::cin >> s;
    std::vector<std::vector<int>> psum(26, {0});
    for (int i = 0; i < s.size(); i++) {
        int idx = s[i] - 97;
        for (int j = 0; j < 26; j++) {
            if (j == idx) {
                psum[j].push_back(psum[j].back() + 1);
            } else {
                psum[j].push_back(psum[j].back());
            }
        }
    }
    for (int i = 0; i < 26; i++) {
        while (psum[i].size() < s.size()) {
            psum[i].push_back(psum[i].back());
        }
    }
    int q;
    std::cin >> q;
    while (q--) {
        char alph;
        int l, r;
        std::cin >> alph >> l >> r;
        std::cout << psum[alph - 97][r + 1] - psum[alph - 97][l] << '\n';
    }
    return 0;
}
