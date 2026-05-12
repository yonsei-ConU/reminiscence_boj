#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

int N, start, finish;

int dfs(int depth, std::string& cur, int cnt, const std::vector<std::string>& sets) {
    if (depth == N) {
        cnt++;
        if (start <= cnt && cnt <= finish) std::cout << cur << '\n';
        else if (cnt > finish) exit(0);
    } else {
        for (char c : sets[depth]) {
            if (cur.find(c) != std::string::npos) continue;
            cur += c;
            cnt = dfs(depth + 1, cur, cnt, sets);
            cur.pop_back();
        }
    }
    return cnt;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::cin >> N >> start >> finish;
    std::vector<std::string> sets(N);
    for (int i = 0; i < N; i++) std::cin >> sets[i];
    std::string cur;
    dfs(0, cur, 0, sets);
    return 0;
}
