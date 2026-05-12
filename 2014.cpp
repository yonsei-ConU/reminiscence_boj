#include <iostream>
#include <vector>
#include <queue>

typedef long long ll;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int K, N;
    std::cin >> K >> N;
    std::vector<int> primes(K);
    for (auto &i : primes) std::cin >> i;
    std::priority_queue<std::pair<ll, int>> pq;
    for (int i = 0; i < K; i++) {
        pq.emplace(-primes[i], i);
    }
    N--;
    while (N--) {
        std::pair<ll, int> p = pq.top();
        pq.pop();
        for (int idx = p.second; idx < K; idx++) {
            if (-p.first * primes[idx] <= 2147483647LL && pq.size() <= N * 10) {
                pq.emplace(p.first * primes[idx], idx);
            }
        }
    }
    std::cout << -pq.top().first;
    return 0;
}
