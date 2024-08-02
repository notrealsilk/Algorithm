"""
5
45 15 10 56 23
96 98 99 40 69
96 84 49 46 34
16 64 81 4 11
10 66 85 55 14

"""

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]

print(arr)
# [[45, 15, 10, 56, 23], [96, 98, 99, 40, 69], [96, 84, 49, 46, 34], [16, 64, 81, 4, 11], [10, 66, 85, 55, 14]]

di = [0,1,0,-1]
dj = [1,0,-1,0]

total = 0

for i in range(N):
    for j in range(N): # NxN 배열의 모든 원소에 대해

        s = 0 # 문제에서 원소와 주변 인접 원소의 차의 절대값의 합 저장

        # i,j 원소의 4방향 원소에 대해
        for k in range(4):
            ni = i + di[k]
            nj = i + dj[k]

            if 0<ni<N and 0<=nj<N:
                s += abs(arr[i][j] - arr[ni][nj]) # 실존하는 인접원소 ni, nj 와의 차의 절대값 abs()

        total += s

print(total)
