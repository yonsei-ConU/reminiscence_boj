#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>

int memo[20][20][20][20];
std::vector<std::string> board;

int dp(int y1, int y2, int x1, int x2) {
    if (y1 > y2 || x1 > x2) {
        return 0;
    } else if (memo[y1][y2][x1][x2] != -1) {
        return memo[y1][y2][x1][x2];
    }
    // 가능한 모든 칸마다 4분할
    std::vector<int> next_state;
    for (int y = y1; y <= y2; y++) {
        for (int x = x1; x <= x2; x++) {
            if (board[y][x] == 'X') continue;
            int nxt = 0;
            int t = dp(y1, y - 1, x1, x - 1);
            nxt ^= t;
            t = dp(y1, y - 1, x + 1, x2);
            nxt ^= t;
            t = dp(y + 1, y2, x1, x - 1);
            nxt ^= t;
            t = dp(y + 1, y2, x + 1, x2);
            nxt ^= t;
            next_state.push_back(nxt);
        }
    }
    std::sort(next_state.begin(), next_state.end());
    int &ret = (memo[y1][y2][x1][x2] = 0);
    for (int nxt : next_state) {
        if (nxt == ret) ret++;
        else if (nxt > ret) break;
    }
    return ret;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int H, W;
    std::cin >> H >> W;

    for (int i = 0; i < H; i++) {
        std::string t;
        std::cin >> t;
        board.push_back(t);
    }
    memset(memo, -1, sizeof(memo));
    int ans = dp(0, H - 1, 0, W - 1);
    if (ans) std::cout << "First";
    else std::cout << "Second";
    return 0;
}
