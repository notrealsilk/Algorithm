import sys
sys.stdin = open("input.txt", "r")

T = int(input()) # 테스트 케이스 입력

for tc in range(1, T + 1): # 테스트 케이스 순회
    # N : 카드 장수
    N = int(input())
    # card : N개의 숫자 ai
    card = list(map(int, input().strip())) # 입력을 받고 양쪽 공백을 제거 / 리스트 변환


    # max_num : 가장 많은 카드의 숫자 max_cnt : 장 수
    max_num , max_cnt = 0, 0

    # 카드 장 수(N)만큼 순회..0~N-1
    for i in range(N):
        cur_cnt = 0 # 순회 중 임시로 저장할 cur_cnt

        for j in range(N):
            # 순회중인 숫자가 같으면 cur_cnt 갱신
            if card[i] == card[j]:
                cur_cnt +=1

        # 현재 max_cnt보다 큰 수가 나타나면 재할당 / max_num 갱신
        if max_cnt < cur_cnt:
            max_cnt = cur_cnt # 큰 수 재할당
            max_num = card[i]
        # 카드 장수가 같으면 숫자 크기로 갱신
        elif max_cnt == cur_cnt and max_num < card[i] :
            max_num = card[i]

    print(f'#{tc} {max_num} {max_cnt}')
