def f(i, k):  # bit[i]를 결정하는 함수
    global cnt, K
    sub_sum = 0
    if i == N:  # 모든 원소에 대해 결정하면
        for j in range(k):
            if bit[j]:  # bit[j]가 0이 아니면
                # print(a[j], end=' ')
                sub_sum +=1
        if sub_sum == K: #  부분집합의 합이 K와 같다면 카운트
            cnt += 1
        #print(sub_sum)  # 부분집합을 한 행에 표시

    else:
        bit[i] = 1
        f(i + 1, k)
        bit[i] = 0
        f(i + 1, k)

K = 2
cnt = 0
N = 3
a = [1, 2, 3]  # 주어진 원소의 집합
bit = [0] * N  # 원소의 포함여부를 표시하는 배열

f(0, N)
print(cnt)