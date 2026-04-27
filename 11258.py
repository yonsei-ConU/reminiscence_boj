import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


first_num, first_money = input_().split() 
first_money = int(first_money)

first31, first31money = input_().split() 
first31money = int(first31money)

first32, first32money = input_().split() 
first32money = int(first32money)

last31, last31money = input_().split() 
last31money = int(last31money)

last32, last32money = input_().split() 
last32money = int(last32money)

last2, last2money = input_().split() 
last2money = int(last2money)


while True:
    n = input_().rstrip()
    if n == '-1':
        break
    ans = 0
    if n == first_num:
        ans += first_money
    if n.startswith(first31):
        ans += first31money
    if n.startswith(first32):
        ans += first32money
    if n.endswith(last31):
        ans += last31money
    if n.endswith(last32):
        ans += last32money
    if n.endswith(last2):
        ans += last2money
    print(ans)
