#include <iostream>

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int N, A, B;
    std::cin >> N >> A >> B;
    A = 66 - A;
    B = 130 - B;

    for (;N < 8; N++) {
        int X, Y;
        std::cin >> X >> Y;
        int Z = 0;
        while (A && X) {
            A -= 3;
            B -= 3;
            X--; Z++;
        }
        while (B && Y && Z < 6) {
            B -= 3;
            Y--; Z++;
        }
        if (A <= 0 && B <= 0) {
            std::cout << "Nice";
            return 0;
        }
    }

    std::cout << "Nae ga wae";
    return 0;
}
