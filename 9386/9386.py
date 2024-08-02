import sys
sys.stdin = open("input1.txt", "r")


# 1. 테스트 케이스 입력
T = int(input())

for tc in range(1, T + 1):
    # 2. 수열 길이 입력
    idx = int(input())
    # 3. 수열 입력
    num_list = list(map(int, input()))

    # 4. 연속된 1의 최대 길이 탐색

    max_one = 0  # 연속한 1의 길이 최댓값
    cur_one = 0  # 현재 탐색중인 연속한 1의 길이 최댓값
    for i in range(idx):
        # 인덱스 탐색 과정 중, 1을 만나면
        if num_list[i] == 1:
            cur_one += 1
            # 0 만나면 cur_one 갱신 중지하고 max_one과 cur_one을 비교해서 최댓값 찾기
        elif num_list[i] == 0:
            # max_one 갱신 필요시 갱신
            if cur_one > max_one:
                max_one = cur_one

            cur_one = 0 # 1 카운트를 위해 0으로 초기화

    # for문 순회를 끝낸 후, 나온 cur_one의 값을 max_one과 비교해서 갱신이 필요하면 갱신
    # 리스트의 마지막 요소가 1인 경우, max_one과 비교를 하지 않은 상태이므로 확인이 필요
    if cur_one > max_one:
        max_one = cur_one

    print(f"#{tc} {max_one}")





