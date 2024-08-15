import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 판의 크기
    arr = [input() for _ in range(N)]

    result = "NO"

    # 가로
    for i in range(N):
        for j in range(N - 4):  # 5개 연속 체크할 공간이 있어야 하므로
            if (arr[i][j] == 'o' and
                arr[i][j + 1] == 'o' and
                arr[i][j + 2] == 'o' and
                arr[i][j + 3] == 'o' and
                arr[i][j + 4] == 'o'):
                result = "YES"
                break
        if result == "YES":
            break

    # 세로
    if result == "NO":  # 가로에서 이미 찾은 경우, 세로는 체크하지 않음
        for j in range(N):
            for i in range(N - 4):  # 5개 연속 체크할 공간이 있어야 하므로
                if (arr[i][j] == 'o' and
                    arr[i + 1][j] == 'o' and
                    arr[i + 2][j] == 'o' and
                    arr[i + 3][j] == 'o' and
                    arr[i + 4][j] == 'o'):
                    result = "YES"
                    break
            if result == "YES":
                break

    # 대각선1
    if result == "NO":  # 가로 또는 세로에서 이미 찾은 경우, 대각선은 체크하지 않음
        for i in range(N - 4):
            for j in range(N - 4):  # 5개 연속 체크할 공간이 있어야 하므로
                if (arr[i][j] == 'o' and
                    arr[i + 1][j + 1] == 'o' and
                    arr[i + 2][j + 2] == 'o' and
                    arr[i + 3][j + 3] == 'o' and
                    arr[i + 4][j + 4] == 'o'):
                    result = "YES"
                    break
            if result == "YES":
                break

    # 대각선2
    if result == "NO":  # 가로, 세로 또는 대각선1에서 이미 찾은 경우, 대각선2는 체크하지 않음
        for i in range(N - 4):
            for j in range(4, N):  # 5개 연속 체크할 공간이 있어야 하므로
                if (arr[i][j] == 'o' and
                    arr[i + 1][j - 1] == 'o' and
                    arr[i + 2][j - 2] == 'o' and
                    arr[i + 3][j - 3] == 'o' and
                    arr[i + 4][j - 4] == 'o'):
                    result = "YES"
                    break
            if result == "YES":
                break

    print(f"#{tc} {result}")
