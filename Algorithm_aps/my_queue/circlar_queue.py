# 초기 큐 생성
N = 4 # 큐 크기
cQ = [0] * N
front = rear = 0

# enQueue()
# 무한반복이 될 수도 있음
rear = (rear) % N # enq(1)
cQ[rear] = 1
rear = (rear) % N # enq(2)
cQ[rear] = 2
rear = (rear) % N # enq(3)
cQ[rear] = 3

front = (front+1) % N
print(cQ[front])
front = (front+1) % N
print(cQ[front])
front = (front+1) % N
print(cQ[front])