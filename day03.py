subjects = "python c++ database linux"
subject = input("과목 입력: ")
if subjects.find(subject) != -1: #찾은 경우(값이 -1이 아닌경우)
    print(f"해당 과목이 존재합니다. 위치는 {subjects.find(subject)}번 인덱스입니다")
else:
    print('해당 과목이 없습니다')