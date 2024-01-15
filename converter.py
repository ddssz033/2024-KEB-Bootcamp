# 화씨 섭씨 계산 프로그램을 반복문을 사용하여 만들기, 3번을 누를 경우 종료

while True:
  menu = input("1) fahrenheit -> celsius 2) celsius -> fahrenheit 3) quit program : ")
  if menu == '1':
    fahrenheit = float(input('input fahrenheit : '))
    print(f'Fahrenheit: {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5/9):.4f}C')
  elif menu == '2':
    celsius = float(input('input celsius : '))
    print(f'celsius: {celsius}C, fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
  else:
    print("terminate program")
    break
