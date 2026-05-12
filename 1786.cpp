#include <iostream>
#include <vector>

std::vector<int> knuth_morris_pratt(std::string &s1, std::string &s2) {
    std::vector<int> fail(s2.size(), 0);
    int j = 0;
    for (int i = 1; i < s2.size(); i++) {
        while (j > 0 && s2[i] != s2[j]) j = fail[j - 1];
        if (s2[i] == s2[j]) {
            j++;
            fail[i] = j;
        }
    }
    std::vector<int> ret;
    j = 0;
    for (int i = 0; i < s1.size(); i++) {
        while (j > 0 && s1[i] != s2[j]) j = fail[j - 1];
        if (s1[i] == s2[j]) {
            if (j + 1 == s2.size()) ret.push_back(i - (int)s2.size() + 2);
            j = fail[j];
        } else {
            j++;
        }
    }
    return ret;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::string S, T;
    getline(std::cin, S);
    getline(std::cin, T);
    std::vector<int> found = knuth_morris_pratt(S, T);
    std::cout << found.size() << '\n';
    for (int i : found) std::cout << i << ' ';
    return 0;
}
