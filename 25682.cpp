#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M, K;
    std::cin >> N >> M >> K;
    std::string board[N];
    for (auto &i : board) std::cin >> i;
    std::string bw = "BW";
    int raw[N][M];
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int x = (i + j) & 1;
            raw[i][j] = (int)(bw[x] == board[i][j]);
        }
    }
    int psum2D[N + 1][M + 1];
    for (int i = 0; i < N; i++) psum2D[i][0] = 0;
    for (int i = 0; i < M; i++) psum2D[0][i] = 0;
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            psum2D[i][j] = psum2D[i - 1][j] + psum2D[i][j - 1] - psum2D[i - 1][j - 1] + raw[i - 1][j - 1];
        }
    }
    int min = 999999999;
    int max = -999999999;
    for (int i = 0; i + K <= N; i++) {
        for (int j = 0; j + K <= M; j++) {
            int cur = psum2D[i + K][j + K] - psum2D[i][j + K] - psum2D[i + K][j] + psum2D[i][j];
            min = std::min(cur, min);
            max = std::max(cur, max);
        }
    }
    std::cout << std::min(min, K * K - max);
    return 0;
}
