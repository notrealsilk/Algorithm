import sys
sys.stdin = open("sample_input.txt", "r")

# 상, 하, 좌, 우
dxy = [[-1, 0], [1, 0], [0, -1], [0, 1]]


# 배양판 크기 확장 함수
def extended_matrix(matrix, N, M, K):
    ex_N = N + (2 * K) # 세로
    ex_M = M + (2 * K) # 가로
    ex_matrix = [[0] * ex_M for _ in range(ex_N)]

    # 초기 배양판을 확장된 배양판 중앙에 배치
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                ex_matrix[K + i][K + j] = (matrix[i][j], matrix[i][j])  # (생명력, 비활성 시간)
    return ex_matrix


# 세포 배양 시뮬레이션 함수
def simulate_cells(matrix, N, M, K):
    active_cells = []
    cell_set = set()  # 세포가 존재하는 위치 기록

    # 초기 활성 세포 리스트 생성
    for i in range(N + 2 * K):
        for j in range(M + 2 * K):
            if matrix[i][j] and isinstance(matrix[i][j], tuple):  # 세포가 존재하면
                life, _ = matrix[i][j]  # 생명력 참조
                active_cells.append([life, i, j, 0])  # (생명력, 좌표, 경과시간)

    # K 시간 동안 시뮬레이션
    for _ in range(K):
        new_cells = []
        cell_growth = {}

        while active_cells:
            life, x, y, time_passed = active_cells.pop()
            cell_set.add((x, y))  # 현재 위치 기록

            # 비활성화 상태일 때
            if time_passed < life:
                new_cells.append([life, x, y, time_passed + 1])
            # 활성화 상태일 때
            elif time_passed == life:
                # 상하좌우로 번식
                for dx, dy in dxy:
                    nx, ny = x + dx, y + dy
                    if (nx, ny) not in cell_set:  # 세포가 없는 곳에 번식
                        # 이미 번식된 셀이 있으면 생명력 비교
                        if (nx, ny) not in cell_growth:
                            cell_growth[(nx, ny)] = life
                        else:
                            # 생명력이 큰 세포만 번식
                            cell_growth[(nx, ny)] = max(cell_growth[(nx, ny)], life)

            # 세포가 생명력의 2배 동안 유지됨
            if time_passed + 1 < 2 * life:
                new_cells.append([life, x, y, time_passed + 1])

        # 새로운 세포를 번식 위치에 추가
        for (nx, ny), life in cell_growth.items():
            if (nx, ny) not in cell_set:  # 이미 존재하는 세포가 아니면
                new_cells.append([life, nx, ny, 0])
                cell_set.add((nx, ny))  # 새로 번식된 위치도 기록

        active_cells = new_cells

    return len(active_cells)

# 입력 처리 및 결과 출력
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # 세로 크기, 가로 크기, 시간 K
    matrix = [list(map(int, input().split())) for _ in range(N)]

    plate = extended_matrix(matrix, N, M, K) # 배양판 확장
    result = simulate_cells(plate, N, M, K) # 줄기세포배양 시작

    # 결과 출력
    print(f"#{tc} {result}")
