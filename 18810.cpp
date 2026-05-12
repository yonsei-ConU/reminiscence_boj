#include <iostream>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, am, aM, bm, bM;
    std::cin >> n >> am >> aM >> bm >> bM;
    int a = 0, b = 0, extra = 0;
    while (n--) {
        int sushi;
        std::cin >> sushi;
        if (sushi & 1) extra++;
        a += sushi >> 1;
        b += sushi >> 1;
    }
    if (a > aM || b > bM || extra < std::max(0, am - a) + std::max(0, bm - b) || a + b + extra > aM + bM) std::cout << "No";
    else std::cout << "Yes";
    return 0;
}
