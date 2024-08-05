import sys
sys.stdin = open("sample_input.txt", "r")

#### 최종 #####
## 함수 2개로 줄임, book 리스트 제거하고 바로 숫자로 페이지 탐색(이건 숫자가 하나하나씩 다 있는 순열이므로)


# 함수1 : A,B 중 빠르게 이진탐색한 사람 찾기
# 파라미터 >> P : 책 전체 쪽수/ Pa : A가 찾아야할 페이지 / Pb : B가 찾아야할 페이지
def fast_search(P, Pa, Pb):

    # 함수2에서 각각 학생 A,B의 이진 탐색횟수 호출
    count_A = binarysearch(P, Pa)
    count_B = binarysearch(P, Pb)

    # A,B의 이진 탐색횟수를 비교해서 승자 찾기 (비긴 것도)
    # 탐색횟수가 적어야 승자

    if count_A < count_B:      # A 승리
        return 'A'
    elif count_A > count_B:    # B 승리
        return 'B'
    else:                      # 비김
        return '0'


# 함수2 : 이진탐색 횟수
# 파라미터 >> P..책 전체 쪽수, page..찾을려는 페이지 번호
def binarysearch(P, page):
    l = 1 # 페이지 시작
    r = P # 페이지 끝
    cnt = 0 # 이진탐색 횟수 (함수의 return 값)

    while l <= r :
        cnt += 1 # while문 실행 될 때 마다 횟수 카운트
        c = (l + r)//2 # 중간 페이지 찾기

        if c == page : # 페이지 찾음 (성공)
            return cnt
        elif c > page : # (중간페이지 > 찾을려는 페이지)면, 오른쪽 범위를 줄임 // 탐색 페이지 번호를 낮춤(왼쪽 탐색)
            r = c
        else:             # (중간페이지 < 찾을려는 페이지)면, 왼쪽 범위를 줄임 // 탐색 페이지 번호를 높임(오른쪽 탐색)
            l = c

    return cnt

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