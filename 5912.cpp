#include <iostream>
#include <vector>
#include <algorithm>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, K;
    std::cin >> N >> K;
    std::vector<int> diff(N + 1, 0);
    for (int i = 0; i < K; i++) {
        int A, B;
        std::cin >> A >> B;
        diff[A - 1]++;
        diff[B]--;
    }
    std::vector<int> raw(N, 0);
    raw[0] = diff[0];
    for (int i = 0; i < N; i++) {
        raw[i] = raw[i - 1] + diff[i];
    }
    std::sort(raw.begin(), raw.end());
    std::cout << raw[N / 2];
    return 0;
}
