# 임스의 SSAFY 알고리즘 문제 추천


N = int(input()) # 문제 푼 일수
A = list(map(int, input().split())) # N일 동안 푼 문제
M = int(input()) # 문제들의 정보 갯수
solv_list = [[x[0], int(x[1]), int(x[2])] for x in (input().split() for _ in range(M))] # 입력하면서 int형 변환
result_solv = [0]*N # 문제 푼 일자에 추천된 문제수 (최종 결과)
j = 0 # M순회할 떄 순회 인덱스 저장

for i in range(N):
    while A[i] > 0 : # 푼 문제를 확인하면 -카운트 할 것
        if solv_list[j][0] == 'ko' and solv_list[j][1] == 3: # 'ko'문제이면서 등급이 3이면
            result_solv[i] += 1
        A[i]-= 1
    j += 1
print(*result_solv)