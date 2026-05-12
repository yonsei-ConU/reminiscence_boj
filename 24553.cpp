#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T;
    std::cin >> T;
    while (T--) {
        long long N;
        std::cin >> N;
        std::cout << ((int)(N % 10 == 0)) << '\n';
    }
    return 0;
}