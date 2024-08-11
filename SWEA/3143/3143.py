import sys
sys.stdin = open("sample_input.txt", "r")

# 함수 : 고지식한 알고리즘을 이용해서 타이핑횟수 카운팅함
def Brute_Ag(A,B):
    i = 0 # A의 인덱스
    N = len(A)
    M = len(B)
    typing = 0 # 타이핑 횟수 (결과물)

    while i < N : # 문자열 A 길이만큼 순회

        # A, B가 겹치는 곳
        # 문자열이므로 슬라이싱으로 접근
        if A[i:i+M] == B :
            typing += 1
            i += M # 겹치는 곳은 B의 길이만큼 건너뜀

        # A,B가 겹치지 않는 곳
        else:
            typing += 1
            i += 1 # A에서 한 문자 옆으로 이동

    return typing

########################

T = int(input())
for tc in range(1, T+1) :
    # A : 입력해야하는 전체 문자열 (텍스트) / B : 일부 타이핑 (패턴)
    A, B = map(str, input().split())

    print(f"#{tc} {Brute_Ag(A,B)}")