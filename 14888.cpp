#include <iostream>
#include <vector>

int min = 1000000001;
int MAX = -1000000001;
std::vector<int> A;

void evaluate(const std::vector<int> &expr) {
    int last = A[0];
    for (int i = 1; i <= expr.size(); i++) {
        if (expr[i - 1] == 0) {
            last += A[i];
        } else if (expr[i - 1] == 1) {
            last -= A[i];
        } else if (expr[i - 1] == 2) {
            last *= A[i];
        } else {
            last /= A[i];
        }
    }
    if (last < min) min = last;
    if (last > MAX) MAX = last;
}

void dfs(int a, int s, int m, int d, std::vector<int> cur) {
    if (!a && !s && !m && !d) {
        evaluate(cur);
    } else {
        if (a) {
            cur.push_back(0);
            dfs(a - 1, s, m, d, cur);
            cur.pop_back();
        }
        if (s) {
            cur.push_back(1);
            dfs(a, s - 1, m, d, cur);
            cur.pop_back();
        }
        if (m) {
            cur.push_back(2);
            dfs(a, s, m - 1, d, cur);
            cur.pop_back();
        }
        if (d) {
            cur.push_back(3);
            dfs(a, s, m, d - 1, cur);
            cur.pop_back();
        }
    }
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    A.resize(N);
    for (auto &i : A) std::cin >> i;
    int add, subtract, multiply, divide;
    std::cin >> add >> subtract >> multiply >> divide;
    dfs(add, subtract, multiply, divide, std::vector<int>(0));
    std::cout << MAX << '\n' << min;
    return 0;
}
