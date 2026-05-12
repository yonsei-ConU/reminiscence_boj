#include <iostream>
#include <vector>

int ans = 0;
int dy[] = {1, -1, 0, 0};
int dx[] = {0, 0, 1, -1};

void dfs(int y1, int x1, int y2, int x2, std::vector<std::vector<int>> &apple, int cnt) {
    for (int i = 0; i < 4; i++) {
        int ny1 = y1 + dy[i];
        int nx1 = x1 + dx[i];
        if (ny1 < 0 || ny1 >= 5 || nx1 < 0 || nx1 >= 5 || apple[ny1][nx1] == 0) continue;
        for (int j = 0; j < 4; j++) {
            int ny2 = y2 + dy[j];
            int nx2 = x2 + dx[j];
            if (ny2 < 0 || ny2 >= 5 || nx2 < 0 || nx2 >= 5 || apple[ny2][nx2] == 0) continue;
            if (cnt == 1) {
                if (ny1 == ny2 && nx1 == nx2) {
                    ans++;
                } else {
                    continue;
                }
            } else if (ny1 == ny2 && nx1 == nx2) {
                continue;
            } else {
                apple[ny1][nx1] = 0;
                apple[ny2][nx2] = 0;
                dfs(ny1, nx1, ny2, nx2, apple, cnt - 2);
                apple[ny1][nx1] = 1;
                apple[ny2][nx2] = 1;
            }
        }
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::vector<std::vector<int>> apple(5, std::vector<int>(5, 1));
    apple[0][0] = 0;
    apple[4][4] = 0;
    int K;
    std::cin >> K;
    int cnt = 25 - K;
    while (K--) {
        int y, x;
        std::cin >> y >> x;
        apple[y - 1][x - 1] = 0;
    }
    dfs(0, 0, 4, 4, apple, cnt - 2);
    std::cout << ans;
    return 0;
}
