import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def cur_sum(l):
    return sum(10 ** (len(l) - 1 - i) * l[i] for i in range(len(l)))


def find_distinct(cur, used, target_length):
    if len(cur) == target_length:
        if cur_sum(cur) > N:
            return cur_sum(cur)
        else:
            return

    for digit in range(1, 10):
        if not used & (1 << digit):
            cur.append(digit)
            used |= 1 << digit
            result = find_distinct(cur, used, target_length)
            if result:
                return result
            cur.pop()
            used ^= 1 << digit
    return


while True:
    try:
        N = int(input_())
    except:
        break
    max_list = [98765432, 9876543, 987654, 98765, 9876, 987, 98, 9]
    min_list = [123456789, 12345678, 1234567, 123456, 12345, 1234, 123, 12, 1]
    if N >= 987654321:
        print(0)
        continue
    for i in range(8):
        if max_list[i] <= N < min_list[i]:
            print(min_list[i])
            break
    else:
        res = list(map(int, list(str(N))))
        print(find_distinct([], 0, len(str(N))))
