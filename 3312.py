import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


pattern = input_().rstrip()
text = input_().rstrip()
text_cnt = [0] * 26
x = len(text) - len(pattern) + 1
for i in range(x): text_cnt[ord(text[i]) - 97] += 1

ans = 0
for i in range(len(pattern)):
    ans += text_cnt[ord(pattern[i]) - 97]
    text_cnt[ord(text[i]) - 97] -= 1
    if i != len(pattern) - 1: text_cnt[ord(text[i + x]) - 97] += 1

print(ans)
