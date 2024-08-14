import sys
sys.stdin = open('sample_input.txt')

def bfs(S, G, V):  # 시작정점 s, 마지막 정점 V
    # 준비
    visited = [0] * (V + 1)  # visited 생성
    q = []  # 큐 생성
    q.append(S)  # 시작점 인큐
    visited[S] = 1  # 시작점 방문표시

    # 탐색 진행
    while q:  # 큐에 정점이 남아있으면 front != rear / 즉, 큐가 비어있지않으면
        t = q.pop(0)  # 디큐

        # t의 인접이고, 인큐된 적 없으면 인큐하고 인큐 표시
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)  # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1 # 간선 수를 구할 때 visited의 차로 구할 수 ㅇ
                # 노드 w는 노드 t에 인접한 노드..
                # 즉, w까지의 최단 거리는 t까지의 최단 거리에서 한 단계(즉, +1) 더 가는 것

    if visited[G] == 0: # 도착 노드"G"에 도달 못한 경우
        return 0
    return visited[G]-1 # 출발노드에서 도착노드의 최단거리 (시작 노드가 1이므로 -1해주기)

# 1. 입력받기
T = int(input())
for tc in range(1, T+1):
    # V : 노드(정점) 갯수 / E : 간선 갯수
    V, E = map(int, input().split())
    # arr : 간선 양쪽의 노드 번호 리스트
    # 2개의 요소씩 입력 받는걸 E씩 반복
    arr = [int(i) for _ in range(E) for i in input().split()]
    # S : 출발 노드 / G : 도착노드
    S, G = map(int, input().split())

    #adj_l : 인접 리스트
    adj_l = [[] for _ in range(V + 1)]

    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)

    print(f"{tc} {bfs(S,G,V)}")
