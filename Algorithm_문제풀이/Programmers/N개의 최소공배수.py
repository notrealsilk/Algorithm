# N개의 최소공배수
# arr 원소의 최댓값을 기준으로 배수 올리면서 모든 원소가 공배수 되는 지 확인하기

def solution(arr):
    max_num = max(arr)  # arr 원소 중 최댓값
    B = 1  # 배수 올리는 변수

    is_done = False  # 최소공배수를 찾았는지 확인하는 변수

    # 최소공배수 구하기
    while not is_done:  # 최소 공배수 찾을 때까지 반복
        is_common = True  # 모든 원소가 공배수인지 확인하는 플래그
        for i in range(len(arr)):
            if (max_num * B) % arr[i] != 0:  # 공배수가 아닌 원소가 있으면 플래그 변경 후 break
                is_common = False
                break
        if is_common:
            is_done = True
        else:
            B += 1  # 공배수를 못 찾았으면 B를 증가시킴

    # 최소 공배수 찾음
    answer = max_num * B
    return answer
