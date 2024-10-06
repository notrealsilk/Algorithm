import sys
sys.stdin=open('sample_input.txt','r')

def simulation(p, d, k, c, visited):
    global N, target, cmd

    # 가지치기: 현재까지 이동 횟수가 최소 조종 횟수 이상일 경우 중단
    if c >= cmd:
        return

    # 목표 지점에 도착한 경우 최소 조종 횟수 갱신
    if p == target:
        cmd = min(cmd, c)
        return

    # 현재 위치 방문 처리
    visited[p[0]][p[1]] = True

    # 4방향 탐색
    for i in range(4):
        new_dir = (d + i) % 4  # 새로운 방향 (시계방향으로 회전)
        new_pos = (p[0] + dir[new_dir][0], p[1] + dir[new_dir][1])  # 새로운 좌표

        # 맵 범위 내에 있고, 방문하지 않은 위치만 탐색
        if 0 <= new_pos[0] < N and 0 <= new_pos[1] < N and not visited[new_pos[0]][new_pos[1]]:
            # 방향 전환이 있을 때는 추가로 조작 횟수가 증가해야 함
            extra_cost = 1 if i != 0 else 0

            # 땅('G')일 경우
            if field[new_pos[0]][new_pos[1]] == 'G':
                simulation(new_pos, new_dir, k, c + 1 + extra_cost, visited)  # 조작 횟수 증가 후 재귀 호출
            # 나무('T')를 벨 수 있는 경우
            elif field[new_pos[0]][new_pos[1]] == 'T' and k > 0:
                simulation(new_pos, new_dir, k - 1, c + 1 + extra_cost, visited)  # 나무를 벤 후 재귀 호출

    # 현재 위치 방문 해제 (다른 경로에서 탐색 가능하게)
    visited[p[0]][p[1]] = False


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())  # N: 필드 크기, K: 나무 벨 수 있는 횟수
    field = [input().strip() for _ in range(N)]

    # 방향 좌표: 상(0), 우(1), 하(2), 좌(3)
    dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 초기 설정
    position = (0, 0)  # 현재 위치 (X의 위치)
    direction = 0  # 초기 방향 (상)
    target = (0, 0)  # 목표 위치 (Y의 위치)

    # X와 Y의 위치 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                position = (i, j)
            elif field[i][j] == 'Y':
                target = (i, j)
        if position != (0, 0) and target != (0, 0):  # X와 Y를 모두 찾으면 중단
            break

    # 시작 지점과 목표 지점이 같은 경우 바로 0을 출력
    if position == target:
        print(f'#{tc} 0')
        continue

    cmd = float('inf')  # 최소 조종 횟수 (무한대로 초기화)
    visited = [[False] * N for _ in range(N)]  # 방문 여부 리스트

    simulation(position, direction, K, 0, visited)  # 최소 조종 횟수 계산

    # cmd가 갱신되지 않았으면 도착할 수 없다는 뜻이므로 -1 출력
    if cmd == float('inf'):
        cmd = -1

    print(f'#{tc} {cmd}')
