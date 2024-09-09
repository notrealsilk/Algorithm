# 상, 하, 좌, 우
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 입력 받기
T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    # 활성화할 세포를 저장 (생명력, x좌표, y좌표, 경과 시간)
    activate = []

    # 초기 상태에서 살아있는 세포를 리스트에 추가
    for n in range(N):
        for m in range(M):
            if grid[n][m] > 0:
                activate.append([grid[n][m], n, m, 0])

    # 세포가 있는 위치를 저장할 집합
    cell_set = set()

    # K시간 동안 세포 번식 시뮬레이션
    for k in range(K):
        tmp_activate = []  # 다음 시간을 위한 임시 리스트
        spread_cell_dict = {}  # 번식할 세포 좌표 및 생명력 관리

        # 리스트에서 세포를 하나씩 확인
        while activate:
            life, cx, cy, time_passed = activate.pop()
            cell_set.add((cx, cy))  # 세포의 현재 위치 저장

            # 아직 비활성 상태일 경우
            if time_passed < life:
                tmp_activate.append([life, cx, cy, time_passed + 1])
                continue

            # 활성화 상태인 경우 번식 시작
            if time_passed == life:
                for dx, dy in dxy:
                    nx, ny = cx + dx, cy + dy
                    if (nx, ny) in cell_set:
                        continue
                    spread_cell_dict.setdefault((nx, ny), []).append(life)

            # 활성화 상태에서 유지 중인 경우 (2 * 생명력 시간 동안 유지)
            if time_passed + 1 < 2 * life:
                tmp_activate.append([life, cx, cy, time_passed + 1])

        # tmp_activate 업데이트
        activate = tmp_activate[:]

        # 번식할 좌표에서 가장 생명력 높은 세포를 선택
        for pos, life_list in spread_cell_dict.items():
            activate.append([max(life_list), pos[0], pos[1], 0])

    # 결과 출력: 남은 활성화 및 비활성 상태의 세포 수
    print(f"#{test_case} {len(activate)}")
