while True:
  menu = input("1) fahrenheit -> celsius 2) celsius -> fahrenheit 3) quit program : ")
  if menu == '1':
    fahrenheit = float(input('input fahrenheit : '))
    print(f'Fahrenheit: {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5/9):.4f}C')
  elif menu == '2':
    celsius = float(input('input celsius : '))
    print(f'celsius: {celsius}C, fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')
  elif menu == '3':
    print("terminate program")
    break