# 무방향 인접 행렬
# stack 풀이
from pprint import pprint

"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""

# 정점의 갯수와 간산의 갯수
V, E = map(int, input().split())

# 간선정보
data = list(map(int,input().split()))
print(data) # [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]

def DFS(start):
    stack = [start] # 시작지점
    visited = [0]*(V+1) # 방문 여부를 체크하는 리스트

    # True인 동안 돈다 == False 일 때 까지 돈다
    while stack: # 스택에 값이 있는 동안 반복 (스택이 빌 때 까지 반복)
        current = stack.pop() # 현재 조사할 노드

        # 방문하지 않은 노드라면 (방문 여부 탐색)
        if visited[current] == 0:
            visited[current] = 1 # 방문 표시
            print(current, end=" ") # 방문한 노드 출력

            # 현재 노드에서 갈 수 있는 다음 노드들을 찾아야 함 (찾아서 스택에 넣기)
            # 탐색방향 결정
            for next in range(V, 0, -1):
                # 다음 노드들 중에
                # 1. 현재 노드와 간선으로 연결되어 있는지
                # 2. 방문한 적이 없는지
                if matrix[current][next] == 1 and visited[next] == 0 :
                    stack.append(next)

# 인접행렬 생성 (행렬 그리기)
# 빈 도화지 만들기
matrix = [[0]*(V+1) for _ in range(V+1)]
#pprint(matrix)
"""
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0]]
"""
for i in range(E):
    n1 = data[i*2]
    n2 = data[i*2+1]
    matrix[n1][n2] = 1
    matrix[n2][n1] = 1
#pprint(matrix)
"""
[[0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 1, 1, 0, 0, 0, 0],
 [0, 1, 0, 0, 1, 1, 0, 0],
 [0, 1, 0, 0, 0, 0, 0, 1],
 [0, 0, 1, 0, 0, 0, 1, 0],
 [0, 0, 1, 0, 0, 0, 1, 0],
 [0, 0, 0, 0, 1, 1, 0, 1],
 [0, 0, 0, 1, 0, 0, 1, 0]]
"""

DFS(1) # 1 2 4 6 5 7 3