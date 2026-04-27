#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>

struct AhoCorasickNode {
    int children[26];
    char s;
    int fail = -1;
    int remove = 0;
    AhoCorasickNode(char s = '\0') : s(s), fail(-1) {
        for (auto & i : children) {
            i = -1;
        }
    }
};

AhoCorasickNode nodes[100000];

struct AhoCorasick {
    static int node_cnt;
    int root;
    AhoCorasick() {
        root = 0;
        node_cnt = 1;
    }
    void insert(const std::string &word) {
        int cur = 0;
        for (char c : word) {
            int c_idx = c - 97;
            if (nodes[cur].children[c_idx] == -1) {
                nodes[cur].children[c_idx] = node_cnt++;
            }
            cur = nodes[cur].children[c_idx];
        }
        nodes[cur].remove = word.size();
    }
    void build() {
        std::queue<int> q;
        for (int & c : nodes[root].children) {
            if (c != -1) {
                nodes[c].fail = root;
                q.push(c);
            } else {
                c = root;
            }
        }
        while (!q.empty()) {
            int u = q.front(); q.pop();
            for (int c = 0; c < 26; c++) {
                int v = nodes[u].children[c];
                if (v != -1) {
                    nodes[v].fail = nodes[nodes[u].fail].children[c];
                    nodes[v].remove = std::max(nodes[v].remove, nodes[nodes[v].fail].remove);
                    q.push(v);
                } else {
                    nodes[u].children[c] = nodes[nodes[u].fail].children[c];
                }
            }
        }
    }
};

int AhoCorasick::node_cnt = 0;

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string S;
    std::cin >> S;
    int N;
    std::cin >> N;
    AhoCorasick ac;
    for (int i = 0; i < N; i++) {
        std::string word;
        std::cin >> word;
        ac.insert(word);
    }
    ac.build();
    std::vector<int> J(S.size() + 1, 0);
    std::vector<char> ans(S.size());
    int cur = 0;
    int r = 0;
    for (char c : S) {
        int idx = c - 97;
        cur = nodes[cur].children[idx];
        ans[r++] = c;
        J[r] = cur;
        if (nodes[cur].remove) {
            r -= nodes[cur].remove;
            cur = J[r];
        }
    }
    for (int i = 0; i < r; i++) {
        std::cout << ans[i];
    }
    return 0;
}
