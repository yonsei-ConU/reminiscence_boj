#include <iostream>
#include <queue>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    int threshold = (9 * M + 9) / 10;
    std::vector<int> A;
    int freq[1000001] = {0};
    for (int i = 0; i < M; i++) {
        int v;
        std::cin >> v;
        A.push_back(v);
        freq[v]++;
    }
    bool chk = false;
    for (int v : A) {
        if (freq[v] >= threshold) chk = true;
    }
    for (int i = M; i < N; i++) {
        int v;
        std::cin >> v;
        A.push_back(v);
        freq[v]++;
        freq[A[i - M]]--;
        if (freq[v] >= threshold) chk = true;
    }
    if (chk) std::cout << "YES";
    else std::cout << "NO";
    return 0;
}