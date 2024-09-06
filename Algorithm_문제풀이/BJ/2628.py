# 종이 자르기
"""
10 8
3
0 3
1 4
0 2
"""
w_len,v_len = map(int,input().split())       # w : 가로 / v : 세로
#arr = [[0] * width for _ in range(vertical)]    # (w x v) 종이 만들기
c = int(input())    # c : 자르는 횟수
max_area = 0        # max_area : 가장 큰 넓이 (최종 결과)

w_arr = [] # 가로로 자르는 점선 번호
v_arr = [] # 세로로 자르는 점선 번호

# 종이 자르는 위치 입력 받기
for _ in range(c):
    dirt, num = map(int,input().split())
    if dirt == 0:
        w_arr.append(num)
    elif dirt == 1:
        v_arr.append(num)

# 입력받은 값 정렬
w_arr.sort()
v_arr.sort()

# 잘려진 종이 좌표 저장
w_cut = []
v_cut = []

# 가로
if w_arr:
    w_cut.append(w_arr[0])
    for w in range(1,len(w_arr)):
        w_cut.append(w_arr[w] - w_arr[w-1])
    w_cut.append(v_len-w_arr[-1])       # 가로로 자르는 좌표는 열(세로)에 있으므로 v_len에서 빼줘야 함
else:
    w_cut.append(v_len)
# print(w_cut) # [2, 1, 5]


# 세로
if v_arr:
    v_cut.append(v_arr[0])
    for v in range(1,len(v_arr)):
        v_cut.append(v_arr[v] - v_arr[v-1])
    v_cut.append(w_len-v_arr[-1])
else:
    v_cut.append(w_len)
#print(v_cut) # [4, 6]

# 최대 넓이 찾기[4, 6]
for i in range(len(w_cut)):
    for j in range(len(v_cut)):
        tem_area = w_cut[i]*v_cut[j]

        # 최댓값 찾으면 갱신
        max_area = max(max_area,tem_area)

print(max_area)
