#include <iostream>
#include <vector>
#include <algorithm>

inline bool value(char s) {
    return (s == 'a') || (s == 'e') || (s == 'i') || (s == 'o') || (s == 'u');
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int L;
    std::cin >> L;
    while (L--) {
        int N;
        std::cin >> N;
        std::vector<std::pair<int, std::string>> runes(N);
        for (int i = 0; i < N; i++) {
            std::string s;
            std::cin >> s;
            int val = 0;
            bool last = false;
            for (char c : s) {
                if (value(c)) {
                    if (last) continue;
                    else {
                        last = true;
                        val--;
                    }
                } else last = false;
            }
            runes[i] = {val, s};
        }
        std::sort(runes.begin(), runes.end());
        for (auto &p : runes) std::cout << p.second << ' ';
        std::cout << '\n';
    }
    return 0;
}
