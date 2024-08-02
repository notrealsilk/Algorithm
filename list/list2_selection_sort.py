def selection_sort (arr, N): # arr..정렬 대상, N 크기
    for i in range(N-1): # 주어진 구간에 대해.. 기준위치를 i를 정하고
        min_idx = i # 최솟값 위치를 기준위치로 가정
        for j in range(i+1, N): # 남은 원소에 대해 실제 최솟값 위치 검색
            if arr[min_idx] > arr[j]:
                min_idx = [j]
        arr[i], arr[min_idx] = arr[min_idx], arr # 구간의 최솟값을 교환



A = [2,7,5,3,4]
B = [4,3,2,1]
selection_sort(A, len(A))
selection_sort(B, len(B))