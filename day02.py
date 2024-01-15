univ = "Inha univ"
print(univ)
print(univ[5])
# univ[5] = 'U" //immutable
subjects = ['python', 'c++', 'linux', 'datastructure', 'db']
print(subjects)
print(subjects[3])
subjects[3] = 'datastructure & algorithm' # mutable
print(subjects)
# print(0.1)
# print(1e-1)
# print(0.01)
# print(1e-2)

#파이썬 키워드들은 변수명으로 사용 불가
#case-sensitive
# ok
abc = 7
Abc = 8
ABC = 6
print(abc, Abc, ABC)

test9 = 77
# 9test = tt 변수명 숫자로는 시작 못함
_9test = 11
print(test9, _9test)

# False = 123 안된다, reserved words

print(type(3.14))
print(isinstance(3.14, float))

artists = ["BTS", "Newjeans", "ive", "nmixx", "aespa"]
groups = artists
artists[2] = "seventeen"
print(artists, groups)