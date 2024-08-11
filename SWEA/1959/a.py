import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    Ai = list(map(int,input().split()))
    Bi = list(map(int,input().split()))


    #A_len > B_len 이면 Ai,Bi서로 값바꿔주기 / 인덱스 계산의 편의를 위해서
    if len(Ai) > len(Bi):
        Ai, Bi = Bi, Ai

    ## 사용할 변수들 선언
    A_len= len(Ai)
    B_len = len(Bi)
    # 마주보는 숫자을 곱한 뒤 모두 더한 최댓값 (최종 결과)
    max_hap = float("-inf")

    for _ in range(B_len - A_len + 1):
        # Bi와 대비해 Ai가 움직이는 횟수 만큼 반복(Ai,Bi 길이 사용)
        for i in range(B_len - A_len+1): #0 1 2
            cur_hap = 0
            # Ai인덱스를 기준으로 숫자 한칸씩 증가
            for j in range(A_len):
                # 현재 순회에서 마주보는 숫자 곱하고 모두 더한 값
                cur_hap += (Ai[j] * Bi[j+i])


        # 최댓값 나오면 갱신
        if max_hap < cur_hap:
            max_hap = cur_hap

    print(f"#{tc} {max_hap}")



