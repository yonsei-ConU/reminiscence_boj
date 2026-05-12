#include <iostream>
#include <vector>
#include <algorithm>

typedef long long ll;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> A(N);
    ll sum = 0;
    for (auto &i : A) {
        std::cin >> i;
        sum += i;
    }
    std::sort(A.begin(), A.end());
    ll ans = 0;
    for (int val : A) {
        sum -= val;
        ans += val * sum;
    }
    std::cout << ans;
    return 0;
}
