#include <vector>
#include <queue>
#include <algorithm>
#include <set>
#include <iostream>

typedef long long ll;

namespace ConU {
    /* 0. 기본 구조체
     * 0-1. Edge
     *  그래프 간선 구조체
     */
    struct Edge {
        int weight;
        int u;
        int v;
        Edge(int start, int end, int cost) : u(start), v(end), weight(cost) {}
        Edge(int start, int end) : u(start), v(end), weight(1) {}
    };

    /* 3. 자료 구조
     * 3-1. UnionFind
     *  분리 집합 구현체
     *  UnionFind(int sz): 크기 sz의 분리 집합 초기화
     *  UnionFind.find(int x): 경로 압축 최적화 적용, x 정점의 루트 노드 반환
     *  UnionFind.unite(int x, int y): x, y 정점을 합침
     * 3-2. segment_tree<T>
     *  비재귀 세그먼트 트리 구현체
     *  연산에 결합법칙이 성립하지 않아도 작동함
     *  segment_tree(arr, identity): 초기값이 arr, 연산 항등원이 identity인 세그먼트 트리 초기화
     *  merge(T a, T b) 함수는 직접 만들어야 함
     *  update(idx, val): idx번 인덱스의 값을 val로 바꿈
     *  query(l, r): l ~ r번을 왼쪽부터 merge한 결과를 리턴
     * 3-4. SegNode<T>
     *  다이나믹, 퍼시스턴트 세그 구현체에 들어갈 노드 구조체
     * 3-5. DynamicSeg<T>
     *  Dynamic Segment Tree 구현체
     *  TODO 설명서 적기
     * 3-6. PersistentSeg<T>
     *  Persistent Segment Tree 구현체
     *  TODO 설명서 적기
     */

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

    template <typename T>
    struct segment_tree {
        // ConU's non-recursive uniform segment tree implementation C++
        int n;
        std::vector<T> tree;
        T identity;

        T merge(T a, T b) {
            return a + b;
        }

        segment_tree(const std::vector<T> &arr, T id) {
            n = 1;
            while (n < arr.size()) n <<= 1;
            identity = id;
            tree.assign(n << 1, identity);
            for (int i = 0; i < arr.size(); i++) {
                tree[n + i] = arr[i];
            }
            for (int i = n - 1; i > 0; i--) {
                tree[i] = merge(tree[2 * i], tree[2 * i + 1]);
            }
        }

        void update(int idx, T val) {
            idx += n;
            tree[idx] = val;
            while (idx > 1) {
                idx >>= 1;
                tree[idx] = merge(tree[idx * 2], tree[idx * 2 + 1]);
            }
        }

        T query(int l, int r) {
            l += n;
            r += n;
            T ret_left = identity;
            T ret_right = identity;
            while (l <= r) {
                if (l & 1) {
                    ret_left = merge(ret_left, tree[l]);
                    l++;
                }
                if (!(r & 1)) {
                    ret_right = merge(tree[r], ret_right);
                    r--;
                }
                l >>= 1;
                r >>= 1;
            }
            return merge(ret_left, ret_right);
        }

        T operator[](int idx) {
            return tree[n + idx];
        }
    };

    template <typename T>
    struct SegNode {
        SegNode *l, *r;
        T val;
        SegNode() : l(nullptr), r(nullptr) {}
        explicit SegNode(T x) : l(nullptr), r(nullptr), val(x) {}
        SegNode(SegNode *left, SegNode *right, T x) : l(left), r(right), val(x) {}
    };

    template <typename T>
    class DynamicSeg {
    public:
        DynamicSeg(int N, T id) : root(new SegNode<T>(id)), n(N), identity(id) {}

        void update(int idx, const T& v) {
            doUpdate(root, 0, n - 1, idx, v);
        }

        T query(int l, int r) {
            return doQuery(root, l, r, 0, n - 1);
        }

    private:
        SegNode<T>* root;
        int n;
        T identity;

        T merge(T a, T b) {
            return a + b;
        }

