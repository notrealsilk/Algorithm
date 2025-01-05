# 5 8 3
# 2 4 5 2 6
N, M, K = map(int, input().split()) # 5 8 3
arr = list(map(int, input().split())) # [2, 4, 5, 2, 6]

# 최대한 가장 큰 수를 더하되, K번 횟수 째가 되면 두번쨰 큰 수 한번만 더했다가 바로 첫번쨰 수로 돌아오기

# 첫번째, 두번째 큰 값 찾기
arr.sort() # [2, 4, 4, 5, 6]
first_num = arr[-1] # 6
second_num = arr[-2] # 5

cnt = 0
result = 0 # 결과값

while cnt < M:
    # 첫번째
    for i in range(K):
        result += first_num
        cnt+=1
    # 두번째
    result+=second_num
    cnt+=1

print(result) # 46
