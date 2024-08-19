T = int(input()) # 전체 Test Case 수

for tc in range(1, T+1):
    N = int(input()) # LED 등 및 버튼의 수
    LED = list(map(int,input().split())) # 원하는 LED 패턴 / 버튼은 1부터, 인덱스는 0부터 (인덱스 접근 시, i+1로)

    s_LED = [0]*N # LED 초기 상태 (다 꺼진 상태)
    min_switch = 0 # 최소 스위치 조작횟수 (최종 결과)

    #while True: # 원하는 LED 패턴이 만들어 질 때까지 반복 / if문으로 멈춤
    for i in range(N):
        if s_LED[i] != LED[i] : # 현재 스위치 상태가 원하는 패턴과 다르면 스위치 켜기
            for j in range(i,N) : # 스위치 조작 시작
                if (j+1) % (i+1) == 0 : # i+1의 배수이면 스위치 조작
                    if s_LED[j] == 1 :
                        s_LED[j] = 0
                    elif s_LED[j] == 0:
                        s_LED[j] = 1
            min_switch += 1  # 스위치 눌리면 +=1 카운트

        #else : # 상태가 같으면 스위치 조작 필요 없음


        if s_LED == LED : # 원하는 LED 패턴이 만들어졌다면
            break

    print(f"#{tc} {min_switch}")

