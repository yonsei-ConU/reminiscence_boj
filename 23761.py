import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


n = int(input_())
ptr = 1
while True:
    if ptr == n:
        print(f"! {n}", flush=True)
        break
    elif ptr == n - 1:
        print(f"? {n - 2} {n - 1}", flush=True)
        ans = input_().rstrip()
        if ans == 'equal':
            print(f"! {n}", flush=True)
        else:
            print(f"! {n - 1}", flush=True)
        break
    else:
        print(f"? {ptr} {ptr + 1}", flush=True)
        ans = input_().rstrip()
        if ans == 'equal':
            ptr += 2
            continue
        elif ptr == 1:
            print(f"? 1 3", flush=True)
            ans = input_().rstrip()
            if ans == 'equal':
                print(f"! 2", flush=True)
            else:
                print(f"! 1", flush=True)
        else:
            print(f"? 1 {ptr}", flush=True)
            ans = input_().rstrip()
            if ans == 'equal':
                print(f"! {ptr + 1}", flush=True)
            else:
                print(f"! {ptr}", flush=True)
        break
