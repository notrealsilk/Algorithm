import sys
sys.stdin = open("sample_input.txt", "r")

# T : 테스트 케이스 갯수
T = int(input())
for tc in range(1, T+1):
    # N : 칠할 영역 수
    N = int(input())
    # 색칠할 공간
    arr = [[0]*10 for _ in range(10)]

    # 좌표와 펜 색깔 입력 (5개)
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                # 색칠 시작 (빨강)
                if color == 1:
                    # 색이 안 칠해져있거나(0), 다른 색(=파랑)이 있는 경우(2)
                    if arr[i][j] == 0 or arr[i][j] == 2:
                        arr[i][j] += color # 색칠
                # 색칠 시작 (파랑)
                elif color == 2:
                    # 색이 안 칠해져있거나(0), 다른 색(=빨강)이 있는 경우(1)
                    if arr[i][j] == 0 or arr[i][j] == 1:
                        arr[i][j] += color # 색칠

    cnt = 0
    # 보라색(3) 찾기
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                cnt += 1

    print(f"#{tc} {cnt}")
