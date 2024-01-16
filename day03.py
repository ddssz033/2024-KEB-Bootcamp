course = "* KEB 2024# KEB !Bootcamp KEB...*!#"
print(course.find('KEB')) #마이너스가 뜰 경우 찾지 못함
print(course.rfind('KEB')) #뒤부터 찾는다
print(course.find('Inha')) #-1
# print(course.index('Inha')) #valueerror
print(course)
course = course.replace('KEB', 'Inha', 1)
print(course)
print(course.strip())
print(course.strip("!#.*"))
# print(course)
# course = course.replace('KEB', "Inha")
# print(course)

#strip: 불필요한 공백을 없애줌, 특정 문자를 없앨수도 있다, 양쪽 끝만 제거