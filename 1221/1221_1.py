# GNS

# 기준 리스트를 딕셔너리로 변환하여 매핑
num_list = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
order_map = {word: index for index, word in enumerate(num_list)}

# 직접 정렬 함수 (버블 정렬 사용)
def bubble_sort(num_list_order):
    n = len(num_list_order)
    for i in range(n):
        for j in range(0, n-i-1):
            # order_map을 사용하여 각 단어의 순서를 비교
            if order_map[num_list_order[j]] > order_map[num_list_order[j+1]]:
                # 순서가 틀리면 교환
                num_list_order[j], num_list_order[j+1] = num_list_order[j+1], num_list_order[j]
    return num_list_order

################################

# 테스트 케이스 수 읽기
T = int(input())

# 각 테스트 케이스에 대해 작업 수행
for i in range(1, T + 1):
    # 테스트 케이스 번호와 단어 수 읽기
    tc, word_len = input().split()
    # 정렬할 단어 리스트 읽기
    num_list_order = input().split()
    # 정렬 함수 호출
    result = bubble_sort(num_list_order)

    # 결과 출력
    print(f"{tc} {' '.join(result)}")