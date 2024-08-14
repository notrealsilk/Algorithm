import sys
sys.stdin = open("input.txt", "r")

def deg_90(N,N_list):
    deg_90 = [[0]*N for _ in range(N)]

    for i in range(N): # 행
        for j in range(N):
            deg_90[i][j] = N_list[N-1-j][i]
    return deg_90

def deg_180(N,N_list):
    deg_180 = [[0] * N for _ in range(N)]
    for i in range(N): # 행
        for j in range(N):
            deg_180[i][j] = N_list[N-1-i][N-1-j]
    return deg_180

def deg_270(N,N_list):
    deg_270 = [[0]*N for _ in range(N)]

    for i in range(N): # 행
        for j in range(N):
            deg_270[i][j] = N_list[j][N-1-i]
    return deg_270



T = int(input())

for tc in range(1, T+1):
    # N 크기 입력
    N = int(input())
    # 2차원 리스트로 입력 받기
    N_list = [list(map(int, input().split())) for _ in range(N)]

    # 각도별 회전한 모양
    # 2차원 리스트로 값을 갱신하고 최종값은 연속해서 출력
    matrix_90, matrix_180, matrix_270 = deg_90(N,N_list),deg_180(N,N_list),deg_270(N,N_list)

    print(f"#{tc}")
    for i in range(N):
        row_90 = ''.join(map(str, matrix_90[i]))
        row_180 = ''.join(map(str, matrix_180[i]))
        row_270 = ''.join(map(str, matrix_270[i]))
        print(f"{row_90} {row_180} {row_270}")