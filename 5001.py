import sys
from heapq import heappush, heappop


small_heap = []
large_heap = []
median = -1
for line in sys.stdin:
    if line == '#\n':
        assert median != -1
        print(median)
        if len(small_heap) == len(large_heap):
            if not small_heap:
                median = -1
                continue
            _, v = heappop(large_heap)
        else:
            _, v = heappop(small_heap)
        median = v
    else:
        if median == -1:
            median = int(line)
            continue
        x = int(line)
        chk = len(small_heap) == len(large_heap)
        values = [x, median]
        if large_heap:
            _, v = heappop(large_heap)
            values.append(v)
        if small_heap:
            _, v = heappop(small_heap)
            values.append(v)
        values = sorted(values)
        # print(len(values))
        if not chk:
            if len(values) == 3:
                a = values.pop()
                heappush(large_heap, (a, a))
                median = values.pop()
                a = values.pop()
                heappush(small_heap, (-a, a))
            else:
                assert len(values) == 4
                a = values.pop()
                heappush(large_heap, (a, a))
                a = values.pop()
                heappush(large_heap, (a, a))
                median = values.pop()
                a = values.pop()
                heappush(small_heap, (-a, a))
        else:
            if len(values) == 2:
                a = values.pop()
                heappush(small_heap, (a, a))
                median = values.pop()
            else:
                assert len(values) == 4
                a = values.pop()
                heappush(large_heap, (a, a))
                median = values.pop()
                a = values.pop()
                heappush(small_heap, (-a, a))
                a = values.pop()
                heappush(small_heap, (-a, a))
