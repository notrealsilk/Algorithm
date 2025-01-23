# 시각
N = int(input())

# '3'이 포함된 경우 계산
minutes_with_three = 15  # '3'이 포함된 분/초 (03, 13, 23, 30~39, 43, 53)
total_minutes = 60

result = 0

for hour in range(N + 1):
    if '3' in str(hour):  # 시간에 '3'이 포함된 경우
        result += total_minutes ** 2  # 모든 경우: 60(분) × 60 (초)
    else:  # 시간에 '3'이 포함되지 않은 경우
        result += (minutes_with_three * total_minutes) + (minutes_with_three * (total_minutes - minutes_with_three))

print(result)
