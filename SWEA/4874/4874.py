import sys
sys.stdin = open("sample_input (2).txt", "r")

# 1. 입력값 받기
T = int(input())
for tc in range(1, T+1):
    cal = list(input().split()) # 계산식

    stack = []
    result = "" # 결과값 저장

# 2. stack 계산
    for cur in cal:
        # 숫자일 경우
        if cur.isdigit():
            stack.append(cur) # 스택에 추가

        # 연산자일 경우
        elif cur == '*':
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(num1*num2)

        elif cur == '+':
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(num1+num2)

        elif cur == '-':
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(num1-num2)

        elif cur == '/':
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            stack.append(num1/num2)

        # 스택에 숫자가 2개 미만이면
        if len(stack) > 2:
            result = 'error'
            break


        # .이면 숫자 팝
        elif cur == '.':
            result = stack.pop()
            break

        else:
            result = "error"
            break

    print(f"#{tc} {result}")

