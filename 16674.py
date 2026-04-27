# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ
# 연>>>>>>>>>>>>>>>>>>>. 누구나 아는 팩트 ㄹㅇㅋㅋ

import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N = int(input_())
sN = str(N)
if sN.replace('2', '').replace('0', '').replace('1', '').replace('8', ''): exit(print(0))
elif not ('2' in sN and '0' in sN and '1' in sN and '8' in sN): exit(print(1))
elif len(set(sN.count(i) for i in '2018')) != 1: exit(print(2))
print(8)
