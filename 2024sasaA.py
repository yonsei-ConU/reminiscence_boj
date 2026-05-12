import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


expression = input_().split()
stack = []
for e in expression:
    try:
        e = float(e)
        if len(stack) == 2:
            rlgh = stack.pop()
            d = stack.pop()
            if rlgh == '+':
                stack.append(d + e)
            elif rlgh == '-':
                stack.append(d - e)
            elif rlgh == '*':
                stack.append(d * e)
            else:
                stack.append(d / e)
        else:
            stack.append(e)
    except ValueError:
        stack.append(e)

result = f"{stack.pop():.3f}"
print("=================")
print("|SASA CALCULATOR|")
print(f"|{result: >15}|")
print("""-----------------
|               |
| AC         /  |
| 7  8  9    *  |
| 4  5  6    -  |
| 1  2  3    +  |
|    0  .    =  |
=================""")
