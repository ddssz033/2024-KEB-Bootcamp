subjects = ["c++", "5", "java", "python", "java", "9", "데이터베이스", "리눅스"]
subjects = subjects[::-1]
print(subjects)
#지울때는 del이나 pop을 쓰자, remove는 피하자
# subjects.pop(2)
# print(subjects)
# subjects.sort(reverse = True)
print(subjects)
copy_subjects = sorted(subjects)
print(subjects)
print(copy_subjects)