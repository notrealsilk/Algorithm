import sys
sys.stdin = open("sample_input(1).txt", "r")

# 테스트 케이스 입력
T = int(input())
for tc in range(1,T+1):
    # N : 배열 크기 / M : 돌을 놓는 횟수
    N,M = map(int,input().split())

    ## 보드 만들기
    board = [[0]*N for _ in range(N)]
    # 보드 안에 초기 돌 배치
    # 흑(B)(1) , 백(W)(2)
    board[(N//2)-1][(N//2)-1] = 2
    board[(N//2)-1][N//2] = 1
    board[N//2][(N//2)-1] = 1
    board[N//2][N//2] = 2

    # 델타 탐색 (상하좌우 + 4대각선)
    dx = [-1,1,0,0, -1,1,-1,1]
    dy = [0,0,-1,1, -1,1,1,-1]

    # 게임 결과, 두 돌의 최종 갯수 카운트
    B_cnt = 0
    W_cnt = 0

    # 게임시작 ("1"부터)
    for k in range(M):
        #i:행, j:열, rock: 흑(B)(1) or 백(W)(2)
        i, j, rock = map(int, input().split())
        i , j = i-1, j-1 # (i,j)는 인덱스 1이 기준이고, 보드판은 인덱스 0이 기준이므로 보드 기준으로 맞춰주기

        ## 게임 규칙에 따라 입력받은 좌표(i,j)에 돌을 놓을 수 있는지 판단
        # 1. [i][j] 좌표가 빈 공간 인지 판단
        if board[i][j] == 0:
        # 2. 델타 탐색해서 인접한 곳에 상대편 돌 있는 지 확인
            for l in range(8):
                nx = j + dx[l]
                ny = i + dy[l]
                # 흑(1) 일 경우
                if 0 <= nx < N and 0 <= ny < N and board[ny][nx] == 2:  # 존재하는 공간인 지 + 상대편 돌이 있는 지 확인
        # 3. 인접한 곳에 상대편 돌이 있다면 마주보는 곳에 내 돌이 있는 지 확인
                    # 상대편 돌을 기준으로 인접한 곳에 내 돌이 있는 지 델타탐색
                    for m in range(8):
                        nx_2 = nx + dx[m]
                        ny_2 = ny + dy[m]
                        if 0 <= nx_2 < N and 0 <= ny_2 < N and board[ny_2][nx_2] == 1: # 존재하는 공간인 지 + 내 돌이 있는 지 확인
                            # 보드에 있는 내 돌[ny_2][nx_2] - 상대편 돌[ny][nx] - 내 돌을 놀 예정인 곳[i][j]이 일직선인 지 확인
                            if  ((board[ny][nx-1] == board[ny_2][nx_2] and board[ny][nx+1] == board[i][j]) or
                                (board[ny][nx+1] == board[ny_2][nx_2] and board[ny][nx-1] == board[i][j]) or
                                (board[ny-1][nx] == board[ny_2][nx_2] and board[ny+1][nx] == board[i][j]) or
                                (board[ny+1][nx] == board[ny_2][nx_2] and board[ny-1][nx] == board[i][j]) or
                                    (board[ny-1][nx-1] == board[ny_2][nx_2] and board[ny+1][nx+1] == board[i][j]) or
                                    (board[ny+1][nx+1] == board[ny_2][nx_2] and board[ny-1][nx-1] == board[i][j]) or
                                    (board[ny-1][nx+1] == board[ny_2][nx_2] and board[ny+1][nx-1] == board[i][j]) or
                                    (board[ny+1][nx-1] == board[ny_2][nx_2] and board[ny-1][nx+1] == board[i][j])):
                                board[i][j] = 1 # 드디어 여기서 돌을 놈..
                                board[ny][nx] = 1 # 내 돌 사이에 있는 상대편 돌도 내 돌로 만들기

                # 백(2) 일 경우
                elif 0 <= nx < N and 0 <= ny < N and rock == 1: # 존재하는 공간인 지 + 상대편 돌이 있는 지 확인
                    # 상대편 돌을 기준으로 인접한 곳에 내 돌이 있는 지 델타탐색
                    for m in range(8):
                        nx_2 = nx + dx[m]
                        ny_2 = ny + dy[m]
                        if 0 <= nx_2 < N and 0 <= ny_2 < N and board[ny_2][nx_2] == 2:  # 존재하는 공간인 지 + 내 돌이 있는 지 확인
                            # 보드에 있는 내 돌[ny_2][nx_2] - 상대편 돌[ny][nx] - 내 돌을 놀 예정인 곳[i][j]이 일직선인 지 확인
                            if ((board[ny][nx - 1] == board[ny_2][nx_2] and board[ny][nx + 1] == board[i][j]) or
                                    (board[ny][nx + 1] == board[ny_2][nx_2] and board[ny][nx - 1] == board[i][j]) or
                                    (board[ny - 1][nx] == board[ny_2][nx_2] and board[ny + 1][nx] == board[i][j]) or
                                    (board[ny + 1][nx] == board[ny_2][nx_2] and board[ny - 1][nx] == board[i][j])or
                                    (board[ny-1][nx-1] == board[ny_2][nx_2] and board[ny+1][nx+1] == board[i][j]) or
                                    (board[ny+1][nx+1] == board[ny_2][nx_2] and board[ny-1][nx-1] == board[i][j]) or
                                    (board[ny-1][nx+1] == board[ny_2][nx_2] and board[ny+1][nx-1] == board[i][j]) or
                                    (board[ny+1][nx-1] == board[ny_2][nx_2] and board[ny-1][nx+1] == board[i][j])):
                                board[i][j] = 2  # 드디어 여기서 돌을 놈..
                                board[ny][nx] = 2  # 내 돌 사이에 있는 상대편 돌도 내 돌로 만들기
        else :
            continue

    ## 게임이 끝나면, 보드를 순회하면서 흑,백 돌 갯수 세기
    for x in range(N):
        for y in range(N):
            if board[x][y] == 1:    # 흑
                B_cnt +=1
            elif board[x][y] == 2:  # 백
                W_cnt += 1

    ## 드디어.. 테스트 케이스 결과 출력
    print(f"#{tc} {B_cnt} {W_cnt}")