"""
1
7 8 #(노드수 /  간선수)
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
1 2 /1 3/ 2 4 /2 5 /4 6 /5 6 /6 7 /3 7
# 2차원 리스트로 인접한 노드의 경로를 저장
"""
# adjl[1] : 1에 인접한 정점
def DFS(s, V) :             # s : 시작 정점 / V : 정점갯수(1번부터 시작인 정점의 마지막 정점)
    visited = [0] * (V+1)   # 방문한 정점을 표시
    stack = []              # 스택생성
    print(s)
    visited[s] = 1          # 시작정점 방문 표시
    v = s                   # v : 현재정점

    while True:
        for w in adjl[v]:   # v에 인접하고, 방문 안한 w가 있으면
            if visited[w] == 0:  # 방문을 안한 곳(0)이라면
                stack.append(v) # push(v) : 현재 정점을 push
                v = w       # w에 방문
                print(v)
                visited[w] = 1 # 1로 방문 표시
                break       # v부터 다시 탐색 (갈림길)
        # 남아있는 갈림길이 없으면
        else:               # 남은 인접 정점이 없어서 break가 걸리지 않은 경우
            if stack: # 이전 갈림길을 스택에서 꺼내서.. / if TOP > -1
                v = stack.pop() # 스택에서 꺼내기
            else: # 되돌아 갈 곳이 없으면, 남은 갈림길이 없으면 탐색종료
                break # While True의 break


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    # adjl :
    adjl = [[] for _ in range(V+1)]
    arr = list(map(int, input().split()))
    for i in range(E): # E개의 쌍을 2개씩 읽기
        v1, v2 = arr[i*2], arr[i*2+1]
        adjl[v1].append(v2)
        adjl[v2].append(v1)

    #print(adjl)
    # [[], [2, 3], [4, 5], [7], [6], [6], [7], []] .. adjl[v1].append(v2)만 있는 경우
    # [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

    DFS(1,V)

# 탐색법
