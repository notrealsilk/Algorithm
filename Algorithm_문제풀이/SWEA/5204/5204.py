def merge_sort(arr):
    global cnt
    # 기저 조건
    if len(arr) == 1: # 배열의 길이가 1이다 = 분할이 끝났다.
        return arr


    ## 분할
    mid = len(arr) // 2
    left = arr[:mid]  # 리스트의 앞쪽 절반
    right = arr[mid:]  # 리스트의 뒤쪽 절반

    # 나눈 리스트 배열
    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # 왼쪽 원소가 더 크면 += cnt
    if sorted_left[-1] > sorted_right[-1]:
        cnt +=1

    # 병합
    # 각 배열의 제일 앞요소를 비교해서 작은거 새로운 배열에 붙이기
    result = []  # 정렬된 배열
    left_length = len(sorted_left)
    right_length = len(sorted_right)
    i = j = 0

    while i < left_length and j < right_length:
        if sorted_left[i] < sorted_right[j]:
            result.append(sorted_left[i])
            i += 1
        else:
            result.append(sorted_right[j])
            j += 1
    # left나 right 둘 중 하나는 요소가 없음!
    # 남아있는거 다 붙이기
    result += sorted_left[i:]
    result += sorted_right[j:]
    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split())) # 정렬할 배열

    cnt = 0
    sorted_arr = merge_sort(arr)

    print(f'#{tc} {sorted_arr[N//2]} {cnt}')


