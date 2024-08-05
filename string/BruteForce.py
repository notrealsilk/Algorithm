## 고지식한 알고리즘

target = "Hello SSAFY 12th!"  # target 패턴을 찾을 대상
pattern = "SSA"  # 우리가 찾을 패턴


def BruteForce(pat, text):
    N = len(text)
    M = len(pat)
    i = 0  # text의 인덱스
    j = 0  # 패턴의 인덱스 (M보다 작을 경우까지 탐색)

    while j < M and i < N: # 패턴이 일치할 때까지 i, j값 증가시키기

        # 틀린 곳을 발견했다면, index 값을 초기화 시킴.
        if text[i] != pat[j]: # 일치하지 않은 곳
            # text의 현재 위치에서 일치하지 않는 곳을 발견! -> i를 증가시켜야 함
            # j값과 일치하는 요소가 i에 나올 때까지 j는 증가시킬 필요가 없음
            #  지금위치 - j
            i = i - j
            # 순회 한 번이 끝나면 무조건 앞으로 나아가야 함
            # 일치하는 값이 나오지 않았다면 j는 제자리에 있어야 하므로 여기서 j에 -1을 해줌
            j = - 1

        i = i + 1
        j = j + 1

        # 검색 성공
        if j == M:
            return i - M
        else:
            return -1


# 심플 버전
text = "This is simple version"
pattern = 'vision'


def BruteForceV2(pat, text):
    for idx in range(len(text) - len(pat) + 1): # 패턴 길이에 맞게 순회
        # 패턴을 처음부터 끝까지 순회
        for j in range(len(pattern)):

            # 1. 다르면, break / 패턴 순회를 돌 필요가 없음
            if text[idx + j] != pat[j]:
                break
        # 같다면(다른게 없다면)
        else:
            return idx
    # 검색실패
    else:
        return -1 # for문을 다 돌았다 = 패턴 매칭이 안됐다.


