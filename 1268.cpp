#include <iostream>

int main() {
    std::cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);

    int students;
    std::cin >> students;

    int class_info[students][5];
    for (int i = 0; i < students; i++) {
        for (int j = 0; j < 5; j++) std::cin >> class_info[i][j];
    }

    int max_val = -1;
    int max_idx = -1;
    for (int i = 0; i < students; i++) {
        int cnt = 0;
        for (int j = 0; j < students; j++) {
            if (i == j) continue;
            for (int k = 0; k < 5; k++) {
                if (class_info[i][k] == class_info[j][k]) {
                    cnt++;
                    break;
                }
            }
        }
        if (cnt > max_val) {
            max_val = cnt;
            max_idx = i;
        }
    }

    std::cout << max_idx + 1;
    return 0;
}
