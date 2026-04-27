import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


for i in range(1, int(input_()) + 1):
    s1 = input_().strip().lower()
    while '  ' in s1:
        s1 = s1.replace('  ', ' ')
    s2 = input_().strip().lower()
    while '  ' in s2:
        s2 = s2.replace('  ', ' ')
    d = {'[': '(', ']': ')', '{': '(', '}': ')', ';': ','}
    for element in d:
        s1 = s1.replace(element, d[element])
        s2 = s2.replace(element, d[element])
    d = {' (': '(', '( ': '(', ' )': ')', ') ': ')', ' .': '.', '. ': '.', ' ,': ',', ', ': ',', ' :': ':', ': ': ':'}
    for element in d:
        s1 = s1.replace(element, d[element])
        s2 = s2.replace(element, d[element])
    print(f"Data set {i}: {'not ' * (s1 != s2)}equal\n")
