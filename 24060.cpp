#include <iostream>
#include <vector>

int save = 0;
int N, K;

bool merge(int start, int mid, int end, std::vector<int> &arr) {
    int i = start;
    int j = mid + 1;
    std::vector<int> tmp;
    while (i <= mid && j <= end) {
        if (arr[i] <= arr[j]) tmp.push_back(arr[i++]);
        else tmp.push_back(arr[j++]);
    }
    while (i <= mid) {
        tmp.push_back(arr[i++]);
    }
    while (j <= end) {
        tmp.push_back(arr[j++]);
    }
    for (int x = 0; x < tmp.size(); x++) {
        arr[x + start] = tmp[x];
        save++;
        if (save == K) {
            std::cout << tmp[x];
            return true;
        }
    }
    return false;
}

bool merge_sort(int start, int end, std::vector<int> &arr) {
    if (start < end) {
        int mid = (start + end) >> 1;
        if (merge_sort(start, mid, arr)) return true;
        if (merge_sort(mid + 1, end, arr)) return true;
        if (merge(start, mid, end, arr)) return true;
    }
    return false;
}

int main(){
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    std::cin >> N >> K;
    std::vector<int> A(N);
    for (auto &i : A) std::cin >> i;
    if (!merge_sort(0, N - 1, A)) std::cout << -1;
    return 0;
}
