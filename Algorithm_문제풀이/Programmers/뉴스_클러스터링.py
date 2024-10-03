# 문자열 두글자씩 끊어서 다중 집합의 원소 만들기
def seper(s):
    string = []
    for i in range(len(s) - 1):
        tem = s[i:i + 2]
        if not tem.isalpha():  # 알파벳이 아닌 문자열이 포함돼있다면 추가 안함
            continue
        string.append(tem)

    return string


def solution(str1, str2):
    answer = 65536

    # 대문자로 바꾸기
    str1 = str1.upper()
    str2 = str2.upper()

    # 1. 문자열 분리하는 함수에 넣기
    A = seper(str1)
    B = seper(str2)

    # 집합 모두 공집합이면 바로 리턴
    if len(A) == 0 and len(B) == 0:
        return answer

    # 2. 교집합
    inter = []  # A와 B의 교집합

    for i in A:
        j = len(B) - 1
        while j >= 0:
            if i == B[j]:
                inter.append(i)
                break
            j -= 1

    # 3. 합집합
    u = A + B

    for w in inter:
        u.remove(w)

    # 4. 자카드 유사도 구하기
    jaccard_i = len(inter)
    jaccard_j = len(u)

    jaccard_similarity = jaccard_i / jaccard_j

    answer = int(answer * jaccard_similarity)

    return answer

str1 = "FRANCE"
str2 = "french"

result = solution(str1,str2)
print(result)