import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


word_original = sorted(set(input_().rstrip().replace(' ', '')))
word = tuple(map(lambda s: ord(s) - 65, word_original))
N = len(word)
ans_val = 27
ans_order = ''
# 앞으로 먼저 갔다가 뒤로 가는 경우
for front in range(N - 1):
    if word[front] * 2 + 26 - word[front + 1] < ans_val:
        ans_val = word[front] * 2 + 26 - word[front + 1]
        ans_order = word_original[:front + 1] + word_original[front + 1:][::-1]
# 앞쪽 방향으로만 가는 경우
if word[-1] < ans_val:
    ans_val = word[-1]
    ans_order = word_original
# 뒤쪽 방향으로만 가는 경우
if 26 - word[0] < ans_val:
    ans_val = 26 - word[0]
    ans_order = word_original[::-1]
# 뒤로 먼저 갔다가 앞으로 가는 경우
for back in range(N - 1, 0, -1):
    if (26 - word[back]) * 2 + word[back - 1] < ans_val:
        ans_val = (26 - word[back]) * 2 + word[back - 1]
        ans_order = word_original[back:][::-1] + word_original[:back]

print(ans_val + N)
print(''.join(ans_order))
