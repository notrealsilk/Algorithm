import sys
sys.stdin = open("sample_input (3).txt", "r")

# 1. 입력값 변수에 할당
T = int(input())
for tc in range(1, T + 1):
    # 문자열 입력받기
    gress = input()

    # 놓여있을 수 있는 공의 경우의 수
    # '()', '(|', '|)' .. 아마 3가지 경우?

    cur = "" # 순회하면서 확인해야하는 문자열을 임시로 저장할 변수
    cnt = 0 # 공 갯수 카운트

    for i in range(len(gress)-1):
        if gress[i] == "(" :
            if gress[i+1] == "|" or gress[i+1] == ")":
                cnt += 1
        elif gress[i] =="|":
            if gress[i+1] == ")":
                cnt += 1

    print(f"#{tc} {cnt}")


"""
       # cur에 저장된 변수가 없다면
        if cur == "":
            if gress[i] == "(" or gress[i] == "|":
                cur = gress[i] # 인덱스로 접근해서 문자열 형식으로 저장

        # cur에 저장된 변수가 있다면
        else :
            # cur에 값이 있고, 공 모양에 맞는 문자열이 gress[i]에 있다면
            # cnt에 +1하고 cur 초기화
            if cur == "(" and (gress[i] == ")" or gress[i] =="|"):
                cnt += 1
                cur = "" # 공 찾았으므로 초기화
            elif cur == "|" and gress[i] == ")":
                cnt += 1
                cur = "" # 공 찾았으므로 초기화
            else :
                cur = ""  # 공 찾지못했어도 초기화
"""


