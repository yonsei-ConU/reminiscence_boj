import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


class lazy_segtree:
    def __init__(self, arr, func, apply_func, merge_func, identity, lazy_identity):
        """
        세그먼트 트리 초기화.

        :param arr: 초기 배열
        :param func: 구간 집계를 위한 함수 (예: 합, 최소값, 최대값 등)
        :param apply_func: 업데이트 함수를 적용하는 함수
        :param merge_func: 지연된 업데이트를 병합하는 함수
        :param identity: 구간 집계의 항등원 (예: 0 for sum, inf for min)
        :param lazy_identity: 지연된 업데이트의 항등원
        """
        self.n = 1
        while self.n < len(arr):
            self.n <<= 1
        self.size = self.n
        self.func = func
        self.apply_func = apply_func
        self.merge_func = merge_func
        self.identity = identity
        self.lazy_identity = lazy_identity

        # 트리 배열과 지연 배열 초기화
        self.tree = [self.identity] * (2 * self.n)
        self.lazy = [self.lazy_identity] * (2 * self.n)

        # 리프 노드에 초기 배열 값 설정
        for i in range(len(arr)):
            self.tree[self.n + i] = arr[i]

        # 내부 노드 계산
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.func(self.tree[2 * i], self.tree[2 * i + 1])

    def _push(self, node, node_left, node_right):
        """
        지연된 업데이트를 현재 노드의 자식 노드에 전달합니다.

        :param node: 현재 노드 인덱스
        :param node_left: 현재 노드의 왼쪽 경계
        :param node_right: 현재 노드의 오른쪽 경계
        """
        if self.lazy[node] != self.lazy_identity:
            mid = (node_left + node_right) // 2
            # 자식 노드에 업데이트 적용
            self._apply(2 * node, node_left, mid, self.lazy[node])
            self._apply(2 * node + 1, mid + 1, node_right, self.lazy[node])
            # 현재 노드의 지연 값 초기화
            self.lazy[node] = self.lazy_identity

    def _apply(self, node, node_left, node_right, value):
        """
        특정 노드에 업데이트를 적용합니다.

        :param node: 노드 인덱스
        :param node_left: 노드의 왼쪽 경계
        :param node_right: 노드의 오른쪽 경계
        :param value: 적용할 업데이트 값
        """
        self.tree[node] = self.apply_func(self.tree[node], value, node_right - node_left + 1)
        if node < self.n:
            self.lazy[node] = self.merge_func(self.lazy[node], value)

    def update_range(self, l, r, value):
        """
        [l, r] 범위에 업데이트를 적용합니다.

        :param l: 업데이트 범위의 왼쪽 인덱스 (0-based)
        :param r: 업데이트 범위의 오른쪽 인덱스 (0-based)
        :param value: 업데이트 값
        """
        def update_recursive(node, node_left, node_right):
            if r < node_left or node_right < l:
                return
            if l <= node_left and node_right <= r:
                self._apply(node, node_left, node_right, value)
                return
            self._push(node, node_left, node_right)
            mid = (node_left + node_right) // 2
            update_recursive(2 * node, node_left, mid)
            update_recursive(2 * node + 1, mid + 1, node_right)
            self.tree[node] = self.func(self.tree[2 * node], self.tree[2 * node + 1])

        update_recursive(1, 0, self.n - 1)

    def query_range(self, l, r):
        """
        [l, r] 범위의 집계를 반환합니다.

        :param l: 질의 범위의 왼쪽 인덱스 (0-based)
        :param r: 질의 범위의 오른쪽 인덱스 (0-based)
        :return: 집계 결과
        """
        res_left = self.identity
        res_right = self.identity

        def query_recursive(node, node_left, node_right):
            nonlocal res_left, res_right
            if r < node_left or node_right < l:
                return
            if l <= node_left and node_right <= r:
                if node_left < node_right:
                    res_left = self.func(res_left, self.tree[node])
                else:
                    res_left = self.func(res_left, self.tree[node])
                return
            self._push(node, node_left, node_right)
            mid = (node_left + node_right) // 2
            query_recursive(2 * node, node_left, mid)
            query_recursive(2 * node + 1, mid + 1, node_right)

        query_recursive(1, 0, self.n - 1)
        return self.func(res_left, res_right)


n, m, k = map(int, input_().split())
arr = [int(input_()) for i in range(n)]
st = lazy_segtree(arr)
for i in range(m+k):
    l = list(map(int, input_().split()))
    if len(l) == 3:
        a, b, c = l
    else:
        a, b, c, d = l
    if a == 1:
        st.update_range(1, 0, len(arr)-1, b-1, c-1, d)
    else:
        print(st.query(1, 0, len(arr)-1, b-1, c-1))

