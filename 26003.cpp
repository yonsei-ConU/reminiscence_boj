#include <iostream>
#include <cmath>
#include <iomanip>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n;
    std::cin >> n;
    long long planets[n][3];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 3; j++) {
            std::cin >> planets[i][j];
        }
    }
    long long ans = 9e18;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            ans = std::min(ans, (planets[i][0] - planets[j][0]) * (planets[i][0] - planets[j][0]) + (planets[i][1] - planets[j][1]) * (planets[i][1] - planets[j][1]) + (planets[i][2] - planets[j][2]) * (planets[i][2] - planets[j][2]));
        }
    }
    std::cout << std::fixed << std::setprecision(10) << std::sqrt((long double)ans);
    return 0;
}
