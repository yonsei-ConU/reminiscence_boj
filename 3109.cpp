#include <iostream>
#include <vector>
#include <string>

int R, C;

bool dfs(int depth, int y, int &ans, std::vector<std::string> &bread) {
    bread[y][depth] = 'x';
    if (depth == C - 1) {
        ans++;
        return true;
    } else {
        for (int ny = y - 1; ny <= y + 1; ny++) {
            if (ny == -1 || ny == R || bread[ny][depth + 1] == 'x') continue;
            if (dfs(depth + 1, ny, ans, bread)) {
                return true;
            }
        }
    }
    return false;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::cin >> R >> C;
    std::vector<std::string> bread(R);
    for (auto &i : bread) std::cin >> i;
    int ans = 0;
    for (int i = 0; i < R; i++) {
        dfs(0, i, ans, bread);
    }
    std::cout << ans;
    return 0;
}
