import sys
from heapq import heappop, heappush
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
class_ = [list(minput()) for _ in range(N)]
class_.sort()
ans = 0
heap = []
for start, end in class_:
    while heap:
        e, s = heappop(heap)
        if e > start:
            heappush(heap, (e, s))
            break
    heappush(heap, (end, start))
    ans = max(ans, len(heap))

print(ans)

"""
시작하는 시간순, 같다면 끝나는 시간순으로 정렬한다.
이제 각각의 강의를 실시간으로 넣고 뺀다.
특정한 강의가 시작하는 시점에서 끝나거나 이미 끝나 있는 강의들은 모두 뺀다. (끝나는 순서 기준으로 힙에다가 넣음)
각 시점들에 대해서 가장 많은 강의가 진행되는 시점이 정답
CLAIM OPT >= max_len
어떤 시점에서 x개의 강의가 진행되고 있다면, 당연히 강의실이 최소 x개가 필요하다.
CLAIM OPT <= max_len -> unnecessary
PROOF `OPT == max_len을 만드는 방법이 존재한다.`
그냥 위에서 넣을 때 방금 넣은 강의가 몇 번 강의실에서 되고 있는지만 관리하면 되는 거 아닌가???
"""
