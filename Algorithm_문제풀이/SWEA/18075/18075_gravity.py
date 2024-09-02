'''
3
9
7 4 2 0 0 6 0 7 0
9
7 4 2 0 0 6 7 7 0
20
52 56 38 77 43 31 11 87 68 64 88 76 56 59 46 57 75 85 65 53

1. 테스트 케이스 입력 > for문
2. 박스크기 입력
3. 리스트 입력

'''

T = int(input()) # 테스트 케이스 입력

for tc in range(1, T+1):
    # 상자들이 담겨있는 칸의 개수
    width = int(input())  # 가로 방 크기 입력
    # 각 상자들의 높이가 담겨있다.
    # 공백을 기준으로 입력받는다.
    box_list = list(map(int, input().split()))  # 쌓여있는 상자 수 입력, 리스트로 저장 // [7, 4, 2, 0, 0, 6, 0, 7, 0]
    #print(tc,width, box_list) # 디버깅 (중간 확인)

    result = 0 # 최종 결과값

    # 모든 상황에 대한 낙차값 구하기 위한 순회
    for i in range(width) :
        # 방해를 받지 않았을 때, i번째 상자가 떨어질 수 있는 최대 높이
        # 전체 길이 - 내 위치+1
        max_h = len(box_list) - (i + 1)

        # 내 다음으로 오는 상장 중 나와 높이가 같거나 더 높은 박스 찾기
        for j in range(i+1, len(box_list)) :# 나를 비교할 필요가 없기에 i+1부터 시작
            # i와 j를 비교 >> i는 현재 검사중인 박스, j는 내 오른쪽에 있는 박스들을 순차 검사
            if box_list[i] <= box_list[j]:
                max_h -= 1 # 나보다 높은 값이 발견되면 최대 낙차값에서 -1 하기

        # 여기서 지금 검사한 상자 높이가 result 값보다 크다면 갱신
        if result < max_h:
            result = max_h

    print(f'#{tc} {result}')

