#include <iostream>
#include <vector>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    if (n > 700) {
        std::cout << "Yes";
        return 0;
    }
    std::vector<int> a(n);
    bool chk[131072] = {false};
    for (auto &i : a) {
        std::cin >> i;
        chk[i] = true;
    }
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < i; j++) {
            for (int k = 0; k < j; k++) {
                if (chk[a[i] ^ a[j] ^ a[k]]) {
                    std::cout << "Yes";
                    return 0;
                }
            }
        }
    }
    std::cout << "No";
    return 0;
}
