#include <iostream>
#include <bitset>
#include <vector>
typedef long long ll;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;
    int comb[5][5] = {1, 0, 0, 0, 0,
                      1, 1, 0, 0, 0,
                      1, 2, 1, 0, 0,
                      1, 3, 3, 1, 0,
                      1, 4, 6, 4, 1};
    int pow[9] = {1, 5, 25, 125, 625, 3125, 15625, 78125, 390625};

    int cnt[9] = {0};
    while (N--) {
        int t;
        std::cin >> t;
        cnt[t - 1]++;
    }

    std::vector<std::vector<int>> d;
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < i; j++) {
            for (int k = 0; k < j; k++) {
                std::vector<int> tmp = {i, j, k};
                d.push_back(tmp);
            }
        }
    }

    std::bitset<1953125> chk;
    int req[9] = {0};
    int t = 0;
    for (int head = 0; head < 9; head++) {
        req[head] += 2;
        if (req[head] > cnt[head]) {
            req[head] -= 2;
            continue;
        }
        t += pow[head] * 2;
        for (int i = 0; i < 84; i++) {
            bool ok = true;
            int dreq[9] = {0};
            int dt = 0;
            for (int x : d[i]) {
                if (req[x] == cnt[x]) {
                    ok = false;
                    break;
                }
                dreq[x]++;
                dt += pow[x];
            }
            if (!ok) continue;
            t += dt;
            for (int x = 0; x < 9; x++) {
                req[x] += dreq[x];
            }
            for (int j = 0; j < 84; j++) {
                bool ok = true;
                int dreq[9] = {0};
                int dt = 0;
                for (int x : d[j]) {
                    if (req[x] == cnt[x]) {
                        ok = false;
                        break;
                    }
                    dreq[x]++;
                    dt += pow[x];
                }
                if (!ok) continue;
                t += dt;
                for (int x = 0; x < 9; x++) {
                    req[x] += dreq[x];
                }
                for (int k = 0; k < 84; k++) {
                    bool ok = true;
                    int dreq[9] = {0};
                    int dt = 0;
                    for (int x : d[k]) {
                        if (req[x] == cnt[x]) {
                            ok = false;
                            break;
                        }
                        dreq[x]++;
                        dt += pow[x];
                    }
                    if (!ok) continue;
                    t += dt;
                    for (int x = 0; x < 9; x++) {
                        req[x] += dreq[x];
                    }
                    for (int l = 0; l < 84; l++) {
                        bool ok = true;
                        int dreq[9] = {0};
                        int dt = 0;
                        for (int x : d[l]) {
                            if (req[x] == cnt[x]) {
                                ok = false;
                                break;
                            }
                            dreq[x]++;
                            dt += pow[x];
                        }
                        if (!ok) continue;
                        t += dt;
                        for (int x = 0; x < 9; x++) {
                            req[x] += dreq[x];
                        }
                        chk[t] = true;
                        for (int x : d[l]) {
                            req[x]--;
                            t -= pow[x];
                        }
                    }
                    for (int x : d[k]) {
                        req[x]--;
                        t -= pow[x];
                    }
                }
                for (int x : d[j]) {
                    req[x]--;
                    t -= pow[x];
                }
            }
            for (int x : d[i]) {
                req[x]--;
                t -= pow[x];
            }
        }
    }

    ll ans = 0;
    for (int i = 0; i < 1953125; i++) {
        if (!chk[i]) continue;
        ll tmp = 1;
        int j = i;
        for (int x : cnt) {
            tmp *= comb[x][j % 5];
            j /= 5;
        }
        ans += tmp;
    }

    std::cout << ans;
    return 0;
}
