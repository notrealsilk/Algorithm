import sys
sys.stdin = open("input.txt", "r")

T = int(input()) # 테스트 케이스 입력

for tc in range(1, T + 1): # 테스트 케이스 순회
    # N : NxN 퍼즐  / K : 단어 길이
    N, K = map(int,input().split())

    # puzzle : NxN 크기의 2차원 리스트 생성 = 단어 퍼즐
    # N번 반복하면서 문자열을 리스트로 변환한 입력값을 받고
    # puzzle 리스트에 저장해서 2차원 리스트 만듦
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # puzzle = []
    # for i in range(N):
    #     puzzle.append(list(map(int, input().split())))

    wid = 0
    leng = 0

    # 가로 순회
    for i in range(N):
        # 가로 임시 변수
        wid_cur_cnt = 0 # 순회 중 임시로 저장할 cur_cnt
        for j in range(N):
            # 1이면 임시변수 카운트
            if puzzle[i][j] == 1:
                wid_cur_cnt += 1 # 가로
            else : # 퍼즐이 0일 떄
                if K == wid_cur_cnt : # 지금까지 나온 1의 길이가 단어 글자수와 같을 경우
                    wid +=1 # 가로에 들어 갈 수 있으므로 1 카운트
                wid_cur_cnt = 0 #초기화

        # 반복문 나온 후에, wid_cur_cnt에 남아있는 값이 있다면 카운트를 위해 반복문 밖에서 재검사
        if K == wid_cur_cnt:
            wid += 1

    # 세로 순회
    for i in range(N):
        # 세로 임시 변수
        leng_cur_cnt = 0  # 순회 중 임시로 저장할 cur_cnt
        for j in range(N):
            if puzzle[j][i] == 1:
                leng_cur_cnt += 1 # 세로
            else : # 퍼즐이 0일 떄
                if K == leng_cur_cnt : # 지금까지 나온 1의 길이가 단어 글자수와 같을 경우
                    leng +=1 # 가로에 들어 갈 수 있으므로 1 카운트
                leng_cur_cnt = 0 # 초기화

        # 반복문 나온 후에, wid_cur_cnt에 남아있는 값이 있다면 카운트를 위해 반복문 밖에서 재검사
        if K == leng_cur_cnt:
            wid += 1

    print(f'#{tc} {wid+leng}')
