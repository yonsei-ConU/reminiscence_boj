#include <iostream>
#include <vector>
#include <utility>
#include <algorithm>
#include <bitset>

const int INF = 2000000000;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, d;
    std::cin >> n >> d;
    std::vector<std::pair<int, int>> points(n);
    for (int i = 0; i < n; i++) {
        std::cin >> points[i].first >> points[i].second;
    }
    std::sort(points.begin(), points.end());

    std::bitset<1000000> chk;
    chk.set();
    int global_max = -INF;
    int global_min = INF;
    int local_max = -INF;
    int local_min = INF;
    int cnt = 0;
    bool leftmost = true;
    for (auto ptr = points.begin(); ptr < points.end(); ptr++) {
        if (ptr != points.begin() && (ptr - 1)->first != ptr->first) {
            global_max = std::max(global_max, local_max);
            global_min = std::min(global_min, local_min);
            local_max = -INF;
            local_min = INF;
            leftmost = false;
        }
        if (leftmost || ptr->second <= global_min || ptr->second >= global_max) {
            chk[cnt] = false;
        }
        local_max = std::max(local_max, ptr->second);
        local_min = std::min(local_min, ptr->second);
        cnt++;
    }

    global_max = -INF;
    global_min = INF;
    local_max = -INF;
    local_min = INF;
    cnt = n - 1;
    bool rightmost = true;
    for (auto ptr = points.rbegin(); ptr != points.rend(); ptr++) {
        if (ptr != points.rbegin() && (ptr - 1)->first != ptr->first) {
            global_max = std::max(global_max, local_max);
            global_min = std::min(global_min, local_min);
            local_max = -INF;
            local_min = INF;
            rightmost = false;
        }
        if (rightmost || ptr->second <= global_min || ptr->second >= global_max) {
            chk[cnt] = false;
        }
        local_max = std::max(local_max, ptr->second);
        local_min = std::min(local_min, ptr->second);
        cnt--;
    }
    std::cout << n - 1000000 + chk.count();
    return 0;
}
