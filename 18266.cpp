#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

typedef long long ll;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, L;
    int weight_sum = 0;
    std::cin >> N >> L;
    std::vector<std::vector<int>> data;
    for (int i = 0; i < N; i++) {
        int w, x, d;
        std::cin >> w >> x >> d;
        data.push_back({x, w, d});
        weight_sum += w;
    }
    std::sort(data.begin(), data.end());
    std::deque<int> cow_order;
    std::vector<std::pair<int, int>> fall_order;
    std::vector<ll> left, right;
    for (int i = 0; i < N; i++) {
        auto &vec = data[i];
        cow_order.push_back(vec[1]);
        if (vec[2] == 1) {
            fall_order.emplace_back(L - vec[0], vec[1] * vec[2]);
            right.push_back(vec[0]);
        } else {
            fall_order.emplace_back(vec[0], vec[1] * vec[2]);
            left.push_back(vec[0]);
        }
    }
    std::sort(fall_order.begin(), fall_order.end());
    int ptr = 0;
    int cur_weight_sum = 0;
    int time = 0;
    while (ptr < N && cur_weight_sum * 2 < weight_sum) {
        time = fall_order[ptr].first;
        if (ptr != N - 1 && fall_order[ptr].first == fall_order[ptr + 1].first) {
            cur_weight_sum += cow_order.front(); cow_order.pop_front();
            cur_weight_sum += cow_order.back(); cow_order.pop_back();
            ptr += 2;
        } else if (fall_order[ptr].second > 0) {
            cur_weight_sum += cow_order.back(); cow_order.pop_back();
            ptr++;
        } else {
            cur_weight_sum += cow_order.front(); cow_order.pop_front();
            ptr++;
        }
    }
    int meeting = 0;
    for (ll v : right) {
        auto it1 = std::upper_bound(left.begin(), left.end(), v);
        auto it2 = std::upper_bound(left.begin(), left.end(), v + 2 * time);
        meeting += it2 - it1;
    }
    std::cout << meeting;
    return 0;
}
