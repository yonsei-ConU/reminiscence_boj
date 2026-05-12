#include <iostream>
#include <algorithm>
#include <vector>

typedef long long ll;

inline ll weekday(ll d) {
    if (d <= 0) return 0;
    ll weeks = d / 7;
    ll rem = d % 7;
    return weeks * 5 + std::min(rem, 5LL);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<std::pair<int, int>> work(N);
    for (auto &p : work) std::cin >> p.first >> p.second;
    std::sort(work.begin(), work.end());
    ll remain = 0, cur_day = 0, ans = 0, normal_work = 0, extra_work = 0;
    for (auto &[d, t] : work) {
        remain += t;
        normal_work += weekday(d) - weekday(cur_day);
        extra_work += d - cur_day;
        if (normal_work >= remain) {
            normal_work -= remain;
            remain = 0;
        } else if (normal_work + extra_work >= remain) {
            remain -= normal_work;
            normal_work = 0;
            ans += remain;
            extra_work -= remain;
            remain = 0;
        } else {
            std::cout << -1;
            return 0;
        }
        cur_day = d;
    }
    std::cout << ans;
    return 0;
}
