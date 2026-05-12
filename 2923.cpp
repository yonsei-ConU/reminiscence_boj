#include <iostream>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    int A[100] = {0};
    int B[100] = {0};
    while (N--) {
        int a, b;
        std::cin >> a >> b;
        a--; b--;
        A[a]++;
        B[b]++;
        int ans = 0;
        int C[100];
        for (int i = 0; i < 100; i++) {
            C[i] = B[i];
        }
        int b_ptr = 99;
        for (int a_ptr = 0; a_ptr < 100; a_ptr++) {
            if (A[a_ptr] == 0) continue;
            // C에서 A[a_ptr] 개만큼 없애야 함
            int cur = A[a_ptr];
            while (cur > 0) {
                while (C[b_ptr] == 0 && b_ptr > 0) b_ptr--;
                if (ans < a_ptr + b_ptr + 2) ans = a_ptr + b_ptr + 2;
                if (C[b_ptr] >= cur) {
                    C[b_ptr] -= cur;
                    cur = 0;
                } else {
                    cur -= C[b_ptr];
                    b_ptr--;
                }
            }
        }
        std::cout << ans << '\n';
    }
    return 0;
}
