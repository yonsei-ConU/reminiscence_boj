#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

int R, C, T;
int dy[] = {0, 0, 1, -1};
int dx[] = {1, -1, 0, 0};

int dfs(int y, int x, int score, int depth, std::vector<std::string>& g) {
    if (depth == T) return score;
    int ret = 0;
    for (int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if (ny < 0 || ny >= R || nx < 0 || nx >= C || g[ny][nx] == '#') continue;
        if (g[ny][nx] == 'S') {
            g[ny][nx] = '.';
            ret = std::max(ret, dfs(ny, nx, score + 1, depth + 1, g));
            g[ny][nx] = 'S';
        } else ret = std::max(ret, dfs(ny, nx, score, depth + 1, g));
    }
    return ret;
}

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    std::cin >> R >> C >> T;
    std::vector<std::string> g(R);
    int y, x;
    for (int i = 0; i < R; i++) {
        std::cin >> g[i];
        for (int j = 0; j < C; j++) {
            if (g[i][j] == 'G') y = i, x = j;
        }
    }

    std::cout << dfs(y, x, 0, 0, g);
    return 0;
}
