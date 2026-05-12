#include <iostream>
#include <set>
#include <vector>
#define int long long

signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, L, R;
    std::cin >> N >> L >> R;
    std::string S;
    std::cin >> S;
    std::set<int> Nidx, Cidx;
    for (int i = 0; i < N; i++) {
        if (S[i] == 'N') Nidx.insert(i);
        else if (S[i] == 'C') Cidx.insert(i);
    }
    std::vector<std::vector<int>> intervals;
    for (int n : Nidx) {
        auto it = Cidx.upper_bound(n);
        if (it == Cidx.end()) continue;
        int c = *it;
        auto it2 = Nidx.lower_bound(c);
        it2--;
        if (*it2 != n) continue;
        if ((n + c) & 1 || S[(n + c) / 2] != 'P') continue;
        int v11;
        if (it == Cidx.begin()) v11 = -1;
        else v11 = *(--it);
        int v12;
        it = Nidx.lower_bound(n);
        if (it == Nidx.begin()) v12 = -1;
        else v12 = *(--it);
        int v1 = std::max(v11, v12);
        it = Nidx.upper_bound(c);
        int v21;
        if (it == Nidx.end()) v21 = N;
        else v21 = *it;
        int v22;
        it = Cidx.upper_bound(c);
        if (it == Cidx.end()) v22 = N;
        else v22 = *it;
        int v2 = std::min(v21, v22);
        // 왼쪽빈칸 오른쪽빈칸 가운데고정
        intervals.push_back({n - v1 - 1, v2 - 1 - c, c - n + 1});
    }
    int ans = 0;
    for (auto &v : intervals) {
        // std::cout << v[0] << ' ' << v[1] << ' ' << v[2] << '\n';
        for (int i = 0; i <= v[0]; i++) {
            int j1 = std::max(0, L - v[2] - i);
            int j2 = std::min(v[1], R - v[2] - i);
            if (j1 <= j2) ans += j2 - j1 + 1;
        }
    }
    std::cout << ans;
    return 0;
}
