def bfs (i,j,N):
    # 준비
    visited = [[0]*N for _ in range(N)]# visited 생성
    q = []          # 큐 생성
    q.append([i,j]) # 시작점 인큐
    visited[i][j]   # 시작점 인큐 표시

    # 탐색
    while q :
        ti, tj = q.pop(0) # 디큐
        if maze[ti][tj] == 3: # visir(t)
            return maze[ti][tj] - 1 - 1 # 경로의 빈 칸 수, -1 추가
        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 미로 내부고, 인접이 벽이 아니면
            wi, wj = ti+di, tj+dj

            if 0 <= wi < N and 0<= wj < N and maze[ti][tj] !=1 and visited[wi][wj] == 0:
                q.append([wi,wj])# 인큐
                visited[wi][wj] = visited[ti][tj] + 1 # 인큐 표시
    return 0 # 디버깅 용

# 시작 지점 찾기
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze [i][j]==2:
                return i,j

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    sti, stj = find_start(N)
    ans = bfs(sti,stj,N)

    print(f"#{tc} {ans}")