def kmp(t, p):
    N = len(t)  # 텍스트의 길이
    M = len(p)  # 패턴의 길이
    lps = [0] * M  # LPS 배열 초기화

    # LPS 배열 계산
    length = 0  # 가장 긴 접두사와 접미사의 길이
    i = 1

    while i < M:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]  # LPS 배열을 참조하여 길이 조정
            else:
                lps[i] = 0
                i += 1

    # 패턴 검색
    i = 0  # 텍스트 인덱스
    j = 0  # 패턴 인덱스

    while i < N:
        if p[j] == t[i]:
            i += 1
            j += 1

        if j == M:  # 패턴이 발견된 경우
            print(i - j, end=' ')  # 패턴의 시작 인덱스 출력
            j = lps[j - 1]  # 다음 비교를 위해 패턴 인덱스 조정

        elif i < N and p[j] != t[i]:
            if j != 0:
                j = lps[j - 1]  # 패턴 인덱스 조정
            else:
                i += 1  # 텍스트 인덱스 증가

    print()  # 줄 바꿈
    return


# 예제 사용
t = 'zzzzzabcacfcbca'
p = 'abcacf'
kmp(t, p)
