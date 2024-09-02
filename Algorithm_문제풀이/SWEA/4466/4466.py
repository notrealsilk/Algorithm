import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    #N : 총 과목 수 # K : 선택 할 수 있는 과목 수
    N, K = map(int,input().split())
    N_score = list(map(int,input().split()))

    max_score = 0  # 총점의 최댓값

# print(N,K, N_score)

    # 점수의 최댓값을 K개 찾기
    for i in range(K):
        # 순회중일 때의 최대값
        cur_score = float("-inf")
        # 순회중일 때의 최대값 인덱스
        max_index = float("-inf")

        # 과목의 점수들 순회하면서 최대 점수 찾기
        for j in range(len(N_score)):
            # 현재 순회에서 저장된 점수보다 높은 점수가 나오면 갱신
            # 순회하면서 리스트 길이가 하나씩 작아지므로 -i 씩 빼주기
            if cur_score < N_score[j]:
                cur_score = N_score[j]
                max_score = j

        # 현재 순회에서 찾은 최댓값 점수를 max_score의 합으로 갱신
        max_score += cur_score
        # 현재 순회에서 최댓값 찾으면 그 최댓값을 리스트에서 지움
        # pop(index) : 인덱스로 접근해서 해당 요소를 pop
        N_score.pop(max_index)

    print(f"#{tc} {max_score}")

"""
pop(index):

index 위치에 있는 요소를 제거하고 반환합니다.
예를 들어, my_list.pop(2)는 리스트의 세 번째 요소(인덱스 2에 해당)를 제거하고 반환합니다.
인덱스를 지정하지 않으면 pop()은 기본적으로 리스트의 마지막 요소를 제거합니다.
"""






