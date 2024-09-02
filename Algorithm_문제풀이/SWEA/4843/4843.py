import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums_list = list(map(int,input().split()))
    result = [] # 최종적으로 특별한 정렬이 이뤄진 리스트

    # N//2번 반복하면서 nums_list N번 순회
    # 최댓값, 최솟값이 반목문을 돌면서 쌍으로 사라지므로 10//2
    for i in range(5):
        max_num = float('-inf')
        min_num = float('+inf')
        max_idx = -1
        min_idx = -1

        for j in range(len(nums_list)):
            # 최댓값 찾기
            if max_num < nums_list[j]:
                max_num = nums_list[j]
                max_idx = j

            # 최솟값 찾기
            if min_num > nums_list[j]:
                min_num = nums_list[j]
                min_idx = j

        # 최댓값 먼저, 최솟값 후에 저장
        result.append(max_num)
        result.append(min_num)

        # nums_list에서 최댓값과 최솟값 제거한 새로운 리스트 생성
        #nums_list = [num for num in nums_list if num != max_num and num != min_num]

        nums_list.remove(max_num)
        nums_list.remove(min_num)

    # N갯수가 홀수 이면, 요소가 한개 남으므로 따로 추가해줌
    # if N % 2 != 0:
    #     result.append(nums_list[0])

    print(f'#{tc}',end=" ")
    print(*result, sep=" ")

