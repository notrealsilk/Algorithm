import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input()) # 농장크기
    arr = [list(map(int, str(input()))) for _ in range(N)]

    center = N//2 # 정마름모의 가운데
    # 농작물 총합저장
    cnt = 0

    # 0 ~ center 순회
    for i in range(0, center+1): # 행
        for j in range(center-i, center+i+1): # 도대체 이런 패턴을 어케 빨리 찾는담,,
            cnt += arr[i][j]


    # center ~ N 순회
    for i in range(center+1, N): # 행
        for j in range(i-center, N-(i-center)):
            cnt += arr[i][j]

    print(f"#{tc} {cnt}")