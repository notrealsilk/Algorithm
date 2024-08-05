import sys

# 테스트 케이스 입력
for _ in range(10):
    tc = int(input())
    N = 100
    arr = [input().strip() for _ in range(N)]

    # 가장 긴 회문 길이
    max_len = 1

    # 가로 방향
    for i in range(N):
        for start in range(N):
            for end in range(start + max_len, N):
                word = arr[i][start:end + 1]
                if word == word[::-1]:  # 회문 검사
                    if end - start + 1 > max_len:  # 길이 비교하여 갱신
                        max_len = end - start + 1

    # 세로 방향
    for j in range(N):
        for start in range(N):
            for end in range(start + max_len, N):
                # 세로 문자열 생성
                word = ''.join(arr[i][j] for i in range(start, end + 1))
                if word == word[::-1]:  # 회문 검사
                    if end - start + 1 > max_len:  # 길이 비교하여 갱신
                        max_len = end - start + 1

    print(f"#{tc} {max_len}")
