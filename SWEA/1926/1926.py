import sys

sys.stdin = open("input.txt","r")

N = int(input())
N_list = [] # 최종 결과

for i in range(1,N+1):
    # 숫자 자리 순회해서 3,6,9 들어간 숫자 찾기
    cur_369 = []
    for j in str(i) :
        if j in "369":
            cur_369.append("-")

    # cur_369에 값이 있다 == 숫자에 3,6,9가 포함돼있다
    if cur_369:
        N_list.append("".join(cur_369))
    else:
        N_list.append(str(i))


print(*N_list)

