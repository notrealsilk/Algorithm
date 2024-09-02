import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    num_list = list(map(int,input().split()))
    subset = []

    # 부분집합 만들기
    for a in range(2) :
        num_list[0] = a
        for b in range(2):
            num_list[1] = b
            for c in range(2):
                num_list[2] = c
                for d in range(2):
                    num_list[3] = d
                    for e in range(2):
                        num_list[4] = e
                        for f in range(2):
                            num_list[5] = f
                            for g in range(2):
                                num_list[6] = g
                                for h in range(2):
                                    num_list[7] = h
                                    for i in range(2):
                                        num_list[8] = i
                                        for j in range(2):
                                            num_list[9] = j
                                            subset.append(num_list.copy())
    print(subset)