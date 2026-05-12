#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> b(N - 1);
    for (auto &i : b) std::cin >> i;
    for (int a0 = 1; a0 <= N; a0++) {
        std::vector<int> a = {a0};
        std::vector<bool> chk(N + 1, false);
        chk[a0] = true;
        chk[0] = true;
        bool ok = true;
        for (int i = 0; i < N - 1; i++) {
            int nxt = b[i] - a.back();
            if (nxt < 0 || nxt > N || chk[nxt]) {
                ok = false;
                break;
            }
            a.push_back(nxt);
            chk[nxt] = true;
        }
        if (ok) {
            for (int v : a) {
                std::cout << v << ' ';
            }
            return 0;
        }
    }
    return 1;
}
