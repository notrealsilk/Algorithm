import sys
sys.stdin = open("sample_input.txt", "r")

# 함수 : 문자열을 파라미터로 주면 괄호 검사하는 함수
def Search(string) :
    # 스택 사이즈 결정하기 위해 열린괄호가 몇개 있는 지 순회
    stack_cnt = 0
    for i in string:
        if i in "({[" :
            stack_cnt += 1
    # 스택 만들기
    stack = [0] * stack_cnt
    top = -1 # top 시작점

    # string 순회하면서 스택에 넣고 빼면서 괄호검사
    for j in string:
        # 열린 괄호 push
        if j in "({[" :
            top += 1
            stack[top] = j

        # 닫힌 괄호
        elif j in ")}]":
            # 열린 괄호 pop할 수 있는 지 검사
            if stack[top] == "(":
                # pop이 되면 stack[top]을 0으로 초기화
                # top 인덱스는 -1
                stack[top] = 0
                top -= 1
            elif stack[top] == "{":
                stack[top] = 0
                top -= 1
            elif stack[top] == "[":
                stack[top] = 0
                top -= 1
            # 괄호 검사 위배
            else:
                return 0

    # 스택 비었는 지 확인
    if stack == "(" or "{" or "[":
        return 0
    # for문, stack 비었는지 확인하는 if문을 다 돌았다 = 괄호 검사가 문제 없이 끝났다
    else :
        return 1

###############################################

# 테스트 케이스 입력
T = int(input())
for tc in range(1, T + 1):
    # 문자열 입력
    string = input()
    print(f"#{tc} {Search(string)}")