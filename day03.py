#join: 리스트를 문자열로, 원소사이 구분기호들을 임의로 붙일수 있다
subjects = ["python", "c++", "database"]
subjects_string = "/".join(subjects)
print(subjects_string)

numbers = input("firstnum secondnum : ").split() # 문자열을 리스트로
print(int(numbers[0]) + int(numbers[1]))

