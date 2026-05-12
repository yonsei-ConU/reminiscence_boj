#include <iostream>

const int MX = 5000001;
int lpf[MX] = {0};

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    for (int i = 2; i < MX; i++) {
        if (lpf[i] == 0) {
            for (int j = i; j < MX; j += i) {
                if (lpf[j] == 0) {
                    lpf[j] = i;
                }
            }
        }
    }
    int N;
    std::cin >> N;
    while (N--) {
        int k;
        std::cin >> k;
        while (k > 1) {
            int t = lpf[k];
            std::cout << t << ' ';
            k /= t;
        }
        std::cout << '\n';
    }
    return 0;
}
