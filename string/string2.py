# 패턴 p와 일치하는 구간의 시작 인덱스 리턴, # 일치하는 경우가 없으면 -1 리턴

def f(t,p):
    N = len(t)
    M = len(p)
    for i in range(N-M+1): # 비교 시작위치
        for j in range(M):
            if t[i+j] != p[j]:
                break # for j, 다음 글자부터 비교 시작
            else: # for문이 중간없이 반복되면
                return i # 패턴을 찾은 경우
    return -1

t = "TTTTTABC"
p = 'TTA'
print(f(t,p))

t = "BCADDSXD"
p = 'TTA'
print(f(t,p))

