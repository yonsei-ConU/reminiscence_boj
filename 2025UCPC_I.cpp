#include <iostream>
#include <map>
#include <queue>

int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    int y[N];
    for (auto &i : y) std::cin >> i;
    std::map<std::pair<int, int>, bool> s;
    int last = 0;
    int x = 1;
    for (int v : y) {
        if (v > last) {
            s[{x, v}] = false;
        } else {
            s[{++x, v}] = false;
        }
        last = v;
    }
    int ans = 0;
    for (auto &[key, value] : s) {
        if (value) continue;
        ans++;
        s[key] = true;
        std::queue<std::pair<int, int>> q;
        q.push(key);
        while (!q.empty()) {
            auto cur = q.front(); q.pop();
            int a = cur.first;
            int b = cur.second;
            for (int i = 0; i < 4; i++) {
                int na = a + dy[i];
                int nb = b + dx[i];
                auto it = s.find({na, nb});
                if (it == s.end() || it->second) continue;
                q.push({na, nb});
                it->second = true;
            }
        }
    }
    std::cout << ans << '\n' << N;
    return 0;
}
