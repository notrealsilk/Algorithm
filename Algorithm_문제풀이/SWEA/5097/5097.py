import sys
sys.stdin = open("sample_input (4).txt", "r")

# 입력값 받기
T = int(input())
for tc in range(1, T+1):
    # N : 숫자 갯수, M : 작업 횟수
    N, M = map(int, input().split())
    # arr : N개의 숫자로 이뤄진 수열
    arr = list(map(int, input().split()))

    for i in range(M):
        # 인덱스 0에 있는 숫자 pop해서 인덱스 맨 끝에 append
        arr.append(arr.pop(0))

    print(f"#{tc} {arr[0]}")