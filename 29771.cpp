#include <iostream>
#include <vector>
#include <set>

typedef long long ll;

struct Query {
    int idx, size;
    ll vnum;
    bool operator<(const Query& rhs) const {
        return idx < rhs.idx;
    }
};

void dfs(int cur, const std::vector<std::vector<int>> &g, std::vector<std::set<Query>> &queries, const std::vector<int> &query_size) {
    for (int nxt : g[cur]) {
        dfs(nxt, g, queries, query_size);
    }
    for (int nxt : g[cur]) {
        if (queries[cur].size() < queries[nxt].size()) {
            std::swap(queries[cur], queries[nxt]);
        }
        for (Query query : queries[nxt]) {
            auto it = queries[cur].find(query);
            if (it != queries[cur].end()) {
                Query tmp = *it;
                queries[cur].erase(it);
                tmp.size += query.size;
                tmp.vnum += query.vnum;
                if ()
            }
        }
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<std::vector<int>> g(N);
    std::vector<bool> root_chk(N, true);
    for (int i = 0; i < N - 1; i++) {
        int p, c;
        std::cin >> p >> c;
        g[p].push_back(c);
        root_chk[c] = false;
    }
    int root;
    for (int i = 0; i < N; i++) {
        if (root_chk[i]) {
            root = i;
            break;
        }
    }
    int Q;
    std::cin >> Q;
    std::vector<int> query_size(Q);
    std::vector<std::set<Query>> queries(N);
    for (int i = 0; i < Q; i++) {
        int k;
        std::cin >> k;
        query_size[i] = k;
        for (int j = 0; j < k; j++) {
            int v;
            std::cin >> v;
            queries[v].insert(Query{i, 1, v});
        }
    }
    return 0;
}
