# 직사각형 네개의 합집합의 면적 구하기
"""
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6
"""
area = 0 # 직사각형이 차지하는 면적 (최종 결과)
arr = [[0]*100 for _ in range(100)] # 100x100 평면 / 여기에서 면적 카운트해서 넓이 셀 거임

# 값 입력 받고
# 해당하는 부분 arr에 1로 면적 채우기
for _ in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    # 좌표 탐색하면서 1로 면적 채우기
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1

# arr에 1로 채워진 부분 갯수 세서 area에 저장 (최종 결과)
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            area += 1
print(area)



