#include <iostream>
#include <vector>

int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<std::string> city(N);
    for (int i = 0; i < N; i++) std::cin >> city[i];
    std::vector<std::vector<bool>> B(N, std::vector<bool>(N, true));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (city[i][j] != 'O') continue;
            for (int k = 0; k < 4; k++) {
                int y = i;
                int x = j;
                while (true) {
                    int ny = y + dy[k];
                    int nx = x + dx[k];
                    if (ny < 0 || ny >= N || nx < 0 || nx >= N || city[ny][nx] != '.') break;
                    B[ny][nx] = false;
                    y = ny; x = nx;
                }
            }
        }
    }
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (city[i][j] == '.' && B[i][j]) std::cout << 'B';
            else std::cout << city[i][j];
        }
        std::cout << '\n';
    }
    return 0;
}