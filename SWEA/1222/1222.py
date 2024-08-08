import sys
sys.stdin = open("input.txt", "r")

T = 10 # 10개 케이스
for tc in range(1,T+1):
    num = int(input()) # 계산식 길이
    cal = list(input())

    #isp = {'(' : 0, '+':1, '-':1, '*':2, '/':2} # 스택 안
    #icp = {'(':3,'+':1, '-':1, '*':2, '/':2} # 스택 밖
    stack = [] # 스택
    num_list = [] # 스택에서 나온 연산자, 피연산자 저장
    top = -1

#  중위표현식  to 후위표현식
# cal이 빌 때 까지 반복
    for cur1 in cal:# 현재 요소를 while문 반복할 때마다 하나씩 꺼냄

        # 숫자면 num_list에 추가
        if cur1 in ['0','1','2','3','4','5','6','7','8','9']:
            num_list.append(int(cur1)) # 입력받은 숫자가 str이므로 int로 바꾸기

        # "+"이면 stack에 추가
        if cur1 == "+":
            top += 1
            stack.append(cur1)
            # 스택에 "+"가 2개 이상 있으면 pop하고 num_list에 추가
            if top == 1:
                tmp = stack.pop()
                top -= 1
                num_list.append(tmp)
    # 마지막 + 요소 pop
    top -= 1
    num_list.append(stack.pop())

# 후위표현식 to 계산
    for cur2 in num_list:
        # 숫자면 stack에 넣기
        if cur2 in [0,1,2,3,4,5,6,7,8,9]:
            top += 1
            stack.append(cur2)

        if cur2 == "+":
            # 스택에서 숫자 2개 stack에서 뽑기
            top -= 1
            num2 = stack.pop()
            top -= 1
            num1 = stack.pop()

            # 계산
            tmp = num1 + num2

            # 계산한 값을 다시 stack에 넣기
            top += 1
            stack.append(tmp)

    # 최종 결과값 스택에서 빼서 출력
    result = stack.pop()

    print(f"#{tc} {result}")