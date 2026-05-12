#include <iostream>
#include <queue>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int Q;
    std::cin >> Q;
    while (Q--) {
        int Ta, Tb, Va, Vb;
        std::cin >> Ta >> Tb >> Va >> Vb;
        int A = 0;
        int B = 0;
        while (Vb) {
            B += Tb;
            Vb--;
        }
        while (Va) {
            if (A < B) A += Ta;
            else B += Ta;
            Va--;
        }
        std::cout << std::max(A, B) << '\n';
    }
    return 0;
}
