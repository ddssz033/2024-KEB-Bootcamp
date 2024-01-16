#두개의 숫자 사이 소수들
numbers = input("input number : ").split()

n1 = int(numbers[0])
n2 = int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1 #왼쪽이 더 큰 경우 swapping

for number in range(n1, n2+1):
    is_prime = True  # int -> bool

    if number < 2:
        pass
    else:
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break
        if is_prime: print(number, end=' ')
