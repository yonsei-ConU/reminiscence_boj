#include <iostream>
#include <vector>

int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};

inline int abs(int x) {
    return x < 0 ? -x : x;
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int h, w;
    std::cin >> h >> w;
    int a[h][w];
    memset(a, 0, sizeof(a));
    for (auto &vec : a) {
        for (auto &v : vec) std::cin >> v;
    }
    int ans[h][w];
    memset(ans, -1, sizeof(ans));
    for (int si = 0; si < h; si++) {
        for (int sj = 0; sj < w; sj++) {
            for (int ei = 0; ei < h; ei++) {
                for (int ej = 0; ej < w; ej++) {
                    if (si == ei && sj == ej) continue;
                    int ev = a[ei][ej];
                    int dist[h][w];
                    memset(dist, -1, sizeof(dist));
                    dist[si][sj] = 0;
                    int y = si;
                    int x = sj;
                    while (true) {
                        if (y == ei && x == ej) break;
                        int min_idx = -1;
                        std::pair<int, int> min_val = {1000000000, 0};
                        for (int i = 0; i < 4; i++) {
                            int ny = y + dy[i];
                            int nx = x + dx[i];
                            if (ny < 0 || ny >= h || nx < 0 || nx >= w) continue;
                            if (abs(a[ny][nx] - ev) < min_val.first or (abs(a[ny][nx] - ev) == min_val.first and abs(a[ny][nx] - a[y][x]) < min_val.second)) {
                                min_idx = i;
                                min_val = {abs(a[ny][nx] - ev), abs(a[ny][nx] - a[y][x])};
                            }
                        }
                        int ny = y + dy[min_idx];
                        int nx = x + dx[min_idx];
                        if (min_idx == -1 or dist[ny][nx] != -1) break;
                        dist[ny][nx] = dist[y][x] + 1;
                        y = ny;
                        x = nx;
                    }
                    if (dist[ei][ej] != -1) ans[si][sj] = std::max(ans[si][sj], dist[ei][ej]);
                    else ans[si][sj] = 1000000000;
                }
            }
        }
    }
    int ans_idx = -1;
    int ans_val = 1000000000;
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            if (ans[i][j] != -1 && ans[i][j] < ans_val) {
                ans_idx = a[i][j];
                ans_val = ans[i][j];
            }
        }
    }
    if (ans_idx == -1) {
        std::cout << "impossible";
    } else {
        std::cout << ans_idx << ' '  << ans_val;
    }
    return 0;
}
