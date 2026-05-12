#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, K;
    std::cin >> N >> K;
    int cur = 0;
    while (N--) {
        std::string word;
        std::cin >> word;
        if (cur + word.size() <= K) {
            if (cur) std::cout << ' ';
            cur += word.size();
        } else {
            std::cout << '\n';
            cur = word.size();
        }
        std::cout << word;
    }
    return 0;
}
