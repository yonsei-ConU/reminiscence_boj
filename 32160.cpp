#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    if (N == 2) {
        std::cout << "1\n2 1";
    } else if (N == 3) {
        std::cout << "2\n1 2\n1 3";
    } else if (N & 1) {
        if ((N & 3) == 1) {
            std::cout << N << '\n';
            int o = 0;
            for (int i = 1; i < N; i += 2) {
                std::cout << i << ' ' << i + 1 << '\n';
                o++;
            }
            int z = 0;
            for (int i = o; i >= 2; i -= 2) {
                std::cout << "1 1\n";
                z++;
            }
            for (int i = z; i >= 2; i--) {
                std::cout << "0 0\n";
            }
            std::cout << "0 " << N << '\n';
        } else {
            std::cout << N - 1 << '\n';
            int o = 0;
            for (int i = 1; i < N; i += 2) {
                std::cout << i << ' ' << i + 1 << '\n';
                o++;
            }
            int z = 0;
            for (int i = o; i >= 2; i -= 2) {
                std::cout << "1 1\n";
                z++;
            }
            for (int i = z; i >= 2; i--) {
                std::cout << "0 0\n";
            }
            std::cout << "0 1\n1 " << N << '\n';
        }
    } else {
        if ((N & 3) == 2) {
            std::cout << N - 1 << '\n';
            int o = 1;
            for (int i = 2; i < N; i += 2) {
                std::cout << i << ' ' << i + 1 << '\n';
                o++;
            }
            int z = 0;
            for (int i = o; i >= 2; i -= 2) {
                std::cout << "1 1\n";
                z++;
            }
            for (int i = z; i >= 2; i--) {
                std::cout << "0 0\n";
            }
            std::cout << "0 1\n1 " << N << '\n';
        } else {
            std::cout << N << '\n';
            int o = 1;
            for (int i = 2; i < N; i += 2) {
                std::cout << i << ' ' << i + 1 << '\n';
                o++;
            }
            int z = 0;
            for (int i = o; i >= 2; i -= 2) {
                std::cout << "1 1\n";
                z++;
            }
            for (int i = z; i >= 2; i--) {
                std::cout << "0 0\n";
            }
            std::cout << "0 " << N << '\n';
        }
    }
    return 0;
}