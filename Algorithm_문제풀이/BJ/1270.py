n = int(input())  # n : 땅의 개수

for i in range(n):
    arr = list(map(int, input().split()))
    Ti = arr[0]  # Ti : 병사 수
    Nij_arr = arr[1:]  # Nij : 군대 번호

    Nij_arr.sort()  # 정렬해서 갯수 카운트

    max_cnt = 0 # max 병사 번호 카운트
    nij = 0  # 병사 번호

    j = 0  # 인덱스
    while j < Ti: # 땅의 병사 수가 될 때까지 반복
        cur_cnt = 0 # 현재 병사 카운트
        cur_nij = Nij_arr[j] # 현재 병사번호
        while j + cur_cnt < Ti and Nij_arr[j] == Nij_arr[j + cur_cnt]: # 인덱스 범위 내에서 확인, 같은 병사 번호가 끝날 때까지 반복
            cur_cnt += 1 # 같은 병사 번호 나오면 카운트

        if max_cnt < cur_cnt:  # 최대 갯수 비교
            max_cnt = cur_cnt
            nij = cur_nij  # 병사번호 갱신

        j += cur_cnt  # 다음 병사 번호로 이동

    if max_cnt > Ti // 2:  # 땅이 지배됐는지 확인
        print(nij)
    else:  # 땅이 전쟁중이라면
        print("SYJKGW")
