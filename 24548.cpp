#include <iostream>

typedef long long ll;

inline int add(int a, int b) {
    if (a / b % 3 == 2) {
        return a - 2 * b;
    } else {
        return a + b;
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::string road;
    std::cin >> road;
    ll cnt[81] = {1};
    int cur = 0;
    for (int i = 0; i < N; i++) {
        if (road[i] == 'T') {
            cur = add(cur, 1);
        } else if (road[i] == 'G') {
            cur = add(cur, 3);
        } else if (road[i] == 'F') {
            cur = add(cur, 9);
        } else {
            cur = add(cur, 27);
        }
        cnt[cur]++;
    }
    ll ans = 0;
    for (ll &v : cnt) {
        ans += v * (v - 1) / 2;
    }
    std::cout << ans;
    return 0;
}
