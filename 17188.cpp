#include <iostream>
#include <vector>
#include <queue>

typedef long long ll;
int N, K, C;

struct Partition {
    std::vector<bool> ban;
    std::vector<int> fix;
    std::vector<int> chosen;
    ll score;
    Partition(std::vector<bool> b, std::vector<int> f, const std::vector<std::vector<ll>> &scores) {
        chosen.resize(f.size());
        std::vector<ll> hohyun(f.size(), 0);
        score = 0;
        ban = b;
        fix = f;
        std::vector<bool> tempban(b.size());
        for (int i = 0; i < fix.size(); i++) {
            if (fix[i] != -1) {
                for (int x = 0; x < fix.size(); x++) {
                    hohyun[x] = std::max(hohyun[x], scores[fix[i]][x]);
                }
                chosen[i] = fix[i];
            } else {
                int max_idx = -1;
                int max_val = -1;
                for (int j = 0; j < ban.size(); j++) {
                    if (!tempban[j] && !ban[j]) {
                        if (scores[j][i] > max_val) {
                            max_idx = j;
                            max_val = scores[j][i];
                        }
                    }
                }
                if (max_idx == -1) {
                    score = -9999999999;
                    return;
                }
                chosen[i] = max_idx;
                tempban[max_idx] = true;
                for (int x = 0; x < fix.size(); x++) {
                    hohyun[x] = std::max(hohyun[x], scores[max_idx][x]);
                }
            }
        }
        for (ll v : hohyun) score += v;
    }
};

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::cin >> N >> K >> C;
    std::vector<std::vector<ll>> scores(N, std::vector<ll>(K, 0));
    for (auto &i : scores) {
        for (auto &j : i) std::cin >> j;
    }
    std::priority_queue<Partition, std::vector<Partition>, bool(*)(const Partition&, const Partition&)> q([](const Partition &a, const Partition &b) { return a.score < b.score; });
    q.push(Partition(std::vector<bool>(N, false), std::vector<int>(K, -1), scores));
    int c = 1;
    while (!q.empty()) {
        Partition cur = q.top(); q.pop();
        if (c == C) {
            std::cout << cur.score;
            return 0;
        }
        c++;
        std::vector<bool> nxt_ban = cur.ban;
        std::vector<int> nxt_fix(K, -1);
        for (int i = 0; i < K; i++) {
            if (cur.fix[i] != -1) {
                nxt_fix[i] = cur.fix[i];
                nxt_ban[cur.fix[i]] = true;
            }
        }
        for (int i = 0; i < K; i++) {
            if (cur.fix[i] == -1) {
                nxt_ban[cur.chosen[i]] = true;
                q.push(Partition(nxt_ban, nxt_fix, scores));
                nxt_fix[i] = cur.chosen[i];
            }
        }
    }
    return 1;
}
