# 왕실의 나이트
location = input() # 나이트 좌표
N = 8 # 체스판 크기
cnt = 0
r = int(location[1])
# ord(문자) : 해당 문자에 해당하는 유니코드 정수 반환
# ord('a') => 97
c = ord(location[0])-96

steps = [(-2,1),(-2,-1),(2,1),(2,-1),(-1,2),(1,-2),(1,-2),(1,2),]

for step in steps:
    n_r, n_c = r+step[0],c+step[1]

    if 0 < n_r <= N and 0 < n_c <= N:
        cnt+=1
print(cnt)


