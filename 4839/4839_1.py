## 함수 2개로 줄임, book 리스트를 만듦

import sys
sys.stdin = open("sample_input.txt", "r")

# 함수1 : A,B 중 빠르게 이진탐색한 사람 찾기
# 파라미터 >> P : 책 전체 쪽수/ Pa : A가 찾아야할 페이지 / Pb : B가 찾아야할 페이지
def fast_search(P, Pa, Pb):

    # 책 쪽수가 담긴 리스트 만들기
    book = list(range(1, P+1))

    # 함수2에서 각각 학생 A,B의 이진 탐색횟수 호출
    count_A = binarysearch(book, Pa)
    count_B = binarysearch(book, Pb)

    # A,B의 이진 탐색횟수를 비교해서 승자 찾기 (비긴 것도)
    # 탐색횟수가 적어야 승자

    if count_A < count_B :      # A 승리
        return 'A'
    elif count_A > count_B :    # B 승리
        return 'B'
    else :                      # 비김
        return '0'


# 함수2 : 이진탐색 횟수
# 파라미터 >> book..책 쪽수 리스트, target..찾을려는 페이지
def binarysearch(book, target):
    l = 0 # 검색 구간의 왼쪽 인덱스
    r = len(book) - 1 # 검색 구간의 오른쪽 인덱스
    count = 0 # 이진탐색 횟수 (함수의 return 값)

    while l <= r :
        count += 1 # while문 실행 될 때 마다 횟수 카운트

        c = (l + r)//2
        if book[c] == target : # 검색성공
            return count
        elif book[c] > target : # (중간페이지 > 찾을려는 페이지)면, 오른쪽 범위를 줄임
            r = c - 1
        else:               # (중간페이지 < 찾을려는 페이지)면, 왼쪽 범위를 줄임
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