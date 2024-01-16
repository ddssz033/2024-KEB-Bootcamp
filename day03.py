# 값을 찾지 못할 시 -1이 아닌 valueerror을 출력하는 index를 사용할 경우

subjects = "python c++ database linux"
subject = input("과목 입력: ")
#예외 처리 필요
try: #정상작동하는 경우
    print(f"해당 과목이 존재합니다. 위치는 {subjects.index(subject)}번 인덱스입니다")
except ValueError: #못찾은 경우(ValueError)
    print('해당 과목이 없습니다')