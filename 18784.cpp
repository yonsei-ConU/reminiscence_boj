#include <iostream>
#include <algorithm>
#include <vector>

typedef long long ll;

const ll MOD = 1000000007;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::pair<int, int> points[N];
    for (auto &i : points) {
        std::cin >> i.first >> i.second;
        i.first += 10000;
        i.second += 10000;
    }
    std::sort(points, points + N);
    int right[20001] = {0};
    int left[20001] = {0};
    ll val[20001] = {0};
    int lastX[20001] = {0};
    for (auto &[x, y] : points) {
        right[y]++;
        val[y] += x;
    }
    std::vector<int> to_update = {points[0].second};
    int real_lastX = points[0].first;
    ll ans = 0;
    for (int i = 1; i <= N; i++) {
        if (i ^ N && points[i].first == real_lastX) {
            to_update.push_back(points[i].second);
            continue;
        }
        ll x = points[i - 1].first;
        for (auto &y : to_update) {
            val[y] -= right[y] * (x - lastX[y]);
            val[y] += left[y] * (x - lastX[y]);
            right[y]--;
            left[y]++;
            lastX[y] = (int)x;
        }
        int lastY = 0;
        ll v = 0;
        for (auto &y : to_update) v += y;
        int sz = to_update.size();
        for (int j = 0; j < sz; j++) {
            v -= (0LL + sz - j) * (to_update[j] - lastY);
            v += (0LL + j) * (to_update[j] - lastY);
            lastY = to_update[j];
            ans += val[lastY] * v;
            ans %= MOD;
        }
        if (i ^ N) {
            to_update = {points[i].second};
            real_lastX = points[i].first;
        }
    }
    std::cout << ans;
    return 0;
}
