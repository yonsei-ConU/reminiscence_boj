#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, K;
    std::cin >> N >> K;
    K++;
    std::vector<int> A(N);
    for (auto &i : A) std::cin >> i;
    std::sort(A.begin(), A.end());
    std::priority_queue<std::vector<int>> pq;
    pq.push({0, 0});

    int last = -1;
    while (K) {
        std::vector<int> vec = pq.top(); pq.pop();
        int val = -vec[0];
        if (val > last) {
            std::cout << val << ": ";
            for (auto it = vec.begin() + 2; it < vec.end(); it++) {
                std::cout << *it << ' ';
            }
            std::cout << '\n';
            K--;
        }
        last = val;

        for (int i = vec[1]; i < N; i++) {
            int t = A[i];
            vec[0] -= t;
            vec[1] = i + 1;
            vec.push_back(t);
            if (pq.size() < K * 10) {
                pq.push(vec);
            }
            vec.pop_back();
            vec[0] += t;
        }
    }
    return 0;
}
