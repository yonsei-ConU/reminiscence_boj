#include <iostream>

typedef long long ll;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T;
    std::cin >> T;
    if (T == 1) {
        ll A, B;
        std::cin >> A >> B;
        ll C = A + B;
        std::string ans;
        while (C) {
            ans += 'a' + (C % 26);
            C /= 26;
        }
        while (ans.size() < 13) ans += 'a';
        std::cout << ans;
    } else {
        ll ans = 0;
        ll v = 1;
        std::string S;
        std::cin >> S;
        for (char c : S) {
            ans += v * (c - 'a');
            v *= 26;
        }
        std::cout << ans;
    }
    return 0;
}
