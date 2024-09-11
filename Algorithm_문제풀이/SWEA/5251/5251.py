import sys
sys.stdin = open("sample_input.txt","r")

def dijkstra(start, N):
    cost[start] = 0 # 시작노드 비용을 초기화

    # 모든 노드 방문 시작
    for _ in range(N+1):
        min_cost = int(1e9)
        min_node = -1

        # 방문x 면서 비용이 가장 적은 노드 찾기
        for j in range(N):
            if not visited[j] and cost[j] < min_cost: # 방문한적 없고 최소 비용이라면
                # 갱신
                min_cost = cost[j]
                min_node = j

        if min_node == -1: # 방문할 노드가 없으면 종료
            break

        visited[min_node] = True # 방문

        # cost, 노드 갱신
        for nx_node, weight in graph[min_node]:
            if not visited[nx_node]: # 방문한 적이 없다면
                new_cost = cost[min_node] + weight
                if new_cost < cost[nx_node]: # 최단 이동이라면 갱신
                    cost[nx_node] = new_cost

T = int(input())
for tc in range(1,T+1):
    N,E = map(int,input().split()) # N : 도착지점 / E : 간선 갯수
    graph = [[] for i in range(N+1)] # 인접리스트
    visited = [False] * (N+1)  # 방문체크 리스트
    cost = [int(1e9)] * (N+1) # 최단 거리 초기화

    for _ in range(E):
        s, e, w = map(int,input().split()) # s: 구간 시작/ e: 구간 끝/ w: 비용
        graph[s].append([e,w])

    dijkstra(0, N)
    print(f"#{tc} {cost[N]}")
