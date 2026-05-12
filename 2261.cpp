#include <iostream>
#include <vector>
#include <algorithm>

inline int dist(const std::pair<int, int> &p1, const std::pair<int, int> &p2) {
    return (p1.first - p2.first) * (p1.first - p2.first) + (p1.second - p2.second) * (p1.second - p2.second);
}

int cpp(int left, int right, const std::vector<std::pair<int, int>> &points) {
    int interval = right - left + 1;
    if (interval <= 4) {
        int ret = 2147483647;
        for (int i = left; i <= right; i++) {
            for (int j = i + 1; j <= right; j++) {
                ret = std::min(ret, dist(points[i], points[j]));
            }
        }
        return ret;
    } else {
        int mid = left + interval / 2;
        int ret = std::min(cpp(left, mid, points), cpp(mid + 1, right, points));
        std::vector<std::pair<int, int>> midpoints;
        int ptr = mid;
        while (ptr <= right && (points[ptr].first - points[mid].first) * (points[ptr].first - points[mid].first) < ret) {
            midpoints.emplace_back(points[ptr].second, points[ptr].first);;
            ptr++;
        }
        ptr = mid - 1;
        while (ptr >= left && (points[mid].first - points[ptr].first) * (points[mid].first - points[ptr].first) < ret) {
            midpoints.emplace_back(points[ptr].second, points[ptr].first);;
            ptr--;
        }
        std::sort(midpoints.begin(), midpoints.end());
        for (int i = 0; i < midpoints.size(); i++) {
            for (int j = i + 1; j < midpoints.size(); j++) {
                if ((midpoints[j].first - midpoints[i].first) * (midpoints[j].first - midpoints[i].first) >= ret) break;
                int d = dist(midpoints[i], midpoints[j]);
                ret = std::min(ret, d);
            }
        }
        return ret;
    }
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<std::pair<int, int>> points(n);
    for (auto &i : points) {
        std::cin >> i.first >> i.second;
    }
    std::sort(points.begin(), points.end());
    std::cout << cpp(0, n - 1, points);
    return 0;
}
