T = int(input())

for tc in range(1, T + 1):
    arr = [list(input()) for i in range(5)]  # 5개의 문자열을 리스트로 입력 받기
    result = ""

    max_length = 0
    for i in range(5):  # 가장 긴 문자열의 길이 찾기
        if len(arr[i]) > max_length:
            max_length = len(arr[i])

    for i in range(max_length):  # 가장 긴 문자열 길이만큼 반복
        for j in range(5):
            if i < len(arr[j]):  # 현재 인덱스가 유효한지 확인
                result += arr[j][i]

    print(f"#{tc} {result}")
