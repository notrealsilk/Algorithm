import sys
sys.stdin = open("input.txt", "r")

def bfs(N):
    # 준비
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q = []  # 큐 생성        /// 케이스1의 경우, (1,5)을 기준으로 인접 인덱스 [1,6], [2,5]
    i, j = 1, 1 # 시작 좌표 (1,1)
    q.append([i,j])  # 시작점 인큐
    visited[i][j] = 1  # 시작점 방문 표시

    # 탐색
    while q: # q가 빌 때까지 반복
        ti, tj = q.pop(0)  # 디큐
        if maze[ti][tj] == 3:  # 도착 지점에 도달했을 때
            return 1

        # q에서 나온 좌표가 어느 쪽으로 갈 수 있는 지 델타 탐색을 하고, q좌표와 인접하면서 갈 수 있는 좌표를 찾으면 인큐
        # 상하좌우 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj

            # 델타 탐색을 하면서 미로크기에 벗어나기 않기, 1은 벽이라서 못가고 0으로만 갈 수 있음
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])  # 인큐
                # (출발~ 도착지까지 도달하는 최소한의 칸 수+ 도착지 도달 여부 알 수 있음)
                # visited[wi][wj] = visited[ti][tj] + 1  # 인큐 표시
                visited[wi][wj] = 1 # 방문한 길에 1 표시 (도착지에 도달하는 지만 확인 할 수 있음)

    return 0  # 도착 지점에 도달 못한 경우

# 테스트 케이스 10개
for _ in range(10):
    tc = int(input())
    # 미로 크기
    N = 16
    maze = [list(map(int, input())) for _ in range(N)] # 실제 미로

    print(f"#{tc} {bfs(N)}")
