def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)

print(fact(5))

##################

def f(n):
    global cnt
    cnt +=1 # 함수 호출때마다 카운트
    if n == 0: # 0이면 호출 멈춤
        return
    else:
        f(n-1)

cnt = 0
f(5) # 재귀호출 횟수가 너무 많아지면 에러남.. f(1000)같이..
# pypy로 하면 작동됨
print(cnt)

##########

def f3(i, N): # i : 현재 인덱스 / N : 크기
    if i ==N :
        return
    else:
        print(arr[i])
        return

arr = [1,2,3]
N = 3
f3(0, N)