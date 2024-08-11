import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # N 크기 입력
    N = int(input())
    # 2차원 리스트로 입력 받기
    N_list = [list(map(int, input().split())) for _ in range(N)]

    # 각도별 회전한 모양
    # 2차원 리스트로 값을 갱신하고 최종값은 연속해서 출력
    deg_90, deg_180, deg_270 = [],[],[]
    #print(N_list)



    """
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 각 행을 문자열로 변환하여 출력
for row in matrix:
    # 행의 각 요소를 문자열로 변환하고, 이를 join()으로 연결
    print(''.join(map(str, row)))

    """