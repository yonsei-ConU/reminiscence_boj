#include <iostream>
#include <vector>
#include <string>

const int MOD = 998244353;
const int ROOT = 3;

int pow(int x, int exp) {
    int result = 1;
    x = x % MOD;
    while (exp > 0) {
        if (exp % 2 == 1)
            result = (1LL * result * x) % MOD;
        exp = exp >> 1;
        x = (1LL * x * x) % MOD;
    }
    return result;
}

std::vector<int> fft(std::vector<int>& arr, bool inverse) {
    int n = arr.size();
    int j = 0;
    for (int i = 1; i < n; ++i) {
        int bit = n >> 1;
        while (j & bit) {
            j ^= bit;
            bit >>= 1;
        }
        j ^= bit;
        if (i < j) {
            std::swap(arr[i], arr[j]);
        }
    }

    for (int length = 2; length <= n; length <<= 1) {
        int omega = pow(ROOT, (MOD - 1) / length);
        if (inverse) omega = pow(omega, MOD - 2);
        for (int i = 0; i < n; i += length) {
            int w = 1;
            for (int j = 0; j < length / 2; ++j) {
                int u = arr[i + j];
                int v = (1LL * arr[i + j + length / 2] * w) % MOD;
                arr[i + j] = (u + v) % MOD;
                arr[i + j + length / 2] = (u - v + MOD) % MOD;
                w = (1LL * w * omega) % MOD;
            }
        }
    }

    if (inverse) {
        int inv_n = pow(n, MOD - 2);
        for (int i = 0; i < n; ++i) {
            arr[i] = (1LL * arr[i] * inv_n) % MOD;
        }
    }
    return arr;
}

std::vector<int> conv(std::vector<int> a, std::vector<int> b) {
    int n = a.size() + b.size() - 1;
    int size = 1;
    while (size < n) size <<= 1;

    a.resize(size);
    b.resize(size);

    fft(a, false);
    fft(b, false);

    for (int i = 0; i < size; ++i) {
        a[i] = (1LL * a[i] * b[i]) % MOD;
    }

    fft(a, true);
    // a.resize(n);
    return a;
}

int main() {
    std::string A, B;
    std::cin >> A >> B;
    std::vector<int> a(A.size());
    std::vector<int> b(B.size());

    for (int i = 0; i < A.size(); i++) a[i] = A[A.size() - 1 - i] - '0';
    for (int i = 0; i < B.size(); i++) b[i] = B[B.size() - 1 - i] - '0';
    std::vector<int> result = conv(a, b);
    result.resize(result.size() + 1);
    int up = 0;
    for (int i = 0; i < result.size() + 1; i++) {
        result[i] += up;
        up = result[i] / 10;
        result[i] %= 10;
    }

    while (result.size() > 1 && result.back() == 0)
        result.pop_back();

    for (int i = result.size() - 1; i >= 0; i--) {
        std::cout << result[i];
    }
    std::cout << std::endl;
}
