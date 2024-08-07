<<<<<<< HEAD
# 테스트 케이스 입력
for _ in range(10):
    tc = int(input())
    N = 100  # 100x100
    arr = [input().strip() for _ in range(N)]

    # 가장 긴 회문의 길이
    max_len = 1

    # 가로
    for i in range(N):
        for start in range(N):
            for end in range(start + max_len, N):  # max_len보다 긴 부분 문자열만 고려
                cur_word = arr[i][start:end + 1]
                # 회문 확인
                if cur_word == cur_word[::-1]:
                    # 더 긴 회문이 발견되면 max_len 갱신
                    max_len = end - start + 1

    # 세로
    for j in range(N):
        for start in range(N):
            # 현재까지 저장된 max_len보다 긴 문자열을 검사
            for end in range(start + max_len, N):
                # 시작~끝까지 세로 문자열을 생성
                cur_word = ''.join(arr[i][j] for i in range(start, end + 1))
                # 회문 확인
                if cur_word == cur_word[::-1]:
                    # 더 긴 회문이 발견되면 max_len 갱신
                    max_len = end - start + 1
=======
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
>>>>>>> afec26f207e2f529d2399fcf764b5283221806ae

    print(f"#{tc} {max_len}")
