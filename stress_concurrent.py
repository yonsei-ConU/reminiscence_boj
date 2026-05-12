from random import randint
from tqdm import trange
from algorithms import *
# [추가] 병렬 실행을 위해 필요한 표준 라이브러리 임포트
from concurrent.futures import ProcessPoolExecutor, as_completed
import os

MAX_TC = 100


def solve(arg):
    """
    solution to test
    """
    from collections import deque
    N, g = arg
    if not N & 1:
        return False
    q = deque([0])
    depth = [0] + [-1] * (N - 1)
    par = [-1] * N
    while q:
        cur = q.popleft()
        for nxt in g[cur]:
            if depth[nxt] == -1:
                depth[nxt] = depth[cur] + 1
                par[nxt] = cur
                q.append(nxt)

    depth_rev = [[] for _ in range(N)]
    for i in range(N):
        depth_rev[depth[i]].append(i)

    cnt = 0
    ans = []
    for d in range(N - 1, 1, -1):
        for v in depth_rev[d]:
            ans.append(f"{v + 1} 1")
            ans.append(f"{v + 1} {par[v] + 1}")
            cnt += 1
            if cnt == (N - 1) >> 1:
                return True, '\n'.join(ans)

    ptr = 0
    while cnt < (N - 1) >> 1:
        cnt += 1
        ans.append(f"1 {depth_rev[1][ptr] + 1}")
        ans.append(f"{depth_rev[1][ptr] + 1} {depth_rev[1][ptr + 1] + 1}")
        ptr += 1

    return True, '\n'.join(ans)


def naive(arg):
    """
    brute force code
    """


def generator():
    N = 2 * randint(1, 4) + 1
    uf = UnionFind(N)
    e = 0
    ret = [[] for _ in range(N)]
    while e < N - 1:
        a = randint(0, N - 1)
        b = randint(0, N - 1)
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            ret[a].append(b)
            ret[b].append(a)
            e += 1
    return N, ret


def check(data, naive_sol, sol):
    if not sol:
        return False
    print(sol)
    N, g = data
    g2 = [[] for _ in range(N)]
    for a, b in sol[1]:
        a -= 1; b -= 1
        g2[a].append(b)
        g2[b].append(a)
    g3 = [set() for _ in range(N)]
    e = 0
    uf = UnionFind(N)
    for i in range(N):
        g[i] = set(g[i])
        g2[i] = set(g2[i])
        g3[i] = g[i] ^ g2[i]
        for v in g3[i]:
            uf.union(i, v)
            e += 1
    if uf.size[uf.find(0)] != N or e != N - 1:
        return False
    return True


# === 추가: 워커(최상위 정의, 한 번에 여러 케이스 처리해서 오버헤드 감소) ===
def _run_many(iters):
    """
    [추가] 단일 프로세스에서 iters개의 테스트를 연속 수행.
    - 실패 시 즉시 실패 정보를 반환하고 종료
    - 성공 시 (True, iters, None, None, None) 반환
    반환값: (ok, processed_count, data, naive_solution, solution)
    """
    for i in range(1, iters + 1):
        data = generator()
        naive_solution = naive(data)
        solution = solve(data)
        if not check(data, naive_solution, solution):
            # i번째에서 실패
            return (False, i, data, naive_solution, solution)
    return (True, iters, None, None, None)


# === 아래 블록만 교체 ===
if __name__ == "__main__":  # [유지] spawn 모드 안전 가드
    try:
        import multiprocessing as mp; mp.set_start_method("fork", force=True)  # [선택] macOS에서 성능/호환 개선

        # [추가] 병렬/배치 설정
        workers = os.cpu_count() or 2
        CHUNK_ITERS = MAX_TC // 100  # [핵심] 워커 1회 호출당 처리할 케이스 수(오버헤드 ↓)
        # 너무 크게 잡으면 한 작업이 오래 걸려 중단 감도가 떨어지니 환경에 맞춰 조절하세요.

        failed = False
        total_processed = 0     # 진행 카운터(원래 tc 누적 개념)
        last_input = None

        # future -> (start_index, assigned_iters) 매핑으로 "전역 테스트 번호" 계산
        with ProcessPoolExecutor(max_workers=workers) as ex:
            with trange(MAX_TC, desc="Running tests", unit="case") as pbar:
                futures = {}
                # [추가] 초기 작업 제출
                remaining = MAX_TC
                for _ in range(min(workers, (MAX_TC + CHUNK_ITERS - 1) // CHUNK_ITERS)):
                    iters = min(CHUNK_ITERS, remaining)
                    if iters <= 0:
                        break
                    start_index = MAX_TC - remaining + 1  # 전역 1-based 시작 번호
                    fut = ex.submit(_run_many, iters)
                    futures[fut] = (start_index, iters)
                    remaining -= iters

                while futures and not failed:
                    for fut in as_completed(list(futures.keys())):
                        start_index, assigned = futures.pop(fut)
                        ok, processed, data, naive_solution, solution = fut.result()
                        total_processed += processed
                        pbar.update(processed)
                        last_input = data

                        if not ok:
                            # [추가] 전역 실패 케이스 번호 = 해당 작업 시작 번호 + (작업 내 실패 위치 - 1)
                            failed_tc = start_index + processed - 1
                            print(f"\nTest case #{failed_tc} failed")
                            print(f"Input: {data}")
                            print(f"Expected: {naive_solution}")
                            print(f"Received: {solution}")
                            failed = True
                            # [추가] 남은 작업 취소
                            for f in futures:
                                f.cancel()
                            break

                        # [추가] 성공적으로 끝났으면 다음 작업 제출(남은 물량이 있으면)
                        if remaining > 0:
                            iters = min(CHUNK_ITERS, remaining)
                            next_start = MAX_TC - remaining + 1
                            new_fut = ex.submit(_run_many, iters)
                            futures[new_fut] = (next_start, iters)
                            remaining -= iters

                    # 루프 탈출 조건 재확인
                    if failed:
                        break

        if not failed and total_processed >= MAX_TC:
            print(f"\n{MAX_TC} test cases passed")
    except KeyboardInterrupt:
        print(f"\nStopping. Currently {total_processed} Test cases passed")
        print(f"Last Input: {last_input if 'last_input' in locals() else 'N/A'}")
# === 교체 끝 ===
