#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string S, ans;
    for (int i = 0; i < 100; i++) S += '2';
    int K;
    std::cin >> K;
    for (int i = 0; i < 100; i++) {
        S[i] = '0';
        std::cout << "? " << S << '\n' << std::flush;
        int response;
        std::cin >> response;
        if (response == K) ans += '0';
        else if (response == K - 1) ans += '5';
        else ans += '2';
        S[i] = '2';
    }
    std::cout << "! " << ans << '\n' << std::flush;
    return 0;
}
