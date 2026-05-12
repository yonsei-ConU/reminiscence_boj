#include <iostream>
#include <vector>

typedef long long ll;
const ll MOD = 469762049;
const ll ROOT = 3;

inline ll power(ll x, ll exp) {
    ll res = 1;
    x %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (1LL * res * x) % MOD;
        x = (1LL * x * x) % MOD;
        exp >>= 1;
    }
    return res;
}

std::vector<ll> fft(std::vector<ll>& a, bool inverse) {
    int n = a.size();
    int j = 0;
    for(int i = 1; i < n; ++i){
        int bit = n >> 1;
        while(j & bit){
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if(i < j) std::swap(a[i], a[j]);
    }

    for(int len = 2; len <= n; len <<= 1){
        ll omega = power(ROOT, (MOD-1)/len);
        if(inverse) omega = power(omega, MOD-2);
        for(int i = 0; i < n; i += len){
            ll w = 1;
            for(int j = 0; j < len/2; ++j){
                ll u = a[i+j];
                ll v = (1LL * a[i+j+len/2] * w) % MOD;
                a[i+j] = (u + v) % MOD;
                a[i+j+len/2] = (u - v + MOD) % MOD;
                w = (1LL * w * omega) % MOD;
            }
        }
    }

    if(inverse){
        ll inv_n = power(n, MOD-2);
        for(auto &x : a) x = (1LL * x * inv_n) % MOD;
    }
    return a;
}

std::vector<ll> conv(std::vector<ll> a, std::vector<ll> b){
    int n = a.size() + b.size() - 1;
    int size = 1;
    while(size < n) size <<= 1;

    a.resize(size, 0);
    b.resize(size, 0);

    fft(a, false);
    fft(b, false);

    for(int i = 0; i < size; ++i){
        a[i] = (1LL * a[i] * b[i]) % MOD;
    }

    fft(a, true);
    a.resize(n);
    return a;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::vector<ll> up(60001, 0), down(60001, 0);
    int nu;
    std::cin >> nu;
    for (int i = 0; i < nu; i++) {
        int t;
        std::cin >> t;
        up[t + 30000] = 1;
    }
    int nm;
    std::cin >> nm;
    std::vector<int> queries(nm);
    for (auto &i : queries) {
        std::cin >> i;
        i += 30000;
    }
    int nd;
    std::cin >> nd;
    for (int i = 0; i < nd; i++) {
        int t;
        std::cin >> t;
        down[t + 30000] = 1;
    }
    auto prod = conv(up, down);
    ll ans = 0;
    for (int q : queries) {
        ans += prod[2 * q];
    }
    std::cout << ans;
    return 0;
}
