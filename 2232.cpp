#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

struct cycle {
    int sum;
    int len;
    int min;
};

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<int> weights(n);
    for (auto &i : weights) {
        std::cin >> i;
    }
    std::vector<int> id(n);
    for (int i = 0; i < n; i++) {
        id[i] = i;
    }
    std::sort(id.begin(), id.end(), [&weights](int a, int b) {return weights[a] < weights[b];});
    std::vector<cycle> cycles;
    cycle least;
    ll ans = 0;
    std::vector<bool> processed(n, false);
    for (int idx = 0; idx < n; idx++) {
        if (processed[idx]) continue;
        cycle cur = {0, 0, 2147483647};
        bool chk = false;
        int i = idx;
        while (!processed[i]) {
            processed[i] = true;
            if (i == 0) {
                chk = true;
            }
            cur.len++;
            cur.sum += weights[i];
            if (weights[i] < cur.min) cur.min = weights[i];
            i = id[i];
        }
        if (chk) {
            least.sum = cur.sum;
            least.min = cur.min;
            least.len = cur.len;
        }
        else cycles.push_back(cur);
        ans += cur.sum + (cur.len - 2) * cur.min;
    }
    for (cycle& cy : cycles) {
        ll delta = least.min * (cy.len + 1) + cy.min * (3 - cy.len);
        if (delta < 0) ans += delta;
    }
    std::cout << ans;
    return 0;
}
