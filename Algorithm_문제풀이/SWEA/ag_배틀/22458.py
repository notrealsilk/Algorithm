# No.1_팀프로젝트 의견 조욜자 임스

# 동일한 의견 (결과)
yes_opinion = []

M, S = map(int,input().split())

# 마싸피, 삼싸피 의견 저장
m_opinion = [input() for i in range(M)] #마싸피
s_opinion = [input() for i in range(S)] #삼싸피

# 동일한 의견 확인
for j in range(M):
    for k in range(S):
        if m_opinion[j] == s_opinion[k]:
            yes_opinion.append(s_opinion[k])
            break

# 출력
if yes_opinion: # 동일한 의견이 있다면
    print(*yes_opinion)
else:
    print("NO!!")
