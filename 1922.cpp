#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>

struct Edge {
    int weight;
    int u;
    int v;
    Edge(int start, int end, int cost) : u(start), v(end), weight(cost) {}
};

struct UnionFind {
    int size;
    std::vector<int> parent;
    std::vector<int> rank;

    explicit UnionFind(int sz) {
        size = sz;
        parent.resize(sz);
        rank.resize(sz);
        for (int i = 0; i < sz; i++) {
            parent[i] = i;
            rank[i] = 0;
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
        if (rank[root_x] < rank[root_y]) parent[root_x] = root_y;
        else if (rank[root_x] > rank[root_y]) parent[root_y] = root_x;
        else {
            parent[root_y] = root_x;
            rank[root_x]++;
        }
    }
};

int kruskal(int v, std::vector<Edge>& edges) {
    UnionFind uf(v);
    std::sort(edges.begin(), edges.end(), [](const Edge& a, const Edge& b) { return a.weight < b.weight; });
    int mst_weight = 0;
    std::vector<Edge> mst;
    for (const Edge& e : edges) {
        if (uf.find(e.u) != uf.find(e.v)) {
            uf.unite(e.u, e.v);
            mst.push_back(e);
            mst_weight += e.weight;
        }
        if (mst.size() == v - 1) break;
    }
    return mst_weight;
}

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int N, M;
    std::cin >> N >> M;

    std::vector<Edge> edges;
    for (int i = 0; i < M; i++) {
        int a, b, c;
        std::cin >> a >> b >> c;
        a--;b--;
        if (a == b) continue;
        edges.emplace_back(a, b, c);
    }

    std::cout << kruskal(N, edges);
    return 0;
}
