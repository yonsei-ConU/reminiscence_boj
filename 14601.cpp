#include <iostream>
#include <vector>

int num = 1;

void dfs1(int ys, int ye, int xs, int xe, int empty, std::vector<std::vector<int>> &ans) {
    if (ye - ys == 2 && xe - xs == 2) {
        int cnt = 0;
        for (int i = ys; i < ye; i++) {
            for (int j = xs; j < xe; j++) {
                if (ans[i][j] == 0 && empty != cnt) ans[i][j] = num;
                cnt++;
            }
        }
        num++;
        return;
    }
    int y2 = (ys + ye) >> 1;
    int y1 = (ys + y2) >> 1;
    int y3 = (y2 + ye) >> 1;
    int x2 = (xs + xe) >> 1;
    int x1 = (xs + x2) >> 1;
    int x3 = (x2 + xe) >> 1;
    if (empty != 0) dfs1(ys, y2, xs, x2, 3, ans);
    if (empty != 1) dfs1(ys, y2, x2, xe, 2, ans);
    if (empty != 2) dfs1(y2, ye, xs, x2, 1, ans);
    if (empty != 3) dfs1(y2, ye, x2, xe, 0, ans);
    dfs1(y1, y3, x1, x3, empty, ans);
}

void dfs2(int ys, int ye, int xs, int xe, int y, int x, std::vector<std::vector<int>> &ans) {
    if (ye - ys == 2 && xe - xs == 2) {
        for (int i = ys; i < ye; i++) {
            for (int j = xs; j < xe; j++) {
                if (ans[i][j] == 0) ans[i][j] = num;
            }
        }
        num++;
        return;
    }
    int ym = (ys + ye) >> 1;
    int xm = (xs + xe) >> 1;
    if (y < ym) {
        if (x < xm) {
            dfs2(ys, ym, xs, xm, y, x, ans);
            dfs1(ys, ye, xs, xe, 0, ans);
        } else {
            dfs2(ys, ym, xm, xe, y, x, ans);
            dfs1(ys, ye, xs, xe, 1, ans);
        }
    } else {
        if (x < xm) {
            dfs2(ym, ye, xs, xm, y, x, ans);
            dfs1(ys, ye, xs, xe, 2, ans);
        } else {
            dfs2(ym, ye, xm, xe, y, x, ans);
            dfs1(ys, ye, xs, xe, 3, ans);
        }
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int K;
    std::cin >> K;
    int N = 1 << K;
    int x, y;
    std::cin >> x >> y;
    x--;
    y = N - y;
    std::vector<std::vector<int>> ans(N, std::vector<int>(N, 0));
    ans[y][x] = -1;
    dfs2(0, N, 0, N, y, x, ans);
    for (auto &a : ans) {
        for (auto &v : a) {
            std::cout << v << ' ';
        }
        std::cout << '\n';
    }
    return 0;
}
