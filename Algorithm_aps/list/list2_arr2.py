arr1 = [0] * 3
arr2 = [[0] * 3 for _ in range(2)]

print(arr1)# [0, 0, 0]
print(arr2) # [[0, 0, 0], [0, 0, 0]]
print(*arr1) # 0 0 0 // unpack (한 행을 가져오면 언팩가능)

for i in range(2):
    print(arr2[i])
# 0 0 0
# 0 0 0

for i in range(2):
    for j in range(3):
        print(arr2[i][j], end=" ")
    print()
# 0 0 0
# 0 0 0
# 0 0 0

##########################################

arr = [[1,2,3],[4,5,6]]
print(len(arr)) # 2 // arr 요소의 갯수
print(len(arr[0])) # 3 // [1,2,3] 요소의 갯수

## 참조
# 이런 방식으로 쓰면 안됨
# 두 개의[0,0,0] 요소가 같은 메모리를 참조하기에 하나의 자리를 바꾸면 둘다 바뀜
#arr = [[0]*3]*2 # [[0,0,0],[0,0,0]]


