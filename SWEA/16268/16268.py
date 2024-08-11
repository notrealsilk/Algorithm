# 풍선팡

import sys
sys.stdin = open("input1.txt", "r")

T = int(input())  # 테스트 케이스 수 입력

for tc in range(1, T + 1):  # 각 테스트 케이스에 대해 반복
    # N M : 퍼즐판의 크기 (N x M)
    N, M = map(int, input().split())
    # 퍼즐판 배열을 2차원 리스트로 입력 받음
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 방향 벡터 설정 (상, 하, 좌, 우)
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    max_ball = 0  # 최대 풍선 수 초기화

    # 퍼즐판의 각 위치를 순회
    for y in range(N): # 세로 (행)
        for x in range(M): # 가로 (열)
            cur_ball = arr[y][x]  # 현재 위치의 풍선 수

            # 각 4방향에 대해 탐색
            for dir in range(4):
                new_x = x + dx[dir]  # 새로운 x 위치 (행 변화)
                new_y = y + dy[dir]  # 새로운 y 위치 (열 변화)
                # 퍼즐판의 범위를 벗어나지 않는 경우 (배열범위)
                if 0 <= new_x < M and 0 <= new_y < N:
                    cur_ball += arr[new_y][new_x]  # 이웃한 위치의 풍선 수 더하기

            # 최대 풍선 수 갱신
            if max_ball <= cur_ball:
                max_ball = cur_ball

    # 테스트 케이스 번호와 최대 풍선 수 출력
    print(f"#{tc} {max_ball}")
