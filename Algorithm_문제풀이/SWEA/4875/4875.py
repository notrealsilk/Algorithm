import sys
sys.stdin = open("sample_input (1).txt", "r")

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
"""
델타의 또 다른 방법
for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
"""

def search(x,y):
    # 튜플로 첫번째 방문할 곳을 담음
    stack = [(x,y)] # 튜플을 사용해서 변경안한다는 뜻
    visited[x][y] = 1
    # 언제까지 탐색 할 건가요?
    while stack:
        x,y = stack.pop()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            # 미로의 범위를 벗어나지 않는지 && 이미 방문한 곳이 아니라면
            if 0 <= nx < N and 0<= ny < N and maze[nx][ny] != 1 and visited[nx][ny] != 1:
                # 다음 방문 위치가 3인지 확인
                if maze[nx][ny] == 3: # 다음 위치가 출구
                    return 1 # 1 반환 후 함수 종료
                # 3이 아니라면
                stack.append((nx,ny)) # 다음으로 갈 곳의 좌표를 튜플의 형태로 묶어서 추가
                visited[nx][ny] = 1 # 방문 처리

    return 0 # while문이 끝났을 때도 1이 반환 안됐다면 방문 위치를 찾지 못했다는 것

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # 2가 담긴 곳 == 출발점
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                print(f"#{tc} {(search(i, j))}")