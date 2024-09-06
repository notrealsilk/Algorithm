# 수 이어가기
"""
100
"""
N = int(input()) # 첫번째 수

max_list = [] # 게임 규칙에 따라 만들 수 있는 최대 개수의 수들

# "두번 째 수"로 선택할 수 있는 수 반복
# (첫번 째 수 < 두번째 수)는 규칙에 따라 음수이므로, 최대 개수가 될 수 없어서 고려할 필요 없음
for i in range(1,N+1):
    tem_list = []
    tem_list.append(N) # 첫번쨰 수
    tem_list.append(i) # 두번쨰 수

    # 게임 시작
    idx = 0
    while True:
        next = tem_list[idx]-tem_list[idx+1] # 앞의 앞의 수에서 앞의 수를 빼기
        if next < 0 :  # 음수라면 게임 멈추기
            break
        tem_list.append(next)
        idx +=1

    # 최대 개수의 수 구하기
    if len(max_list) < len(tem_list):
        max_list = tem_list

print(len(max_list))
print(*max_list)
