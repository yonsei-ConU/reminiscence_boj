#include <iostream>
#include <vector>
#include <queue>
#define int long long

int check(int N, std::vector<int> &B, int mid) {
    int ret = 0;
    std::priority_queue<std::pair<int, int>> q;
    for (int i = 0; i < N; i++) {
        q.emplace(-B[i], i);
    }
    std::vector<bool> done(N, false);
    while (!q.empty()) {
        auto [key, cur] = q.top(); q.pop();
        if (done[cur]) continue;
        done[cur] = true;
        for (int nxt : {cur - 1, cur + 1}) {
            if (nxt < 0 || nxt == N || done[nxt]) continue;
            else if (B[nxt] - B[cur] > mid) {
                ret += B[nxt] - B[cur] - mid;
                B[nxt] = B[cur] + mid;
            }
            q.emplace(-B[nxt], nxt);
        }
    }
    return ret;
}

signed main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, T;
    std::cin >> N >> T;
    std::vector<int> A(N);
    for (auto &i : A) std::cin >> i;
    int lo = -1;
    int hi = 0;
    for (int i = 0; i < N - 1; i++) {
        hi = std::max(hi, A[i + 1] - A[i]);
        hi = std::max(hi, A[i] - A[i + 1]);
    }
    hi++;
    while (lo + 1 < hi) {
        int mid = (lo + hi) >> 1;
        std::vector<int> B = A;
        if (check(N, B, mid) <= T) {
            hi = mid;
        } else {
            lo = mid;
        }
    }
    std::vector<int> B = A;
    check(N, B, hi);
    for (int v : B) std::cout << v << ' ';
    return 0;
}
