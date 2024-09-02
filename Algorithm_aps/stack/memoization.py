# memo를 위한 배열을 할당, 모두 0으로 초기화
# memo[0]을 0으로, memo[1]는 1로 초기화한다.

def fibo1(n):
	global memo
	# memo[n] == 0.. fibo(n)이 계산된 적이 없으면
	if n >= 2 and memo[n] == 0 :
		memo[n] = fibo1(n-1) + fibo1(n-2) # 저장
	return memo[n]

n = 5
memo = [0]* (n+1)
memo[0] = 0
memo[1] = 1
print(fibo1(n))