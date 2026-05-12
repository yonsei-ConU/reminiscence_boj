#include <iostream>
#include <vector>
#include <queue>

int dx[8] = {1, 2, 2, 1, -1, -2, -2, -1};
int dy[8] = {2, 1, -1, -2, -2, -1, 1, 2};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int T;
    std::cin >> T;
    while (T--) {
        int l;
        std::cin >> l;
        int sx, sy, ex, ey;
        std::cin >> sx >> sy >> ex >> ey;
        std::vector<std::vector<int>> dist(l, std::vector<int>(l, -1));
        dist[sx][sy] = 0;
        std::queue<std::pair<int, int>> q;
        q.emplace(sx, sy);
        while (!q.empty()) {
            auto [x, y] = q.front(); q.pop();
            for (int i = 0; i < 8; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= l || ny < 0 || ny >= l || dist[nx][ny] != -1) continue;
                dist[nx][ny] = dist[x][y] + 1;
                q.emplace(nx, ny);
            }
        }
        std::cout << dist[ex][ey] << '\n';
    }
    return 0;
}
