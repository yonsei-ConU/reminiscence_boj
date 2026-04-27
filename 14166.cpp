#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
//#include "algorithms.cpp"

typedef long long ll;

struct Partition {
    int unfixed;
    int idx;
    ll cost;
};

int get_key(const std::vector<int> &v) {
    if (v.size() == 1) return 2147483647;
    else return v[1] - v[0];
}

auto comp1 = [](const std::vector<int> &lhs, const std::vector<int> &rhs) {
    return get_key(lhs) < get_key(rhs);
};

struct comp2 {
    bool operator()(const Partition& lhs, const Partition& rhs) {
        return lhs.cost > rhs.cost;
    }
};


int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int N, K;
    std::cin >> N >> K;
    std::vector<std::vector<int>> controllers(N);
    ll ans = 0;
    for (auto &i : controllers) {
        int M;
        std::cin >> M;
        i.resize(M);
        for (auto &j : i) std::cin >> j;
        std::sort(i.begin(), i.end());
        ans += i[0];
    }
    if (K == 1) {
        std::cout << ans;
        return 0;
    }
    std::sort(controllers.begin(), controllers.end(), comp1);
    //ConU::print2D(controllers);
    std::priority_queue<Partition, std::vector<Partition>, comp2> q;
    q.push({0, 1, ans + get_key(controllers[0])});
    int k = 2;
    while (!q.empty()) {
        Partition cur = q.top(); q.pop();
        //std::cout << cur.unfixed << ' ' << cur.idx << ' ' << cur.cost << std::endl;
        ans += cur.cost;
        if (k == K) {
            std::cout << ans;
            return 0;
        }
        k++;
        if (controllers[cur.unfixed].size() > cur.idx + 1) {
            q.push({cur.unfixed, cur.idx + 1, cur.cost + controllers[cur.unfixed][cur.idx + 1] - controllers[cur.unfixed][cur.idx]});
        }
        if (cur.unfixed < N - 1 && controllers[cur.unfixed + 1].size() > 1) {
            q.push({cur.unfixed + 1, 1, cur.cost + get_key(controllers[cur.unfixed + 1])});
            if (cur.idx == 1) {
                q.push({cur.unfixed + 1, 1, cur.cost + get_key(controllers[cur.unfixed + 1]) - get_key(controllers[cur.unfixed])});
            }
        }
    }
    return 1;
}
