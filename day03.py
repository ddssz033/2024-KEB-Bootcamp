#prime number
number = int(input("input number : "))
is_prime = True #int -> bool
i = 2
while i < number:
    if number % i == 0:
        is_prime = False # +을 제거함
        break
    i = i + 1

if is_prime: # ==을 제거
    print(f'{number} is prime number')
else: #그외(소수가 아님)
    print(f'{number} is not prime number')



# subjects = {'python':'kim', 'c++': 'sung', 'datastructure': 'kim', 'db': 'kang'}
# print("{0[python]} {0[datastructure]}".format(subjects))
