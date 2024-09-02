STACK_SIZE = 10
stack = [0]*STACK_SIZE
top = -1

top += 1
stack[top] = 1 # push(1)
top += 1
stack[top] = 2 # push(2)
top += 1
stack[top] = 3 # push(3)

top = -1 # pop() # 출력하기 전에 top을 -1하고 출력하기
print(stack[top+1])