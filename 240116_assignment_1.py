# 1월 16일 과제-프로그램 확장하기(3번 단독소수 판정, 4번 구간소수 판정)

while True:
    menu = input(
        "1) fahrenheit -> celsius 2) celsius -> fahrenheit 3) one-prime number 4) finding prime number between 2-numbers 5) press any key except 1~4 to exit: ")
    if menu == '1':
        fahrenheit = float(input('input fahrenheit : '))
        print(f'Fahrenheit: {fahrenheit}F, Celsius : {((fahrenheit - 32.0) * 5 / 9):.4f}C')
    elif menu == '2':
        celsius = float(input('input celsius : '))
        print(f'celsius: {celsius}C, fahrenheit : {((celsius * 9.0 / 5.0) + 32.0):.4f}F')
    elif menu == '3':
        number = int(input('input number'))
        is_prime = True
        i = 2
        while i < number:
            if number % i == 0:
                is_prime = False
                break
            i = i + 1
        if is_prime:
            print(f'{number} is prime number')
        else:
            print(f'{number} is not prime number')
    elif menu == '4':
        nums = input('input 2 numbers : ').split()

        n1 = int(nums[0])
        n2 = int(nums[1])
        if n1 > n2:
            n1, n2 = n2, n1

        for num in range(n1, n2 + 1):
            is_prime = True

            if num < 2:
                pass
            else:
                for i in range(2, num):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime: print(num, end=' ')
        print()


    else:
        print("exit")
        break
