#include <iostream>
#include <random>

inline char get_win(char c) {
    if (c == 'R') return 'P';
    else if (c == 'P') return 'S';
    else return 'R';
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::random_device rand;
    std::mt19937 gen(rand());
    int N;
    std::cin >> N;
    std::string cur(N, ' ');
    for (char &c : cur) {
        int r = gen() % 3;
        if (r == 0) c = 'R';
        else if (r == 1) c = 'P';
        else c = 'S';
    }
    bool ok = false;
    for (int i = 0; i < 420; i++) {
        std::cout << "? " << cur << std::endl;
        int wins, drawn, lost;
        std::cin >> wins >> drawn >> lost;
        if (wins == N) {
            ok = true;
            break;
        }
        drawn--; lost--;
        if (drawn != -2) cur[drawn] = get_win(cur[drawn]);
        if (lost != -2) cur[lost] = get_win(get_win(cur[lost]));
    }
    if (ok) {
        std::cout << "! " << cur << std::endl;
        return 0;
    } else {
        return 1;
    }
}