#prime number
number = int(input("input number : "))
cnt = 0
i = 1
while i <= number:
    if number % i == 0:
        cnt = cnt + 1
    i = i + 1

if cnt == 2: #나누어 떨어지는 수가 1과 자기 자신뿐인 경우
    print(f'{number} is prime number')
else: #그외(소수가 아님)
    print(f'{number} is not prime number')



# subjects = {'python':'kim', 'c++': 'sung', 'datastructure': 'kim', 'db': 'kang'}
# print("{0[python]} {0[datastructure]}".format(subjects))
