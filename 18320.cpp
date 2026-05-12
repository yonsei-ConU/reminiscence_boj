#include <iostream>

typedef long long ll;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    ll N, K, M;
    std::cin >> N >> K >> M;
    ll lo = 0;
    ll hi = 5e11 + 1;
    while (lo + 1 < hi) {
        ll mid = (lo + hi) >> 1;
        ll day = 0;
        ll cur = N;
        while (cur > 0) {
            ll Y = cur / mid;
            if (Y <= M) {
                day += (cur + M - 1) / M;
                break;
            }
            ll d;
            if (Y > (cur - Y) / mid) {
                d = 1;
            } else {
                ll lo2 = 1;
                ll hi2 = K - day + 1;
                while (lo2 + 1 < hi2) {
                    ll mid2 = (lo2 + hi2) >> 1;
                    if (Y > (cur - Y * mid2) / mid) hi2 = mid2;
                    else lo2 = mid2;
                }
                d = hi2;
            }
            day += d;
            cur -= d * Y;
            if (day > K) break;
        }
        if (day <= K) lo = mid;
        else hi = mid;
    }
    std::cout << lo;
    return 0;
}
