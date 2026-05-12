#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

struct Edge {
    int u, v;
    ll weight;
};

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

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<Edge> edges(n - 1);
    for (auto &e : edges) {
        std::cin >> e.u >> e.v >> e.weight;
        e.u--; e.v--;
    }
    std::sort(edges.begin(), edges.end(), [](const Edge &a, const Edge &b) {return a.weight > b.weight;});
    UnionFind uf(n);
    ll ans = 0;
    int max_size = 1;
    for (const Edge &e : edges) {
        if (uf.find(e.u) != uf.find(e.v)) {
            uf.unite(e.u, e.v);
            max_size = std::max(max_size, uf.size[uf.find(e.u)]);
            ans = std::max(ans, e.weight * (max_size - 1));
        }
    }
    std::cout << ans;
    return 0;
}
