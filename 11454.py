import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


def calc_max(arr):
    ans_cnt = -1
    ans_idx = -1
    for i in range(len(arr)):
        if arr[i] > ans_cnt:
            ans_cnt = arr[i]
            ans_idx = i
    return ans_cnt, ans_idx


for _ in range(int(input_())):
    s = input_().rstrip()
    alph = [0] * 26
    for char in s:
        alph[ord(char) - 97] += 1
    res = [''] * len(s)
    pointer = 0
    while pointer < len(s):
        if res[pointer]:
            pointer += 1
            continue
        left = len(s) - pointer
        z, a = calc_max(alph)
        # print(pointer, z, chr(a + 97), ' '.join(res))
        z = 2 * z - 1
        if z > left:
            print('IMPOSSIBLE')
            break
        elif z == left:
            alphabet_to_put = chr(a + 97)
            for i in range(pointer, len(s), 2):
                res[i] = alphabet_to_put
            alph[a] = 0
        else:
            for i in range(26):
                if alph[i] and (not pointer or ord(res[pointer - 1]) - 97 != i):
                    res[pointer] = chr(i + 97)
                    alph[i] -= 1
                    break
            else:
                assert False
        pointer += 1
    else:
        print(''.join(res))
