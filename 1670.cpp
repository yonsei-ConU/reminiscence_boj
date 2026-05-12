#include <iostream>
typedef long long ll;
const int mod = 987654321;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    N >>= 1;
    int catalan[N + 1];
    catalan[0] = 1;
    for (int i = 1; i <= N; i++) {
        int tmp = 0;
        for (int j = 0; j < i; j++) {
            ll tmp2 = (ll) catalan[j] * catalan[i - j - 1];
            int delta = tmp2 % mod;
            tmp += delta;
            while (tmp >= mod) tmp -= mod;
        }
        catalan[i] = tmp;
    }
    std::cout << catalan[N];
    return 0;
}
