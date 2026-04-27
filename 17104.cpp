#include <iostream>
#include <vector>

const int MOD = 998244353;
const int ROOT = 3;

inline int power(int x, int exp) {
    int res = 1;
    x %= MOD;
    while (exp > 0) {
        if (exp & 1) res = (1LL * res * x) % MOD;
        x = (1LL * x * x) % MOD;
        exp >>= 1;
    }
    return res;
}

std::vector<int> fft(std::vector<int>& a, bool inverse) {
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
        int omega = power(ROOT, (MOD-1)/len);
        if(inverse) omega = power(omega, MOD-2);
        for(int i = 0; i < n; i += len){
            int w = 1;
            for(int j = 0; j < len/2; ++j){
                int u = a[i+j];
                int v = (1LL * a[i+j+len/2] * w) % MOD;
                a[i+j] = (u + v) % MOD;
                a[i+j+len/2] = (u - v + MOD) % MOD;
                w = (1LL * w * omega) % MOD;
            }
        }
    }

    if(inverse){
        int inv_n = power(n, MOD-2);
        for(auto &x : a) x = (1LL * x * inv_n) % MOD;
    }
    return a;
}

std::vector<int> conv(std::vector<int> a, std::vector<int> b){
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

std::vector<int> sieve(int n){
    std::vector<int> is_prime(n+1, 1);
    is_prime[0] = is_prime[1] = 0;
    for(int i = 2; i <= n; ++i){
        if(is_prime[i]){
            for(int j = 2*i; j <= n; j += i){
                is_prime[j] = 0;
            }
        }
    }
    return is_prime;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::vector<int> primes = sieve(1000000);
    std::vector<int> primes2(1000001, 0);
    for(int p = 0; p <= 1000000; ++p){
        if(primes[p]) primes2[p] = 1;
    }
    std::vector<int> res = conv(primes, primes2);

    int T;
    std::cin >> T;
    while(T--){
        int N;
        std::cin >> N;
        int t = res[N] / 2;
        if (primes[N / 2]) t++;
        std::cout << t << '\n';
    }
}