        void doUpdate(SegNode<T> *cur, int l, int r, int idx, T val) {
            if (l > idx || r < idx) return;
            if (l == r) {
                cur->val = val;
                return;
            }
            int mid = l + ((r - l) >> 1);
            if (idx <= mid) {
                if (!cur->l) cur->l = new SegNode<T>(identity);
                doUpdate(cur->l, l, mid, idx, val);
            } else {
                if (!cur->r) cur->r = new SegNode<T>(identity);
                doUpdate(cur->r, mid + 1, r, idx, val);
            }
            T val_left = cur->l ? cur->l->val : identity;
            T val_right = cur->r ? cur->r->val : identity;
            cur->val = merge(val_left, val_right);
        }

        T doQuery(SegNode<T> *cur, int ql, int qr, int l, int r) {
            if (!cur || ql > r || qr < l) return identity;
            if (l >= ql && r <= qr) return cur->val;
            int mid = l + ((r - l) >> 1);
            return merge(doQuery(cur->l, ql, qr, l, mid), doQuery(cur->r, ql, qr, mid + 1, r));
        }
    };

    template <typename T>
    class PersistentSeg {
    public:
        PersistentSeg(std::vector<T> arr, T id) : n(arr.size()), identity(id) {
            roots.clear();
            roots.push_back(new SegNode<T>);
            build(0, n - 1, roots[0], arr);
        }

        void update(int idx, T val, int time = -1) {
            SegNode<T> *root;
            if (time == -1) root = roots.back();
            else root = roots[time];
            SegNode<T> *new_root = DoUpdate(0, n - 1, root, idx, val);
            roots.push_back(new_root);
        }

        T query(int l, int r, int time) {
            return DoQuery(l, r, 0, n - 1, roots[time]);
        }

        int time() {
            return (int)roots.size() - 1;
        }

    private:
        int n;
        T identity;
        std::vector<SegNode<T>*> roots;

        T merge(T a, T b) {
            return a + b;
        }

        void build(int l, int r, SegNode<T> *cur, const std::vector<T> &arr) {
            if (l == r) {
                cur->val = arr[l];
            } else {
                int mid = l + ((r - l) >> 1);
                cur->l = new SegNode<T>;
                build(l, mid, cur->l, arr);
                cur->r = new SegNode<T>;
                build(mid + 1, r, cur->r, arr);
                cur->val = merge(cur->l->val, cur->r->val);
            }
        }

        SegNode<T> *DoUpdate(int l, int r, SegNode<T> *cur, int idx, T val) {
            if (l == r) return new SegNode<T>(val);
            int mid = l + ((r - l) >> 1);
            if (idx <= mid) {
                auto ret = new SegNode<T>(DoUpdate(l, mid, cur->l, idx, val), cur->r, val);
                ret->val = merge(ret->l->val, ret->r->val);
                return ret;
            } else {
                auto ret = new SegNode<T>(cur->l, DoUpdate(mid + 1, r, cur->r, idx, val), val);
                ret->val = merge(ret->l->val, ret->r->val);
                return ret;
            }
        }

        T DoQuery(int ql, int qr, int l, int r, SegNode<T> *cur) {
            if (qr < l || r < ql) return identity;
            else if (ql <= l && r <= qr) return cur->val;
            else {
                int mid = l + ((r - l) >> 1);
                return merge(DoQuery(ql, qr, l, mid, cur->l), DoQuery(ql, qr, mid + 1, r, cur->r));
            }
        }
    };

    /* 4. DP
     * 4-1. LIS_len(arr)
     *  가장 긴 증가하는 부분 수열 길이를 리턴 O(NlogN)
     * 4-5. LineContainer
     *  O(n log n) CHT를 위한 Line Container
     */

    int LIS_len(const std::vector<int>& arr) {
        std::vector<int> temp;
        temp.emplace_back(-2147483647);

        for (int element : arr) {
            int lo = -1;
            int hi = temp.size();

            // Binary search to find the correct position of element
            while (lo + 1 < hi) {
                int mid = (lo + hi) / 2;
                if (temp[mid] < element) {
                    lo = mid;
                } else {
                    hi = mid;
                }
            }

            if (hi == temp.size()) {
                temp.push_back(element);
            } else {
                temp[hi] = element;
            }
        }

        return temp.size() - 1;  // Exclude the initial -inf
    }

