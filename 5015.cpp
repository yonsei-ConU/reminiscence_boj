#include <iostream>
#include <string>

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string P;
    std::cin >> P;
    int N;
    std::cin >> N;

    while (N--) {
        std::string name;
        std::cin >> name;
        // dp[i][j]: P[i], name[j]까지의 매칭이 가능한가?
        bool dp[P.size()][name.size()];
        for (int i = 0; i < P.size(); i++) {
            for (int j = 0; j < name.size(); j++) {
                dp[i][j] = false;
                if (!i) {

                }
            }
        }
    }
    return 0;
}
