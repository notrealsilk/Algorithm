path = [] # 수열 저장

# 특정 숫자가 이미 사용되었는지 확인 
# 예를 들어, [False, True, False, ...] 이런 식으로 특정 숫자가 사용되었는지 여부를 나타냅니다.
used = []

N = 0 # 수열 길이

## 순열 중복 허용
def type1(x):
		## 기저조건
    # x가 N과 같으면, 즉 수열의 길이가 N에 도달하면 지금까지 만든 수열을 출력
    if x == N:
        print(path)
        return

    # 주사위의 눈(1부터 6까지)을 하나씩 시도합니다.
    for i in range(1, 7):
        # 현재 눈을 수열에 추가
        path.append(i)
        # 재귀 호출로 다음 수를 결정
        type1(x + 1)
        # 수열에서 마지막에 추가한 눈을 제거하여 다음 반복에서 다른 눈을 시도
        path.pop()

## 순열 중복을 허용하지 않음 = (중복을 제거하는 코드)
def type2(x):
    # x가 N과 같으면, 즉 수열의 길이가 N에 도달하면 지금까지 만든 수열을 출력
    if x == N:
        print(path)
        return

    # 주사위의 눈(1부터 6까지)을 하나씩 시도합니다.
    for i in range(1, 7):
        # 만약 이 눈이 이미 수열에 사용되었으면, 넘어감
        if used[i]:
            continue

        used[i] = True # 이 눈을 사용했음을 기록
        path.append(i) # 현재 눈을 수열에 추가
        type2(x + 1) # 재귀 호출로 다음 수를 결정
        # 수열에서 마지막에 추가한 눈을 제거하여 다음 반복에서 다른 눈을 시도합니다.
        path.pop()
        # 이 눈을 다시 사용할 수 있도록 표시합니다.
        used[i] = False

# N과 type 값을 입력받습니다.
# N은 수열의 길이, type은 수열 생성 방식을 나타냅니다.
N, type = map(int, input().split())

# used 리스트를 False로 초기화합니다. (숫자 1부터 6까지 사용 여부를 추적)
used = [False for _ in range(7)]

# type 값에 따라 다른 수열 생성 방식을 실행합니다.
if type == 1:
    type1(0)

if type == 2:
    type2(0)
