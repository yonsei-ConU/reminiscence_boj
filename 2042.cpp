#include <iostream>
#include <vector>
#include "algorithms.cpp"
using namespace ConU;

typedef long long ll;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M, K;
    std::cin >> N >> M >> K;
    std::vector<ll> arr(N);
    for (auto &i : arr) std::cin >> i;
    int Q = M + K;
    segment_tree<ll> st(arr, 0LL);

    while (Q--) {
        int a;
        std::cin >> a;
        if (a == 1) {
            int b;
            ll c;
            std::cin >> b >> c;
            st.update(b - 1, c);
        } else {
            int b, c;
            std::cin >> b >> c;
            std::cout << (st.query(b - 1,  c - 1)) << '\n';
        }
    }
}
