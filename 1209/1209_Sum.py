from pprint import pprint

import sys
sys.stdin = open("input.txt", "r")

########################################

# 1. 테스트 케이스 입력(input())
for i in range(10):
    tc = int(input())
# 2. 해당 테스트 케이스의 2차원 배열의 각 행 값 입력(input()) > 입력해서 list로 변환
    # 2-1. 입력받은 값을 1차원 리스트를 2차원 리스트(100x100크기의 arr)로 만들기
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
    ## 1차원 리스트를 2차원 리스트로 만듦

    # for test_case in range(1, T + 1):
    #     tc = int(input())
    #     N = 100
    #     numbers = [list(map(int, input().split())) for _ in range(N)]  # 100 X 100 행렬


# 3. 각 행, 열, 대각선1, 대각선2와 같이 4가지 경우로 나누고, 각 경우의 최댓값 구하기

    # 3-1. 행 (row)
    max_row = 0 # 행의 최댓값

    for i in range(100):
        # 현재 for문을 순회하는 행의 합을 저장하는 sum_row을 초기화
        sum_row = 0
        for j in range(100):
            sum_row += arr[i][j]
        # 만약, 현재 행(sum_row)의 합이 행의 최댓값(max_row)보다 크면 max_row 갱신
        if sum_row > max_row :
            max_row = sum_row
    #print(max_row)

    # 3-2. 열 (col)
    max_col = 0 # 열의 최댓값

    for i in range(100):
        # 현재 for문을 순회하는 행의 합을 저장하는 sum_col을 초기화
        sum_col = 0
        for j in range(100):
            sum_col += arr[j][i]
        # 만약, 현재 열(sum_col)의 합이 열의 최댓값(max_col)보다 크면 max_col 갱신
        if sum_col > max_col:
            max_col = sum_col
    #print(max_col)

    # 3-3. 대각선1 (diag1)
    # 대각선1의 인덱스는 [0][0] > [1][1] > [2][2]... 씩 변화 // arr[i+1][j+1]

    # 시작 인덱스
    row = 0
    col = 0
    # 대각선1의 최댓값 저장
    max_diag1 = 0

    for i in range(100):
        max_diag1 += arr[row+i][col+i]
    #print(max_diag1)


    # 3-4. 대각선2 (diag_2)
    # 대각선2의 인덱스는 [0][99] > [1][98] > [2][97]...씩 변화 // arr[i+1][j-1]

    # 시작 인덱스
    row = 0
    col = 99
    # 대각선2의 최댓값 저장
    max_diag2 = 0

    for i in range(100):
        max_diag2 += arr[row+i][col-i]
    #print(max_diag2)

# 4. 행, 열, 대각선1, 대각선2의 최댓값을 비교해서 4가지 경우 중 최댓값을 구하기
    max_result = 0 # 구하고자 하는 최댓값

    max_list = [max_row, max_col, max_diag1, max_diag2]
    for i in max_list:
        if i > max_result:
            max_result = i

# 5. 출력
    print(f"#{tc} {max_result}")