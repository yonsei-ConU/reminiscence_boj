#include <iostream>
#include <vector>

void dfs(int ys, int ye, int xs, int xe, const std::vector<std::string> &S) {
    int cnt = 0;
    for (int y = ys; y < ye; y++) {
        for (int x = xs; x < xe; x++) {
            cnt += S[y][x] - '0';
        }
    }
    if (cnt == 0) {
        std::cout << 0;
    } else if (cnt == (xe - xs) * (ye - ys)) {
        std::cout << 1;
    } else {
        int xm = (xs + xe) >> 1;
        int ym = (ys + ye) >> 1;
        std::cout << '(';
        dfs(ys, ym, xs, xm, S);
        dfs(ys, ym, xm, xe, S);
        dfs(ym, ye, xs, xm, S);
        dfs(ym, ye, xm, xe, S);
        std::cout << ')';
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<std::string> S(N);
    for (auto &s : S) std::cin >> s;
    dfs(0, N, 0, N, S);
    return 0;
}
