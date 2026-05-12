#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int k, s, e;
    std::cin >> k >> s >> e;
    int pos[k];
    for (int i = 0; i < k; i++) pos[i] = i + 1;
    if (s != 1) {
        pos[0] ^= pos[s - 1] ^= pos[0] ^= pos[s - 1];
        if (e == 1) e = s;
    }
    if (e != k) pos[k - 1] ^= pos[e - 1] ^= pos[k - 1] ^= pos[e - 1];
    std::cout << 2 * (k - 1) * (k - 1) - 1 << '\n';
    // part 1
    for (int i = 1; i < k - 1; i++) {
        for (int j = k - 1; j >= i; j--) {
            std::cout << pos[0] << ' ' << pos[j] << '\n';
        }
        for (int j = i + 1; j < k; j++) {
            std::cout << pos[j] << ' ' << pos[i] << '\n';
        }
    }
    std::cout << pos[0] << ' ' << pos[k - 1] << '\n';
    // part 2
    for (int i = k - 2; i >= 1; i--) {
        std::cout << pos[i] << ' ' << pos[0] << '\n';
        for (int j = k - 2; j > i; j--) {
            std::cout << pos[i] << ' ' << pos[j] << '\n';
        }
        for (int j = i; j < k - 1; j++) {
            std::cout << pos[j] << ' ' << pos[k - 1] << '\n';
        }
        std::cout << pos[0] << ' ' << pos[k - 1] << '\n';
    }
    return 0;
}
