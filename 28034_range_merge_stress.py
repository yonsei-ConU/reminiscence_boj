import random


def solve(r1, r2):
    if not r1 or not r2:
        return range(0)

    len_r1 = len(r1)
    len_r2 = len(r2)

    if len_r1 == 1 and len_r2 == 1:
        step_s3 = 1
    elif len_r1 == 1:
        step_s3 = r2.step
    elif len_r2 == 1:
        step_s3 = r1.step
    elif r1.step == 1 or r2.step == 1:
        step_s3 = 1
    else:
        step_s3 = 2

    min_sum = r1.start + r2.start
    max_sum = r1[-1] + r2[-1]
    return set(range(min_sum, max_sum + step_s3, step_s3))


def naive(r1, r2):
    ret = set()
    for a in r1:
        for b in r2:
            ret.add(a + b)
    return ret


try:
    for i in range(1, 10001):
        start2 = random.randint(1, 30)
        step2 = random.randint(1, 2)
        stop2 = start2 + step2 * random.randint(1, 30) + 1
        # start1 = random.randint(1, 10)
        start1 = random.randint(1, 30)
        step1 = random.randint(1, 2)
        stop1 = start1 + step1 * random.randint(1, 30) + 1
        r1 = range(start1, start1 + 2, 2)
        r2 = range(start2, stop2, step2)
        n = naive(r1, r2)
        s = solve(r1, r2)
        if n != s:
            print(f"Test case #{i} failed")
            print(f"Input {r1} {r2}")
            # print(f"Output: {p}")
            print(f"Expected: {sorted(n)}")
            print(f"Received: {sorted(s)}")
            break
    else:
        print(f"10000 Test cases passed")
except KeyboardInterrupt:
    print(f"Stopping. Currently {i} Test cases passed")
