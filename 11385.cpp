#include <iostream>
#include <vector>
typedef long long ll;

inline ll power(ll x, ll exp, ll MOD) {
    ll res = 1;
    x %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (1LL * res * x) % MOD;
        x = (1LL * x * x) % MOD;
        exp >>= 1;
    }
    return res;
}

std::vector<ll> fft(std::vector<ll>& a, ll MOD, ll ROOT, bool inverse) {
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
        ll omega = power(ROOT, (MOD-1)/len, MOD);
        if(inverse) omega = power(omega, MOD-2, MOD);
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
        ll inv_n = power(n, MOD-2, MOD);
        for(auto &x : a) x = (1LL * x * inv_n) % MOD;
    }
    return a;
}

std::vector<ll> conv(std::vector<ll> a, std::vector<ll> b, ll MOD, ll ROOT){
    int n = a.size() + b.size() - 1;
    int size = 1;
    while(size < n) size <<= 1;

    a.resize(size, 0);
    b.resize(size, 0);

    fft(a, MOD, ROOT, false);
    fft(b, MOD, ROOT, false);

    for(int i = 0; i < size; ++i){
        a[i] = (1LL * a[i] * b[i]) % MOD;
    }

    fft(a, MOD, ROOT, true);
    a.resize(n);
    return a;
}

ll crt(std::vector<ll> mods, std::vector<ll> remainders) {
    __int128 x = 1;
    for (ll m : mods) x *= m;
    __int128 ret = 0;
    for (int i = 0; i < mods.size(); i++) {
        __int128 m = mods[i];
        __int128 r = remainders[i];
        __int128 t = x / m;
        ret += r * t * power(t, m - 2, m);
    }
    return ret % x;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(0);

    int N, M;
    std::cin >> N >> M;
    std::vector<ll> f(N + 1);
    for (int i = 0; i <= N; i++) std::cin >> f[i];
    std::vector<ll> g(M + 1);
    for (int i = 0; i <= M; i++) std::cin >> g[i];

    std::vector<ll> result1 = conv(f, g, 998244353, 3);
    std::vector<ll> result2 = conv(f, g, 2013265921, 31);
    ll ans = 0;
    for (int i = 0; i < result1.size(); i++) {
        ans ^= crt({998244353, 2013265921}, {result1[i], result2[i]});
    }
    std::cout << ans;
    return 0;
}
