#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    std::vector<int> a(n);
    std::vector<int> pos(n);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
        pos[--a[i]] = i;
    }
    std::cout << "3\n";
    for (int start = 0; start < n / 2; start += n / 4) {
        std::vector<int> sort_pos;
        std::vector<bool> check(n, false);
        std::vector<int> sort_a;
        for (int i = start; i < start + n / 4; i++) {
            sort_pos.push_back(i);
            sort_a.push_back(a[i]);
            check[i] = true;
        }
        for (int i = start; i < start + n / 4; i++) {
            if (check[pos[i]]) continue;
            sort_pos.push_back(pos[i]);
            sort_a.push_back(i);
            check[pos[i]] = true;
        }
        int i = start;
        while (sort_pos.size() < n / 2) {
            while (check[i]) i++;
            sort_pos.push_back(i);
            sort_a.push_back(a[i]);
            check[i] = true;
        }
        for (int v : sort_pos) {
            std::cout << v + 1 << ' ';
        }
        std::cout << '\n';
        std::sort(sort_pos.begin(), sort_pos.end());
        std::sort(sort_a.begin(), sort_a.end());
        for (i = 0; i < n / 2; i++) {
            a[sort_pos[i]] = sort_a[i];
            pos[sort_a[i]] = sort_pos[i];
        }
    }
    for (int i = n / 2; i < n; i++) {
        std::cout << i + 1 << ' ';
    }
    return 0;
}
