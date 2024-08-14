import sys

sys.stdin = open('input.txt')

"""
라이브 강의 진행 코드 (인접 리스트)
"""


def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    # 준비
    visited = [0] * (V + 1)  # visited 생성
    q = []  # 큐 생성 # 아직 지나가지 않은 노드를 q에 넣음
    # # 아래 두 과정 하나로 합칠 수도 ㅇ
    q.append(s)  # 시작점 인큐
    visited[s] = 1  # 시작점 방문표시

    # 탐색 진행
    while q:  # 큐에 정점이 남아있으면 front != rear / 즉, 큐가 비어있지않으면
        t = q.pop(0)  # 디큐
        print(t)  # 방문한 정점에서 할일

        # t의 인접이고, 인큐된 적 없으면 인큐하고 인큐 표시
        for w in adj_l[t]:  # 인접한 정점 중 인큐되지 않은 정점 w가 있으면
            if visited[w] == 0:
                q.append(w)  # w인큐, 인큐되었음을 표시
                visited[w] = visited[t] + 1 # 간선 수를 구할 때 visited의 차로 구할 수 ㅇ


V, E= map(int, input().split())  # 1번부터 V번 노드(정점), E개의 간선
arr = list(map(int, input().split()))
print(arr)
# 인접리스트 -------------------------
adj_l = [[] for _ in range(V + 1)] # 1번부터 시작하므로 1번 인덱스부터 시작, 0번 인덱스는 무시..그래서 +1해줌
# [[], [2, 3]..노드1의 인접 노드, [1, 4, 5]..노드2의 인접, [1, 7]..노드3의 인접, [2, 6], [2, 6], [4, 5, 7], [6, 3]]

# for i in range(0, E*2, 2):
#     v1, v2 = arr[i], arr[i+1]
#     adj_l[v1].append(v2)
#     adj_l[v2].append(v1)  # 방향이 없는 경우
#     print(adj_l)
for i in range(E):
    v1, v2 = arr[i * 2], arr[i * 2 + 1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)  # 방향이 없는 경우
# 여기까지 인접리스트 -----------------
bfs(1, V)

####################################################################################

"""
라이브 강의 진행 코드 (인접행렬)
"""
# def bfs(s, V):  # 시작정점 s, 마지막 정점 V
        # 준비
#     visited = [0] * (V + 1)  # visited 생성 / n : 정점의 갯수+방문기록 만큼 생성  Visited 배열 초기화
#     q = []  # 큐 생성

#    q.append(s)  # 시작점 인큐(enqueue)
#     visited[s] = 1  # 시작점 방문표시

        # 탐색 진행
#     while q:  # 큐가 비어있지 않은 동안 반복
#         t = q.pop(0)  # 디큐 # 큐의 첫번째 원소 반환 / 방문할 노드 = 처리할 노드
#         print(t)  # 방문한 정점 출력
#         for w in range(1, V + 1):  # 모든 노드에 대해
#             # 현재 노드와 연결되어 있고, 아직 방문하지 않은 노드라면
#             if adj_m[t][w] == 1 and visited[w] == 0:
#                 q.append(w)  # w 인큐, 인큐 되었음을 표시
#                 visited[w] = visited[t] + 1 # n으로부터 1만큼 이동
#     # print(visited)


# V, E = map(int, input().split())  # 1번부터 V번 정점, E개의 간선
# arr = list(map(int, input().split()))  # 간성 정보

# # 인접행렬
# adj_m = [[0] * (V + 1) for _ in range(V + 1)]

# for i in range(E):
#     v1, v2 = arr[i * 2], arr[i * 2 + 1]
#     adj_m[v1][v2] = 1
#     adj_m[v2][v1] = 1  # 방향이 없는 경우

# bfs(1, V)
