#include <iostream>
#include <vector>
#include <set>

void dfs(int cur, const std::vector<std::vector<int>> &g, std::vector<std::set<int>> &v, std::vector<int> &mex) {
    for (int nxt : g[cur]) {
        dfs(nxt, g, v, mex);
        mex[cur] = std::max(mex[cur], mex[nxt]);
        if (v[cur].size() < v[nxt].size()) {
            for (int val : v[cur]) {
                if (val == mex[cur]) mex[cur]++;
                v[nxt].insert(val);
            }
            std::swap(v[cur], v[nxt]);
        } else {
            for (int val : v[nxt]) {
                if (val == mex[cur]) mex[cur]++;
                v[cur].insert(val);
            }
        }
        while (v[cur].find(mex[cur]) != v[cur].end()) mex[cur]++;
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<std::vector<int>> g(N);
    int root;
    for (int i = 0; i < N; i++) {
        int t;
        std::cin >> t;
        if (t == -1) {
            root = i;
        } else {
            g[t - 1].push_back(i);
        }
    }
    std::vector<std::set<int>> v(N);
    std::vector<int> mex(N, 0);
    for (int i = 0; i < N; i++) {
        int t;
        std::cin >> t;
        v[i].insert(t);
        if (t == 0) mex[i] = 1;
    }

    dfs(root, g, v, mex);
    for (int val : mex) std::cout << val << '\n';
    return 0;
}
