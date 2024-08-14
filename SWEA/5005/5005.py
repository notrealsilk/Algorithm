import sys
sys.stdin = open("sample_input (1).txt", "r")

def bfs(i, j, N):
    # 준비
    visited = [[0] * N for _ in range(N)]  # visited 생성
    q = []  # 큐 생성
    q.append([i, j])  # 시작점 인큐
    visited[i][j] = 1  # 시작점 방문 표시

    # 탐색
    while q:
        ti, tj = q.pop(0)  # 디큐
        if maze[ti][tj] == 3:  # 도착 지점에 도달했을 때
            return visited[ti][tj] - 1 - 1 # 경로의 빈 칸 수
            # 시작점이 1이므로 -1 해줌, 지나가는 칸 수 이므로 또 -1

        # 상하좌우 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj

            # 델타 탐색을 하면서 미로크기에 벗어나기 않기, 1은 벽이라서 못가고 0으로만 갈 수 있음
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])  # 인큐
                visited[wi][wj] = visited[ti][tj] + 1  # 인큐 표시

    return 0  # 도착 지점에 도달 못한 경우

# 시작 지점 찾기
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 미로 크기
    maze = [list(map(int, input())) for _ in range(N)] # 실제 미로

    sti, stj = find_start(N) # 미로 시작점 찾기

    print(f"#{tc} {bfs(sti, stj, N)}") # 지나야하는 최소한의 칸 수 출력하는 함수
