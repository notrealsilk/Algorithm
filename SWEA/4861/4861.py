# 회문

import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트 케이스 수 입력
T = int(input())
for tc in range(1, T + 1):
    # N: 글자판의 크기, M: 회문의 길이
    N, M = map(int, input().split())
    # NxN 글자판
    arr = [input() for _ in range(N)]

    # 회문 단어 저장 // 최종 결과
    result = ""

    # 가로 방향
    for i in range(N): # 리스트 안 요소 (단어) 순회
        for j in range(N - M + 1):  # 시작 가능한 위치 // 문자열 순회
           word = arr[i][j:j + M]
           if word == word[::-1]:  # 회문 검사
                result = word  # 회문을 찾으면 저장
                break  # 안쪽 루프 중단
        if result:  # 안쪽 루프에서 회문을 찾았다면
            break  # 바깥쪽 루프도 중단

    # 세로 방향
    if not result:  # 가로에서 찾지 못한 경우에만 세로 검사
        for j in range(N):
            for i in range(N - M + 1):
                word = ''.join(arr[i + k][j] for k in range(M))
                if word == word[::-1]:
                    result = word  # 회문을 찾으면 저장
                    break  # 안쪽 루프 중단
            if result:  # 안쪽 루프에서 회문을 찾았다면
                break  # 바깥쪽 루프도 중단

    print(f"#{tc} {result}")
