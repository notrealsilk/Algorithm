#### 인접행렬 DFS ####
# 공식적인 큰 틀

from pprint import pprint

# 노드
node = ['', 'A', 'B','C','D','E','F','G']

"""
노드와 간선 그래프 to 코드로 표현하는 방법
1. 인접 행렬
2. 인접 리스트

## 인접 행렬 (adjacency matrix)
- n x n 크기의 정사각형 행렬
- 노드들 간의 연결 관계를 행렬로 표현한 것
# 대각선을 기준으로 대칭이 되야함

# 인접 행렬을 그릴 때 i ,j = 0, 0 인덱스는 무시해도됨
(1부터 시작하려고 0,0을 무시한 것..)

- 무방향 그래프에서는 
    - 정점 i와 j 사이에 간선이 있다면 matrix[i][j] = matrix[j][i] = 1, 없으면 0
# 행렬은 대칭 구조로 만들어짐
"""

"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

# 그래프 to 인접행렬 정보
#       A  B  C  D  E  F  G
matrix = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0],   # A
    [0, 1, 0, 0, 1, 1, 0, 0],   # B
    [0, 1, 0, 0, 0, 1, 0, 0],   # C
    [0, 0, 1, 0, 0, 0, 1, 0],   # D
    [0, 0, 1, 1, 0, 0, 1, 0],   # E
    [0, 0, 0, 0, 1, 1, 0, 1],   # F
    [0, 0, 0, 0, 0, 0, 1, 0],   # G
]


# 탐색하는함수
def DFS(s,V):
    # 파라미터.. s : 시작정점, V : 엣지(간선)
    # 스택에 시작정점을 push
    stack = [s]  # 스텍에 시작정점 넣고 시작해도됨
    # 방문 여부 체크하는 리스트
    visited = [0] * (V+1)

    # 스택이 빌 때까지 DFS 진행 (스택에 값이 있는 동안 진행)
    while stack: # 스택에 요소가 없을 때까지 반복
        # 현재 조사할 노드
        current = stack.pop()

        # 방문하지 않은 노드라면 / 방문의 기준을 visited로 하기
        if visited[current] == 0: # 방문한 적이 없으면 0
            # 방문표시
            visited[current] = 1 # 여기가 방문했다는 표시!!!!!!!!!!!!!!
            # 방문한 노드가 출력
            print(node[current])

            ## !노드 방향 설정하는 곳!
            # 현재 노드에서 갈 수 있는 다음 노드들을 스택에 추가
            # A>>B로 가야하므로 스택에 C를 넣어야함
            # V ~ 1까지 역순으로 확인 (작은 번호의 노드가 스택의 위쪽으로 위치하게 됨) (A B D F E C G)
            for next in range(V, 0, -1): # V에서 뒤부터 탐색해서 스택에 C >> B 순서로 들어감
            # 큰 번호 우선 탐색을 한다면 (C부터 탐색)
            # for nect in range(1, V+1) # 오른쪽부터 깊이 탐색 (A C E F G D B)

                # 다음 노드가 간선이 연결 + 방문한 적이 없다면(0) 스택에 넣기
                if matrix[current][next] == 1 and visited[next] == 0:
                    # 스택에 push
                    stack.append(next) # 주의.. 스택에 넣은 것 != 방문했다는 표시를 했다



# 인접행렬 만들기
# V = 노드의 개수
# E = 간선의 개수
V, E = map(int, input().split())

adj_matrix = [[0] * (V + 1) for _ in range(V + 1)] # 0번째 인덱스 고려하지 않을려고 V+1

# 노드별 간선 정보
data = list(map(int, input().split())) # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 << 이거 받는 input

# 간선 정보를 넣기
# 간선의 개수만큼 반복하면서 넣기
for i in range(E):
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

pprint(adj_matrix)

DFS(1,7)