#include <iostream>
#include <set>
#include <vector>

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int N, K;
    std::cin >> N >> K;
    std::set<int> sensors;
    for (int i = 0; i < N; i++) {
        int t;
        std::cin >> t;
        sensors.insert(t);
    }
    K--;
    int last = *sensors.begin();
    std::vector<int> diff;
    for (int v : sensors) {
        diff.emplace_back(v - last);
        last = v;
    }
    std::sort(diff.begin(), diff.end(), [&](int a, int b) {return a > b;});
    int ans = 0;
    for (int i = K; i < diff.size(); i++) ans += diff[i];
    std::cout << ans;
    return 0;
}
