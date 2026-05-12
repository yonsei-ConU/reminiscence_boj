#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

static std::string trans(const std::string &s) {
    std::string t = s;
    for (char &c : t) {
        if (c == '6') c = '9';
        else if (c == '9') c = '6';
    }
    std::reverse(t.begin(), t.end());
    return t;
}

bool cmp(const std::string &s1, const std::string &s2) {
    return s1 + s2 > s2 + s1;
}

bool cmp2(const std::string &s1, const std::string &s2) {
    if (s1.size() > s2.size()) return true;
    if (s1.size() < s2.size()) return false;
    return cmp(s1, s2);
}

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N;
    std::cin >> N;

    std::vector<std::string> lst;
    lst.reserve(N);

    for (int i = 0; i < N; i++) {
        std::string temp;
        std::cin >> temp;
        lst.push_back(trans(temp));
    }

    std::sort(lst.begin(), lst.end(), cmp);
    std::vector<std::string> lst2 = lst;
    std::sort(lst2.begin(), lst2.end(), cmp2);
    std::string inject_first = lst2.front();

    int idx = -1;
    for (int i = 0; i < (int)lst.size(); i++) {
        if (lst[i] == inject_first) {
            idx = i;
            break;
        }
    }
    std::string result;
    for (int i = 0; i < idx; i++) {
        result += lst[i];
    }
    result += lst[idx];
    for (int i = idx; i < (int)lst.size(); i++) {
        result += lst[i];
    }

    std::cout << trans(result) << "\n";
    return 0;
}
