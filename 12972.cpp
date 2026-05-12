#include <iostream>
#include <map>
#include <vector>

int gcd(int a, int b) {
    return (b == 0) ? a : gcd(b, a % b);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::map<int, int> gcd_table;
    for (int i = 0; i < N * N; i++) {
        int t;
        std::cin >> t;
        gcd_table[t]++;
    }
    std::vector<int> ans;
    while (N--) {
        int mx = 0;
        for (auto p : gcd_table) {
            if (p.second > 0 && p.first > mx) mx = p.first;
        }
        gcd_table[mx]--;
        ans.push_back(mx);
        for (int val : ans) {
            gcd_table[gcd(val, mx)] -= 2;
        }
    }

    for (int val : ans) std::cout << val << ' ';
    return 0;
}
