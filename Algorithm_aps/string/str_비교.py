s1 = 'abc'
s2 = 'abc'
s3 = s1[:2]+'c'

print(s1 == s2) # True
print(s1 == s3) # True
print(s1 is s3) # False