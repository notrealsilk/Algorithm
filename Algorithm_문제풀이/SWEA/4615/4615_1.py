import sys
sys.stdin = open("sample_input(1).txt", "r")

# 테스트 케이스 입력
T = int(input())
for tc in range(1, T + 1):
    # N : 배열 크기 / M : 돌을 놓는 횟수
    N, M = map(int, input().split())

    # 보드 만들기
    board = [[0] * N for _ in range(N)]
    # 보드 안에 초기 돌 배치
    # 흑(B)(1), 백(W)(2)
    board[(N // 2) - 1][(N // 2) - 1] = 2
    board[(N // 2) - 1][N // 2] = 1
    board[N // 2][(N // 2) - 1] = 1
    board[N // 2][N // 2] = 2

    # 방향 탐색 (상하좌우 + 4대각선)
    dx = [-1, 1, 0, 0, -1, 1, -1, 1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]

    # 게임 결과, 두 돌의 최종 개수 카운트
    B_cnt = 0
    W_cnt = 0

    # 게임 시작 ("1"부터)
    for k in range(M):
        # i:행, j:열, rock: 흑(B)(1) or 백(W)(2)
        i, j, rock = map(int, input().split())
        i, j = i - 1, j - 1  # (i,j)는 인덱스 1이 기준이고, 보드판은 인덱스 0이 기준이므로 보드 기준으로 맞춰주기

        ## 게임 규칙에 따라 입력받은 좌표(i,j)에 돌을 놓을 수 있는지 판단
        # 1. [i][j] 좌표가 빈 공간 인지 판단
        if board[i][j] == 0:
        # 2. 방향 탐색해서 인접한 곳에 상대편 돌 있는 지 확인
            for l in range(8):
                nx = j + dx[l]
                ny = i + dy[l]

                # 3. 인접한 곳에 상대편 돌이 있는지 확인
                # 존재하는 공간인 지 + 상대방 돌이 있는 지 확인
                if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == (3 - rock):
                # 4. 상대편 돌을 기준으로 인접한 곳에 내 돌이 있는 지 방향 탐색
                # 내 돌이 있다면 돌을 놓고 (내 돌) ~ (현재 턴에서 논 돌) 사이에 있는 상대편 돌을 뒤집기
                    to_flip = [] # 뒤집을 돌의 좌표 임시 저장
                    while 0 <= nx < N and 0 <= ny < N: # 존재하는 공간이라면 작동
                        if board[ny][nx] == 0:  # 빈 공간이면 중단
                            break
                        if board[ny][nx] == rock:  # 내 돌을 만났다면
                            # 사이에 있는 상대 돌을 모두 뒤집음
                            for fx, fy in to_flip:
                                board[fy][fx] = rock
                            board[i][j] = rock  # 드디어.. 내 돌 놓기
                            break
                        # (nx, ny)에 상대편 돌이 있음..to_flip에 좌표 저장하고 내 돌 찾으러 go
                        to_flip.append((nx, ny))
                        # 같은 방향으로 한 칸 더 가서 계속 탐색
                        nx += dx[l]
                        ny += dy[l]

    # 게임이 끝나면, 보드를 순회하면서 흑, 백 돌 개수 세기
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:  # 흑
                B_cnt += 1
            elif board[x][y] == 2:  # 백
                W_cnt += 1

    print(f"#{tc} {B_cnt} {W_cnt}")
