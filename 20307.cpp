#include <iostream>
#include <numeric>
#include <vector>
#include <string>

typedef long long ll;

struct frac {
    ll numerator;
    ll denominator;

    frac(ll num, ll den = 1) {
        if(den < 0){
            num = -num;
            den = -den;
        }
        ll g = std::gcd(num, den);
        if(g == 0) {
            numerator = 0;
            denominator = 1;
        } else {
            numerator = num / g;
            denominator = den / g;
        }
    }
    frac() : numerator(0), denominator(1) {}
    frac operator+(ll other) const {
        return *this + frac(other);
    }
    frac operator+(frac other) const {
        ll new_num = this->numerator * other.denominator + this->denominator * other.numerator;
        ll new_den = this->denominator * other.denominator;
        ll g = std::gcd(new_num, new_den);
        return {new_num / g, new_den / g};
    }
    frac operator-(ll other) const {
        return *this - frac(other);
    }
    frac operator-(frac other) const {
        return *this + frac(-other.numerator, other.denominator);
    }
    frac operator*(ll other) const {
        return *this * frac(other);
    }
    frac operator*(frac other) const {
        ll new_num = this->numerator * other.numerator;
        ll new_den = this->denominator * other.denominator;
        ll g = std::gcd(new_num, new_den);
        return {new_num / g, new_den / g};
    }
    frac operator/(ll other) const {
        return *this / frac(other);
    }
    frac operator/(frac other) const {
        return *this * frac(other.denominator, other.numerator);
    }
    bool operator==(ll other) const {
        return this->denominator == 1 && this->numerator == other;
    }
    bool operator==(int other) const {
        return this->denominator == 1 && this->numerator == other;
    }
    bool operator!=(ll other) const {
        return !(*this == other);
    }
    bool operator!=(int other) const {
        return !(*this == other);
    }
    frac& operator=(frac other) {
        this->numerator = other.numerator;
        this->denominator = other.denominator;
        return *this;
    }
    frac& operator+=(frac other) {
        *this = *this + other;
        return *this;
    }
    frac& operator-=(frac other) {
        *this = *this - other;
        return *this;
    }
    frac& operator*=(frac other) {
        *this = *this * other;
        return *this;
    }
    frac& operator/=(frac other) {
        *this = *this / other;
        return *this;
    }
};

std::vector<std::vector<frac>> gaussian(std::vector<std::vector<frac>> eq) {
    int N = eq.size();
    int M = eq[0].size();
    int nonzero_col = -1;
    int pivot_row = 0;
    while (pivot_row < N) {
        bool ok = false;
        int nonzero_row = -1;
        for (int col = nonzero_col + 1; col < M; col++) {
            for (int row = pivot_row; row < N; row++) {
                if (eq[row][col] != 0) {
                    ok = true;
                    nonzero_col = col;
                    nonzero_row = row;
                    break;
                }
            }
            if (ok) break;
        }
        if (!ok) break;
        std::swap(eq[pivot_row], eq[nonzero_row]);
        frac a = eq[pivot_row][nonzero_col];
        if (a != 1) {
            for (auto &i: eq[pivot_row]) {
                i /= a;
            }
        }
        for (int row = pivot_row + 1; row < N; row++) {
            frac b = eq[row][nonzero_col];
            for (int col = 0; col < M; col++) {
                eq[row][col] -= b * eq[pivot_row][col];
            }
        }
        pivot_row++;
    }
    for (int row = N - 1; row >= 0; row--) {
        int pivot_col = -1;
        for (int col = 0; col < M - 1; col++) {
            if (eq[row][col] != 0) {
                pivot_col = col;
                break;
            }
        }
        if (pivot_col == -1) continue;
        for (int k = 0; k < row; k++) {
            frac a = eq[k][pivot_col];
            for (int col = 0; col < M; col++) {
                eq[k][col] -= a * eq[row][col];
            }
        }
    }
    return eq;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, M;
    std::cin >> N >> M;
    std::vector<std::vector<frac>> eq(N, std::vector<frac>(M, 0));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            std::string s;
            std::cin >> s;
            int find = -1;
            for (int idx = 0; idx < s.size(); idx++) {
                if (s[idx] == '/') {
                    find = idx;
                    break;
                }
            }
            frac x;
            if (find == -1) {
                x = std::stoi(s);
            } else {
                ll n = std::stoi(s.substr(0, find));
                ll d = std::stoi(s.substr(find + 1));
                x = frac(n, d);
            }
            eq[i][j] = x;
        }
    }
    std::vector<std::vector<frac>> res = gaussian(eq);
    for (auto &i : res) {
        for (auto &j : i) {
            if (j.denominator == 1) {
                std::cout << j.numerator << ' ';
            }
            else {
                std::cout << j.numerator << '/' << j.denominator << ' ';
            }
        }
        std::cout << std::endl;
    }
    return 0;
}
