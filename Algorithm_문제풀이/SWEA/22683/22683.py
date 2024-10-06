# import sys
# sys.stdin=open('sample_input.txt','r')

# rc카 최소 조종 횟수 = 반환값
def simulation(p, d, k, c, visited):  # 방문 표시를 함수에 전달
    global N, target, cmd

    # 가지치기
    if c >= cmd:  # 이미 최소 조종횟수보다 많다면
        return

    # 목표 지점 도착했다면 최소 조종횟수인지 체크
    if p == target:
        cmd = min(cmd, c)  # 최소 조종 횟수 갱신
        return

    # 현재 위치 방문 표시
    visited[p[0]][p[1]] = True

    # 4방향 탐색
    for i in range(4):
        new_dir = (d + i) % 4
        new_pos = (p[0] + dir[new_dir][0], p[1] + dir[new_dir][1])

        # 맵을 벗어나지 않으면서 방문하지 않은 곳만 탐색
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N and not visited[new_pos[0]][new_pos[1]]:
            if field[new_pos[0]][new_pos[1]] == 'G':  # 땅이라면
                simulation(new_pos, new_dir, k, c + 1, visited)  # 조작 횟수 증가 후 재귀 호출
            elif field[new_pos[0]][new_pos[1]] == 'T' and k > 0:  # 나무가 있고 벨 수 있는 경우
                simulation(new_pos, new_dir, k - 1, c + 1, visited)  # 나무를 베고, 나무 횟수 감소 후 재귀 호출

    # 현재 위치 방문 표시 해제 (다른 경로에서 탐색 가능하도록)
    visited[p[0]][p[1]] = False


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N:필드의 크기 / K:나무 벨 수 있는 횟수
    field = [input().strip() for _ in range(N)]

    # 방향 좌표
    # 상(0) 우(1) 하(2) 좌(3)
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 초기 설정
    position = (0, 0)  # 현재 위치 = X
    direction = 0  # 초기 방향 -> 상(0)
    target = (0, 0)  # 목표 위치 = Y

    # rc카 초기 설정 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                position = (i, j)
            elif field[i][j] == 'Y':
                target = (i, j)
        if position != (0, 0) and target != (0,0): # X,Y 값 다 찾았으면 멈추기
            break

    cmd = float('inf')  # 최소 조종 횟수 (최종결과)
    visited = [[False] * N for _ in range(N)]  # 방문 여부 리스트

    simulation(position, direction, K, 0, visited)  # 최소 조종 횟수 계산
    if cmd == float('inf'):
        cmd = -1

    print(f'#{tc} {cmd}')