    struct Line {
        mutable ll k, m, p;
        bool operator<(const Line& o) const { return k < o.k; }
        bool operator<(ll x) const { return p < x; }
    };

    struct LineContainer : std::multiset<Line, std::less<>> {
        // (for doubles, use inf = 1/.0, div(a,b) = a/b)
        static const ll inf = 9223372036854775807;
        ll div(ll a, ll b) { // floored division
            return a / b - ((a ^ b) < 0 && a % b); }
        bool isect(iterator x, iterator y) {
            if (y == end()) return x->p = inf, 0;
            if (x->k == y->k) x->p = x->m > y->m ? inf : -inf;
            else x->p = div(y->m - x->m, x->k - y->k);
            return x->p >= y->p;
        }
        void add(ll k, ll m) {
            auto z = insert({k, m, 0}), y = z++, x = y;
            while (isect(y, z)) z = erase(z);
            if (x != begin() && isect(--x, y)) isect(x, y = erase(y));
            while ((y = x) != begin() && (--x)->p >= y->p)
                isect(x, erase(y));
        }
        ll query(ll x) {
            auto l = *lower_bound(x);
            return l.k * x + l.m;
        }
    };

    /*
     * 5. 그래프
     * 5-1. 트리 관련 알고리즘
     * 5-1-1. kruskal(v, edges)
     *  크루스칼 알고리즘 구현체
     *  v개의 정점을 가진 그래프, edges에는 Edge 구조체
     *  유니온 파인드 자료 구조 필요
     * 5-1-5. HLD
     *  heavy-light 분할 구조체
     * 5-2. 최단 경로 알고리즘
     * 5-2-1. dijkstra(g, st)
     *  다익스트라 알고리즘 구현체. g[cur] = {nxt, dist}
     *  시작정점 번호가 st일 때 나머지 모든 정점까지의 최단경로를 리턴
     * 5-2-3. 플로이드 워셜
     *  5-2-3-1. inplace_floyd_warshall(g)
     *   플로이드 워셜 알고리즘 구현체, 리턴값이 없고 매개변수로 넘어온 그래프를 바꿈
     */

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

    template <typename T>
    struct HLD {
        std::vector<std::vector<int>> g;
        int root, N;
        int time = 0;
        std::vector<int> sz, depth, par, disc, esc, top;
        segment_tree<T> st;
        HLD(const std::vector<std::vector<int>> &input_tree, int r, segment_tree<T> &seg):
                root(r), N(input_tree.size()), st(seg) {
            g.resize(N);
            sz.resize(N);
            depth.resize(N);
            par.resize(N);
            disc.resize(N);
            esc.resize(N);
            top.resize(N);
            get_g(input_tree, root, root);
            depth[root] = 0;
            decompose(root);
            hld_ett(root);
        }
        void get_g(const std::vector<std::vector<int>> &h, int cur, int parent) {
            for (int nxt : h[cur]) {
                if (nxt == parent) continue;
                g[cur].push_back(nxt);
                get_g(h, nxt, cur);
            }
        }
        void decompose(int cur) {
            sz[cur] = 1;
            for (int &nxt : g[cur]) {
                depth[nxt] = depth[cur] + 1;
                par[nxt] = cur;
                decompose(nxt);
                sz[cur] += sz[nxt];
                if (sz[nxt] > sz[g[cur][0]]) std::swap(nxt, g[cur][0]);
            }
        }
        void hld_ett(int cur) {
            disc[cur] = time++;
            for (int nxt : g[cur]) {
                top[nxt] = nxt == g[cur][0] ? top[cur] : nxt;
                hld_ett(nxt);
            }
            esc[cur] = time;
        }

        void update(int idx, T val) {
            st.update(disc[idx], val);
        }

        T query(int l, int r) {
            T ret = st.identity;
            while (top[l] ^ top[r]) {
                if (depth[top[l]] < depth[top[r]]) std::swap(l, r);
                ret = st.merge(ret, st.query(disc[top[l]], disc[l]));
                l = par[top[l]];
            }
            if (depth[l] > depth[r]) std::swap(l, r);
            // vertex query: disc[l], edge query: disc[l] + 1
            ret = st.merge(ret, st.query(disc[l] + 1, disc[r]));
            return ret;
        }
    };

