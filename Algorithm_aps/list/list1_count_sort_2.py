DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNTS = [0] * 5 # DATA가 0~4까지의 정수

N = len(DATA) # DATA의 크기
TEMP = [0] * N # 정렬 결과 저장

# 1단계 : DATA 원소 별 개수 세기
for x in DATA: # DATA 원소 x를 가져와서 COUNTS[x]에 개수 기록
    COUNTS[x] += 1

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1,5): # COUNT[0]~COUNT[4] 까지 누적 개수
    COUNTS[i] = COUNTS[i-1] + COUNTS[i]

# 3단계 : DATA 맨 뒤부터 TEMP에 자리 잡기
for i in range(N-1, -1, -1): # N-1~ 0까지
    COUNTS[DATA[i]] -= 1 # 누적개수 1개 감소
    #idx = [COUNTS[DATA[i] # 아래와 같은 경우가 어려우면 이렇게 한단계 거쳐도 ㄱㅊ
    TEMP[COUNTS[DATA[i]]] = DATA[i]

print(*TEMP)