# strip('[]')  으로 문자열 양 끝에 있는 대괄호 제거
# ,를 기준으로 문자열 나눠서 int형 리스트로 변환
arr = list(map(int, input().strip('[]').split(', '))) # arr : 번호 누르는 순서
hand = input() # hand : 오른손 or 왼손잡이

key_pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]

# *,#을 -1로 처리
left = -1 # 왼손 현재 위치
right = -1 # 오른손 현재 위치

used_hand = "" # 사용한 손 (최종결과)

# 버튼 누르기 시작 !
for i in arr :
    if i == key_pad[0][0] or i == key_pad[1][0] or key_pad[2][0]:  # 1,4,7 번호를 눌러야 한다면
    #if i == 1 or i == 4 or i == 7 :
        left = i # 왼손으로 버튼 누르기
        used_hand += "L" # 사용한 손 저장

    elif i == key_pad[0][2] or i == key_pad[1][2] or i == key_pad[2][2] : # 3,6,9 번호를 눌러야 한다면
    #elif i == 3 or i == 6 or i == 9 :
        right = i # 오른손으로 버튼 누르기
        used_hand += "R" # 사용한 손 저장

    elif i == key_pad[0][1] or i == key_pad[1][1] or i == key_pad[2][1] or i == key_pad[3][1] :  # 2,5,8,0 번호를 눌러야 한다면
    # elif i == 2 or i == 5 or i == 8 or i == 0 :
        # 현재 손 위치 계산 시작
        # 왼손, 오른손이 각각 움직인 횟수
        left_move = 0
        right_move = 0

        # 1. 두 손가락의 현 위치를 기준으로 어느 손가락이 i에 가까운지 카운트
        # 1-1. 만약 거리가 같다면 오른손,왼손잡이 인지 비교해서 버튼 누를 손 결정하기

print(used_hand)




