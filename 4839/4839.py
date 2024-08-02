## 함수 3개, book 리스트를 만듦

import sys
sys.stdin = open("sample_input.txt", "r")

# 함수1 : A,B 중 빠르게 이진탐색한 사람 찾기
# 파라미터 >> P : 책 전체 쪽수/ Pa : A가 찾아야할 페이지 / Pb : B가 찾아야할 페이지
def fast_search(P, Pa, Pb):

    # 책 쪽수가 담긴 리스트 만들기
    book = list(range(1, P + 1))

    # 함수2, 함수 3에서 각각 학생 A,B의 이진 탐색횟수 호출
    count_A = A_binarysearch(book, Pa)
    count_B = B_binarysearch(book, Pb)

    # A,B의 이진 탐색횟수를 비교해서 승자 찾기 (비긴 것도)
    # 탐색횟수가 적어야 승자

    if count_A < count_B :      # A 승리
        return 'A'
    elif count_A > count_B :    # B 승리
        return 'B'
    else :                      # 비김
        return '0'


# 함수2 : A의 이진탐색 횟수
def A_binarysearch(book, Pa):
    l = 0 # 검색 구간의 왼쪽 인덱스
    r = len(book) - 1 # 검색 구간의 오른쪽 인덱스
    count_A = 0 # A학생의 이진탐색 횟수 (함수2의 return 값)

    while l <= r :
        count_A += 1 # while문 실행 될 때 마다 횟수 카운트

        c = (l + r)//2
        if book[c] == Pa : # 검색성공
            return count_A
        elif book[c] > Pa : # (중간페이지 > 찾을려는 페이지)면, 검색 구간 페이지를 낮춘다.
            r = c - 1
        else:               # (중간페이지 < 찾을려는 페이지)면, 검색 구간 페이지를 높인다.
            l = c + 1

    return False # 검색 실패

# 함수3 : B의 이진탐색 횟수
def B_binarysearch(book, Pb):
    l = 0 # 검색 구간의 왼쪽 인덱스
    r = len(book) - 1 # 검색 구간의 오른쪽 인덱스
    count_B = 0  # B학생의 이진탐색 횟수 (함수3의 return 값)

    while l <= r :
        count_B += 1 # while문 실행 될 때 마다 횟수 카운트

        c = (l + r)//2
        if book[c] == Pb : # 검색성공
            return count_B
        # (중간페이지 > 찾을려는 페이지)면, 검색 구간 오른쪽 인덱스(= 끝 인덱스)를 낮춰서 앞으로 검색할 페이지를 낮춘다.
        elif book[c] > Pb :
            r = c - 1
        # (중간페이지 < 찾을려는 페이지)면, 검색 구간 오른쪽 인덱스(= 끝 인덱스)를 높여서 앞으로 검색할 페이지를 높인다.
        else:
            l = c + 1

    return False # 검색 실패

##################################################

# 테스트케이스 입력
T = int(input())

# 테스트 케이스 순회
for tc in range(1, T+1):
    # (P : 책의 전체 쪽수 / Pa : A가 찾을 쪽 번호 / Pb : B가 찾을 쪽 번호) 입력
    P, Pa, Pb = map(int, input().split())

    # 함수 호출해서 승자 찾기
    result = fast_search(P, Pa, Pb)
    print(f"#{tc} {result}")