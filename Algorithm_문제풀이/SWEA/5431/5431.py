import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, 1 + T):
# N : 전체 학생 수/ K : 제출한 학생 수
    N, K = map(int, input().split())
    yes_stu = list(map(int, input().split()))
    no_stu = []

# yes_stu에 없으면 no_stu에 현재 순회하고 있는 i추가
    for i in range(1, N + 1):
        if i not in yes_stu:
            no_stu.append(str(i))

    result = " ".join(no_stu)
    print(f"#{tc} {result}")






