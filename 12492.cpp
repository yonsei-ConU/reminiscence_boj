#include <iostream>
#include <string>

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int T;
    std::cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        int R, C;
        std::cin >> R >> C;
        std::string tiles[R];
        for (int i = 0; i < R; i++) std::cin >> tiles[i];

        bool ok = true;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (tiles[i][j] == '#') {
                    if (i == R - 1 || j == C - 1 || tiles[i + 1][j] != '#' || tiles[i][j + 1] != '#' || tiles[i + 1][j + 1] != '#') {
                        ok = false;
                        break;
                    } else {
                        tiles[i][j] = '/';
                        tiles[i][j + 1] = '\\';
                        tiles[i + 1][j] = '\\';
                        tiles[i + 1][j + 1] = '/';
                    }
                }
            }
        }

        std::cout << "Case #" << tc << ":\n";
        if (ok) {
            for (int i = 0; i < R; i++) std::cout << tiles[i] << '\n';
        } else std::cout << "Impossible\n";
    }

    return 0;
}
