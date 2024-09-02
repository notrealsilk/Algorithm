import sys
sys.stdin = open("input.txt", "r")


def sudoku1(arr):
    # 스도쿠판 순회하면서 1~9 중복 확인
    for i in range(9):
        # 중복 없는 지 계산
        row = [] # 행
        col = [] # 열
        for j in range(9):
            # 중복 있으면 0 / 행
            if arr[i][j] in row:
                return 0
            # 중복 없으면 n에 해당 숫자 넣고 다음 순회
            row.append(arr[i][j])

            # 중복있으면 0 / 열
            if arr[j][i] in col:
                return 0
            # 중복 없으면 n에 해당 숫자 넣고 다음 순회
            col.append(arr[j][i])
    # 순회 끝남 = 중복 없음
    return 1

def sudoku2(arr):
    """
    3x3 배열에 중복이 없는지 확인
    """

    for row in range(0,9,3):
        for col in range(0,9,3):
            n = []  # 중복 없는 지 계산
            for i in range(3):
                for j in range(3):
                    # 중복 있으면 0
                    if arr[row+i][col+j] in n:
                        return 0
                    # 중복 없으면 n에 해당 숫자 넣고 다음 순회
                    else:
                        n.append(arr[row+i][col+j])
    # 순회 끝남 = 중복 없음
    return 1


def sudoku_valid(arr):
    """
    스도쿠 전체 조건 확인하는 함수
    """
    return sudoku1(arr) and sudoku2(arr)



# T : 테스트 케이스 갯수
T = int(input())
for tc in range(1, T+1):
    # 스도쿠판(9x9)
    arr = [list(map(int,input().split())) for _ in range(9)]
    print(f"#{tc} {sudoku_valid(arr)}")

