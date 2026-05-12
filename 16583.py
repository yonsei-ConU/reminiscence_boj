import sys
input_ = sys.stdin.readline
def minput(): return map(int, input_().split())


N, M = minput()
G = [[] for _ in range(N)]

for _ in range(M):
    u, v = minput()
    u = 1; v -= 1
    G[u].append(v)
    G[v].append(u)

"""
### sol by coconut99

* dfs tree
DFS를 돌려서 나온 스패닝 트리인건 뭐 알잖아
thm: 무향그래프의 dfs트리 상에서는 cross edge가 존재하지 않는다. 이것도 알고있긴해
pf) 귀류법 (cross edge가 존재했다면 dfs의 방문순서라는 가정에 모순된다)

간선의 개수가 M개인데, 부메랑은 항상 M>>1개만큼 만들 수 있음을 보일 수 있다.
리프노드에서부터 부메랑을 한 개씩 만든다.
리프노드는 자식으로 가는 간선따위 있을 리가 없기 때문에 front이든 back이든 하는 edge에 다 연결
"짝수면 다 없애고, 홀수면 하나만 빼고 다 없앤다"
"""
