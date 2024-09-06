# 스위치 켜고 끄기
"""
8
0 1 0 1 0 0 0 1
2
1 3
2 3
"""
# 스위치 번호는 1부터 시작, 인덱스는 0부터 시작이니 이를 조심!

s = int(input())                        # 스위치 갯수
switch = list(map(int,input().split())) # 스위치 상태
stu_len = int(input())                  # 학생 수

# 스위치 켜고 끄기 시작
for i in range(stu_len):
    stu, num = map(int,input().split()) # 학생 성별, 학생이 받은 수
    # 남학생이라면
    if stu == 1:
        # 인덱스는 0, 스위치 번호는 1부터 시작하므로 -1 해주기
        for i in range(num,len(switch)+1): # switch[num] ~ switch 끝까지 순회
            if i % num == 0:               # num이 배수라면 스위치 상태 변경
                if switch[i - 1] == 0:
                    switch[i - 1] = 1
                else:
                    switch[i - 1] = 0

    # 여학생이라면
    elif stu == 2:
        i = 1
        while True: # 좌우로 대칭이 아닐 때 까지 반복
            if num - 1 - i < 0 or num - 1 + i >= len(switch):  # 인덱스 범위를 벗어나지 않도록 확인
                if switch[num - 1] == 0:
                    switch[num - 1] = 1
                else:
                    switch[num - 1] = 0
                break

            else : # 인덱스 범위 내에 있다면
                if switch[num-1-i] == 0 and switch[num-1+i] == 0:
                    switch[num-1-i] = 1
                    switch[num-1+i] = 1
                elif switch[num-1-i] == 1 and switch[num-1+i] == 1:
                    switch[num-1-i] = 0
                    switch[num-1+i] = 0
                else :
                    if switch[num - 1] == 0:
                        switch[num - 1] = 1
                    else:
                        switch[num - 1] = 0
                    break
            i += 1

# 스위치를 20개씩 끊어서 출력하기
for i in range(0, len(switch), 20):
    print(*switch[i:i+20])
