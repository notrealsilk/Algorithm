stu_list = []

# 제출한 학생 stu_list에 저장
for i in range(28):
    stu_list.append(int(input()))

# 제출 안 한 학생 색출
min_stu_num = 0
max_stu_num = 0

for num in range(1, 31):
    if num not in stu_list:
        # 학생 1 색출
        if min_stu_num == 0:
            min_stu_num = num
            continue
        # 학생 2 색출 -> 색출 완료
        else:
            max_stu_num = num
            break

print(min_stu_num)
print(max_stu_num)
