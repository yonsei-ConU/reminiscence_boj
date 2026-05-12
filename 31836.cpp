#include <iostream>
#include <vector>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    std::vector<int> A, B;
    while (N >= 3) {
        A.push_back(N--);
        B.push_back(N--);
        B.push_back(N--);
    }
    if (N == 2) {
        A.push_back(N--);
        B.push_back(N--);
    }
    std::cout << A.size() << '\n';
    for (int &i : A) std::cout << i << ' ';
    std::cout << '\n';
    std::cout << B.size() << '\n';
    for (int &i : B) std::cout << i << ' ';
    std::cout << '\n';
    return 0;
}
