#include <iostream>
#include <vector>

typedef long long ll;

ll sum(int N, int root) {
    ll ret = 0;
    ll l = root;
    ll r = root;
    while (true) {
        ret += r * (r + 1) / 2 - l * (l - 1) / 2;
        l *= 2;
        if (l > N) break;
        r *= 2;
        r++;
        if (r > N) r = N;
    }
    return ret;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, Q;
    std::cin >> N >> Q;
    int root = 1;
    while (Q--) {
        int q, v;
        std::cin >> q >> v;
        if (q == 1) {
            root = v;
        } else {
            std::vector<int> trace;
            int cur = root;
            while (cur > 0 && cur != v) {
                trace.push_back(cur);
                cur >>= 1;
            }
            if (v == root) {
                std::cout << sum(N, 1);
            } else if (cur == v && cur != root) { // 서브트리 루트가 원래트리 조상임
                std::cout << sum(N, 1) - sum(N, trace.back());
            } else {
                std::cout << sum(N, v);
            }
            std::cout << '\n';
        }
    }
    return 0;
}
