import sys
sys.stdin = open("sample_input.txt","r")

# 배양판 크기 확장 함수
def extended_matrix(matrix, N, M, K):
    ex_N = N + (2 * K)
    ex_M = M + (2 * K)
    ex_matrix = [[0] * ex_M for _ in range(ex_N)]

    # 초기 배양판을 확장된 배양판 중앙에 배치
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                ex_matrix[K + i][K + j] = (matrix[i][j], matrix[i][j])  # (생명력, 비활성 시간)
    return ex_matrix


# 줄기세포 배양하는 함수
def simulation(plate, N, M, K):
    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # K시간 동안 배양 시작
    for _ in range(K):
        cur_plate = [row[:] for row in plate]  # 현재 plate 상태(+1시간 될 때마다 갱신)

        # 분열할 세포를 저장할 리스트
        new_cells = []

        # plate 탐색
        for i in range(N + 2 * K):
            for j in range(M + 2 * K):
                if plate[i][j]:  # 세포가 있으면
                    life, state_time = plate[i][j]

                    # 비활성 상태에서 시간이 지나서 활성화로 변할 때
                    if state_time > 0:
                        cur_plate[i][j] = (life, state_time - 1)
                    elif state_time == 0:  # 활성화 시작
                        cur_plate[i][j] = (life, -1)  # 활성화 상태로 전환
                        # 번식 시작 (델타 탐색)
                        for d in directions:
                            ni, nj = i + d[0], j + d[1]
                            if 0 <= ni < N + 2 * K and 0 <= nj < M + 2 * K:
                                if not cur_plate[ni][nj]:  # 번식할 위치가 비어 있으면
                                    new_cells.append((ni, nj, life))

                    # 활성화된 세포가 (2 * 생명력 시간) 동안 유지되므로 상태 갱신
                    if state_time < 0 and abs(state_time) < 2 * life:
                        cur_plate[i][j] = (life, state_time - 1)

        # 번식할 세포 추가 (번식 위치 중 가장 높은 생명력 가진 세포만 번식)
        for ni, nj, life in new_cells:
            if not cur_plate[ni][nj] or cur_plate[ni][nj][0] < life:
                cur_plate[ni][nj] = (life, life)  # 새로 번식한 세포는 비활성화 상태로 시작

        plate = cur_plate  # 업데이트된 상태로 갱신

    # 살아있는 세포의 수 계산 (비활성 상태 + 활성 상태)
    alive_count = sum(1 for row in plate for cell in row if cell and cell[1] >= -2 * cell[0])

    return alive_count


# 테스트케이스 처리
T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())  # 세로 크기 N, 가로 크기 M, 배양 시간 K
    init_plate = [list(map(int, input().split())) for _ in range(N)]  # 초기 배양판

    # 배양판 크기 늘리기 (세포가 배양되면서 크기가 커지므로, 최대로 커질 수 있는 크기까지 확장)
    plate = extended_matrix(init_plate, N, M, K)
    # 줄기세포 배양 시작
    result = simulation(plate, N, M, K)
    print(f"#{tc} {result}")