    std::vector<int> dijkstra(const std::vector<std::vector<std::pair<int, int>>>& g, int st) {
        int INF = 2147483647;
        int N = g.size();
        std::vector<int> ret(N, INF);
        ret[st] = 0;
        std::priority_queue<std::pair<int, int>> pq;
        pq.emplace(0, st);
        while (!pq.empty()) {
            int dist = -pq.top().first;
            int cur = pq.top().second;
            pq.pop();
            if (dist > ret[cur]) continue;
            for (const auto &edge: g[cur]) {
                int nextnum = edge.first;
                int nextdist = edge.second;
                if (ret[nextnum] <= dist + nextdist) continue;
                ret[nextnum] = dist + nextdist;
                pq.emplace(-ret[nextnum], nextnum);
            }
        }
        return ret;
    }

    void inplace_floyd_warshall(std::vector<std::vector<int>>& g) {
        int n = g.size();
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (i != j) g[i][j] = std::min(g[i][j], g[i][k] + g[k][j]);
                }
            }
        }
    }

    /*
     * 6. 문자열
     * 6-1. knuth_morris_pratt(s1, s2)
     * s1 문자열에서 s2 문자열을 검색
     * s1 문자열에서 s2 문자열의 시작점이 나타나는 인덱스의 리스트를 리턴
     * 중간에 fail함수를 리턴하면 실패함수만 얻을 수 있음
     */
    std::vector<int> knuth_morris_pratt(std::string &s1, std::string &s2) {
        std::vector<int> fail(s2.size(), 0);
        int j = 0;
        for (int i = 1; i < s2.size(); i++) {
            while (j > 0 && s2[i] != s2[j]) j = fail[j - 1];
            if (s2[i] == s2[j]) {
                j++;
                fail[i] = j;
            }
        }
        std::vector<int> ret;
        j = 0;
        for (int i = 0; i < s1.size(); i++) {
            while (j > 0 && s1[i] != s2[j]) j = fail[j - 1];
            if (s1[i] == s2[j]) {
                if (j + 1 == s2.size()) {
                    ret.push_back(i - s2.size() + 2);
                    j = fail[j];
                }
            } else {
                j++;
            }
        }
        return ret;
    }

    /*
     * 7. 기타
     * 7-3. 좌표 압축
     *  7-3-1. inplace_coordinate_compression(N, A)
     *   길이 N과 벡터 A를 받아, A를 좌표압축된 A로 변환
     *  7-3-2. coordinate_compression(N, A)
     *   길이 N과 벡터 A를 받아, 좌표압축된 A를 리턴
     */
    void inplace_coordinate_compression(int N, std::vector<int> &A) {
        std::vector<int> id(N);
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
        std::sort(id.begin(), id.end(), [&](int a, int b) {
            return A[a] < A[b];
        });

        int newX = 0;
        for (int i = 1; i < N; i++) {
            if (A[id[i - 1]] < A[id[i]]) {
                A[id[i - 1]] = newX++;
            } else {
                A[id[i - 1]] = newX;
            }
        }
        A[id[N - 1]] = newX;
    }

    std::vector<int> coordinate_compression(int N, std::vector<int> A) {
        std::vector<int> id(N);
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
        std::sort(id.begin(), id.end(), [&](int a, int b) {
            return A[a] < A[b];
        });

        int newX = 0;
        for (int i = 1; i < N; i++) {
            if (A[id[i - 1]] < A[id[i]]) {
                A[id[i - 1]] = newX++;
            } else {
                A[id[i - 1]] = newX;
            }
        }
        A[id[N - 1]] = newX;
        return A;
    }

    /*
     * 8. CPP 유틸리티 함수
     * 8-1. print2D(any 2D data structure)
     * 들어 있는 모든 값들을 출력
     */
    template<typename T>
    void print2D(T &arr) {
        std::cout << "\n******\n";
        for (auto a : arr) {
            for (auto v : a) {
                std::cout << v << ' ';
            }
            std::cout << '\n';
        }
        std::cout << "******\n";
    }
}
