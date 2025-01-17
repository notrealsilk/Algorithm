# 크로아티아 알파벳 목록
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

# 크로아티아 알파벳을 모두 '*'로 치환
for alpha in croatia:
    word = word.replace(alpha, '*')

print(len(word))
