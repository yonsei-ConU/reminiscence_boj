#include <iostream>
#include <vector>
#include <array>

int dy[4] = {1, -1, 0, 0};
int dx[4] = {0, 0, 1, -1};
int n, m, q;
std::vector<std::pair<int, int>> heights[1000000];

struct UnionFind {
    std::vector<int> parent;
    std::vector<int> size;

    explicit UnionFind(int sz) {
        parent.resize(sz);
        size.resize(sz);
        for (int i = 0; i < sz; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    int find(int x) {
        if (parent[x] == x) return x;
        return parent[x] = find(parent[x]);
    }

    void unite(int x, int y) {
        int root_x = find(x);
        int root_y = find(y);
        if (root_x == root_y) return;
        if (size[root_x] < size[root_y]) parent[root_x] = root_y, size[root_y] += size[root_x];
        else parent[root_y] = root_x, size[root_x] += size[root_y];
    }
};

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    // xm + y coordinate!!!
    std::cin >> n >> m >> q;
    std::vector<std::vector<int>> mountain(n, std::vector<int>(m));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            std::cin >> mountain[i][j];
            mountain[i][j]--;
            heights[mountain[i][j]].emplace_back(i, j);
        }
    }
    int ans[q];
    int done = 0;
    std::vector<std::vector<std::array<int, 3>>> queries(1);
    for (int i = 0; i < q; i++) {
        int a1, b1, a2, b2;
        std::cin >> a1 >> b1 >> a2 >> b2;
        a1--;b1--;a2--;b2--;
        if (a1 == a2 && b1 == b2) {
            done++;
            ans[i] = mountain[a1][b1];
        } else {
            queries[0].push_back({a1 * m + b1, a2 * m + b2, i});
        }
    }
    std::vector<int> lo = {-1};
    std::vector<int> hi = {1000000};
    // make only one union find in each iteration
    while (done < q) {
        std::vector<int> mids(lo.size());
        for (int i = 0; i < lo.size(); i++) {
            // process the case when lo + 1 == hi here
            // in this case, the answers of the queries are already determined
            if (lo[i] + 1 == hi[i]) {
                for (const auto &query : queries[i]) {
                    done++;
                    ans[query[2]] = hi[i];
                }
                mids[i] = -1;
            } else {
                mids[i] = (lo[i] + hi[i]) >> 1;
            }
        }
        UnionFind uf(n * m);
        int cur_merged = 0;
        int ptr = 0;
        std::vector<int> next_lo, next_hi;
        std::vector<std::vector<std::array<int, 3>>> next_queries(mids.size() * 2);
        for (int i = 0; i < mids.size(); i++) {
            // calculate all 'mid' values in the current iteration
            int mid = mids[i];
            if (mid == -1 || queries[i].empty()) continue;
            next_lo.push_back(lo[i]);
            next_lo.push_back(mid);
            next_hi.push_back(mid);
            next_hi.push_back(hi[i]);
            for (;cur_merged <= mid; cur_merged++) {
                for (auto &[y, x] : heights[cur_merged]) {
                    for (int j = 0; j < 4; j++) {
                        int ny = y + dy[j];
                        int nx = x + dx[j];
                        if (ny < 0 || ny >= n || nx < 0 || nx >= m || mountain[ny][nx] > mountain[y][x]) continue;
                        uf.unite(y * m + x, ny * m + nx);
                    }
                }
            }
            for (const auto &query : queries[i]) {
                if (uf.find(query[0]) == uf.find(query[1])) {
                    // (lo, mid)
                    next_queries[ptr].push_back(query);
                } else {
                    // (mid, hi)
                    next_queries[ptr + 1].push_back(query);
                }
            }
            ptr += 2;
        }
        std::swap(lo, next_lo);
        std::swap(hi, next_hi);
        std::swap(queries, next_queries);
    }

    for (int a : ans) {
        std::cout << a + 1 << '\n';
    }
    return 0;
}
