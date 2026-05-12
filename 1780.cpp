#include <iostream>
#include <vector>

int NEG = 0;
int ZERO = 0;
int ONE = 0;

void dfs(int ys, int ye, int xs, int xe, const std::vector<std::vector<int>> &S) {
    int neg = 0;
    int zero = 0;
    int one = 0;
    for (int y = ys; y < ye; y++) {
        for (int x = xs; x < xe; x++) {
            if (S[y][x] == -1) neg++;
            else if (!S[y][x]) zero++;
            else one++;
        }
    }
    int tot = (xe - xs) * (ye - ys);
    if (neg == tot) NEG++;
    else if (zero == tot) ZERO++;
    else if (one == tot) ONE++;
    else {
        int xm1 = (2 * xs + xe) / 3;
        int xm2 = (xs + 2 * xe) / 3;
        int ym1 = (2 * ys + ye) / 3;
        int ym2 = (ys + 2 * ye) / 3;
        dfs(ys, ym1, xs, xm1, S);
        dfs(ys, ym1, xm1, xm2, S);
        dfs(ys, ym1, xm2, xe, S);
        dfs(ym1, ym2, xs, xm1, S);
        dfs(ym1, ym2, xm1, xm2, S);
        dfs(ym1, ym2, xm2, xe, S);
        dfs(ym2, ye, xs, xm1, S);
        dfs(ym2, ye, xm1, xm2, S);
        dfs(ym2, ye, xm2, xe, S);
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<std::vector<int>> S(N, std::vector<int>(N));
    for (auto &s : S) {
        for (auto &i : s) std::cin >> i;
    }
    dfs(0, N, 0, N, S);
    std::cout << NEG << '\n' << ZERO << '\n' << ONE;
    return 0;
}
