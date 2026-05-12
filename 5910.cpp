#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<std::pair<int, int>> a, b;
    ll ans = 0;
    for (int i = 0; i < N; i++) {
        int U, D;
        std::cin >> U >> D;
        ans += D;
        if (U > D) {
            a.emplace_back(U, D);
        } else {
            b.emplace_back(U, D);
        }
    }
    std::sort(a.begin(), a.end(), [](const std::pair<int, int> &a, const std::pair<int, int> &b) {
        return a.second > b.second;
    });
    std::sort(b.begin(), b.end());
    ll cur = 0;
    for (auto it = b.begin(); it != a.end();) {
        cur -= it->first;
        if (cur < 0) {
            ans -= cur;
            cur = 0;
        }
        cur += it->second;
        it++;
        if (it == b.end()) it = a.begin();
    }
    std::cout << ans;
    return 0;
}
